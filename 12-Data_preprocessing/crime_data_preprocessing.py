# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 17:59:21 2026

@author: Admin
"""



import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.feature_selection import VarianceThreshold
from sklearn.impute import SimpleImputer
from feature_engine.outliers import Winsorizer
from imblearn.over_sampling import SMOTE

# ==========================================
# 1. Load Crime Data
# ==========================================
# Standard crime datasets (e.g., US crime data) typically contain:
# 'Unnamed: 0' (State/City identifier), 'Murder', 'Assault', 'UrbanPop', 'Rape'
df = pd.read_csv('C:/12-Data_preprocessing/crime_data.csv')

print("--- Step 1: Initial Shape & Overview ---")
print("Initial Shape:", df.shape)
print(df.head())
print(df.info())

# Inference:
# - Loads the raw crime dataset and displays baseline dimensions and column data types.
# - Renaming the index column (if unnamed) preserves region identifiers for tracking.
if 'Unnamed: 0' in df.columns:
    df.rename(columns={'Unnamed: 0': 'City_State'}, inplace=True)

# ==========================================
# 2. Check & Handle Missing Values
# ==========================================
print("\n--- Step 2: Missing Values Check ---")
print("Missing values per column:\n", df.isnull().sum())

# Separate categorical and numerical columns
cat_cols = df.select_dtypes(include=['object']).columns
num_cols = df.select_dtypes(include=['int64', 'float64']).columns

# Fill categorical missing values with Mode
for col in cat_cols:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].mode()[0])

# Fill numerical missing values with Mean
for col in num_cols:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].mean())

print("Missing values after imputation:\n", df.isnull().sum())

# Inference:
# - Mode imputation preserves the most frequent regional categories without introducing synthetic labels.
# - Mean imputation replaces missing rates with overall feature central tendencies, preventing row loss.

# ==========================================
# 3. Removing Duplicates
# ==========================================
print("\n--- Step 3: Duplicate Handling ---")
initial_rows = df.shape[0]
df.drop_duplicates(inplace=True)
print(f"Removed {initial_rows - df.shape[0]} duplicate row(s). Shape after deduplication: {df.shape}")

# Inference:
# - Duplicate observations distort statistical distribution and artificially inflate sample density; dropping them ensures clean analysis.

# ==========================================
# 4. Outlier Detection & Treatment (Winsorization)
# ==========================================
print("\n--- Step 4: Outlier Treatment ---")
crime_features = [col for col in ['Murder', 'Assault', 'UrbanPop', 'Rape'] if col in df.columns]
if not crime_features:
    crime_features = list(num_cols)



##testing 
import os
import shutil
import matplotlib

cache_dir = matplotlib.get_cachedir()
shutil.rmtree(cache_dir, ignore_errors=True)
print(f"Cleared cache at: {cache_dir}")

#testing




import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager
import os

# 1. Register all Windows fonts directly into fontManager
win_fonts_dir = r"C:\Windows\Fonts"
if os.path.exists(win_fonts_dir):
    for font_file in os.listdir(win_fonts_dir):
        if font_file.lower().endswith(('.ttf', '.otf', '.ttc')):
            try:
                font_manager.fontManager.addfont(os.path.join(win_fonts_dir, font_file))
            except Exception:
                pass

# 2. Pick Arial (guaranteed on Windows)
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial']

# 3. Your plotting code
plt.figure(figsize=(10, 4))
for i, col in enumerate(crime_features, 1):
    plt.subplot(1, len(crime_features), i)
    sns.boxplot(y=df[col])
    plt.title(f"Original {col}")
plt.tight_layout()
plt.show()


#testing










# Display boxplots before winsorization
plt.figure(figsize=(10, 4))
for i, col in enumerate(crime_features, 1):
    plt.subplot(1, len(crime_features), i)
    sns.boxplot(y=df[col])
    plt.title(f"Original {col}")
plt.tight_layout()
plt.show()

# Apply Winsorizer (IQR method, capping both tails at 1.5 IQR)
winsor = Winsorizer(
    capping_method='iqr',
    tail='both',
    fold=1.5,
    variables=crime_features
)
df[crime_features] = winsor.fit_transform(df[crime_features])

# Inference:
# - Outliers in violent crime metrics (such as Rape or Assault) can severely bias clustering/regression centroids.
# - IQR-based Winsorization caps extreme values instead of discarding rows, retaining geographic sample size.

# ==========================================
# 5. Normalization & Standardization
# ==========================================
print("\n--- Step 5: Scaling Features ---")
# Standardization (Mean = 0, Std = 1)
scaler_std = StandardScaler()
df_scaled = df.copy()
df_scaled[crime_features] = scaler_std.fit_transform(df_scaled[crime_features])

# Normalization (Min-Max: [0, 1])
scaler_minmax = MinMaxScaler()
df_minmax = df.copy()
df_minmax[crime_features] = scaler_minmax.fit_transform(df_minmax[crime_features])

# Inference:
# - Features like 'Assault' (values in hundreds) dominate smaller-scale features like 'Murder' (values < 20).
# - Standardization brings all metrics onto an equal footing, crucial for PCA, K-Means clustering, and distance algorithms.

# ==========================================
# 6. Skewness Detection & Transformation
# ==========================================
print("\n--- Step 6: Skewness Handling ---")
for col in crime_features:
    skew_val = skew(df[col].dropna())
    print(f"Feature: {col} | Skewness: {skew_val:.4f}")
    
    if skew_val > 0.5:
        print(f" -> Positive skew in '{col}': Applying Log transformation (np.log1p).")
        df[f'{col}_log'] = np.log1p(df[col])
    elif skew_val < -0.5:
        print(f" -> Negative skew in '{col}': Applying Reflection + Log transformation.")
        reflected = df[col].max() + 1 - df[col]
        df[f'{col}_reflected_log'] = np.log1p(reflected)
    else:
        print(f" -> Feature '{col}' is symmetric. No transformation required.")

# Inference:
# - Severe right-skewness pulls linear model estimates; log1p transformation compresses long right tails towards Gaussian normality.

# ==========================================
# 7. Zero Variance Feature Removal
# ==========================================
print("\n--- Step 7: Zero Variance Removal ---")
df['constant_dummy'] = 1  # Dummy constant column for validation

selector = VarianceThreshold(threshold=0.0)
numeric_df = df.select_dtypes(include=['float64', 'int64'])
df_var_filtered = selector.fit_transform(numeric_df)
retained_cols = numeric_df.columns[selector.get_support()]

print("Retained non-zero variance features:", list(retained_cols))
df = df[list(retained_cols) + list(cat_cols)]

# Inference:
# - Zero-variance features carry zero statistical information and increase computation without predictive value.

# ==========================================
# 8. Categorical Encoding (Dummy Variables)
# ==========================================
print("\n--- Step 8: One-Hot Encoding ---")
df_encoded = pd.get_dummies(df, drop_first=True)
print("Shape before dummy encoding:", df.shape)
print("Shape after dummy encoding:", df_encoded.shape)

# Inference:
# - Converts qualitative features (like State or Region) into numeric indicator variables while dropping the first level to avoid multicollinearity.

# ==========================================
# 9. Target Imputation & Handling Imbalance (SMOTE)
# ==========================================
print("\n--- Step 9: SMOTE Imbalance Handling ---")
# Example setup: Creating binary risk target if unlabelled
if 'Crime_Risk' not in df_encoded.columns:
    median_murder = df_encoded['Murder'].median() if 'Murder' in df_encoded.columns else 0
    df_encoded['Crime_Risk'] = (df_encoded['Murder'] > median_murder).astype(int)

X = df_encoded.drop(columns=['Crime_Risk'])
y = df_encoded['Crime_Risk']

# Impute any residual NaN values prior to resampling
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)

smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_imputed, y)

print("Class distribution before SMOTE:\n", y.value_counts())
print("Class distribution after SMOTE:\n", pd.Series(y_resampled).value_counts())

# Inference:
# - Synthesizes minority risk profiles using k-nearest neighbors to balance training data and prevent bias toward the majority class.





