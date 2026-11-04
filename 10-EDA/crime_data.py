# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 21:59:46 2026

@author: Admin
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. Load dataset and basic inspection
df = pd.read_csv('C:/10-EDA/crime_data.csv')
df = df.rename(columns={'Unnamed: 0': 'State'})

print("Dataset Shape:", df.shape)
print("\nData Types & Non-Null Counts:")
df.info()
print("\nFirst 5 Records:")
print(df.head())

'''Inference:

The dataset contains 50 rows and 5 columns, representing 50 US states across crime statistics 
(Murder, Assault, Rape per 100,000 residents) and demographic data (UrbanPop, percentage of population
living in urban areas).

All crime and population variables are numeric (float64 and int64), while the state identifier 
is a string (object).'''

# 2. Check for missing values and duplicates
missing_count = df.isnull().sum()
duplicate_count = df.duplicated().sum()

print("Missing values per column:\n", missing_count)
print("Duplicate rows:", duplicate_count)

'''
Inference:

There are zero missing values across all columns and no duplicated entries. The dataset is 
clean and ready for analytical computation without imputation.

'''

# 3. Descriptive statistics
summary_stats = df.describe().T[['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']]
summary_stats['IQR'] = summary_stats['75%'] - summary_stats['25%']
print(summary_stats)

'''
Inference:

Assault shows the largest scale and dispersion, ranging from 45 to 337 with a mean of 170.76 
and standard deviation of 83.34.

Murder averages 7.79 (median = 7.25), ranging from a low of 0.80 (North Dakota) to 17.40 (Georgia).

Rape rates average 21.23 with a median of 20.10, ranging from 7.30 to 46.00.

UrbanPop has a mean of 65.54% (median = 66.0%), spanning between 32% and 91%, indicating 
an even demographic spread across rural and urban-heavy states.
'''

# 4. Outlier detection using Interquartile Range (IQR)
numeric_cols = ['Murder', 'Assault', 'UrbanPop', 'Rape']

for col in numeric_cols:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    print(f"{col}: {len(outliers)} outlier(s) detected -> {outliers[['State', col]].to_dict(orient='records') if len(outliers) > 0 else 'None'}")
    
    
'''
Inference:Murder, Assault, and UrbanPop have no univariate outliers under the 1.5 $\times$ IQR rule.
Rape contains 2 upper-bound outliers: Nevada (46.0) and Alaska (44.5), where reported rates are 
substantially higher than the 75th percentile benchmark (26.18).
'''


# 5. Correlation analysis
corr_matrix = df[numeric_cols].corr()
print("Correlation Matrix:\n", corr_matrix.round(3))


'''
Inference:Murder and Assault have a very strong positive correlation ($r = 0.802$): 
    States with elevated assault figures almost universally exhibit elevated homicide rates.
    Assault and Rape are moderately-to-strongly correlated ($r = 0.665$), and Murder and Rape 
    show moderate positive correlation ($r = 0.564$).UrbanPop has a negligible correlation with 
    Murder ($r = 0.070$) and a modest correlation with Assault ($r = 0.259$). A higher percentage 
    of urban population does not inherently drive higher violent homicide rates in this dataset. 
    However, UrbanPop shows a moderate correlation with Rape ($r = 0.411$).
'''

# 6. Top states by crime category
for col in ['Murder', 'Assault', 'Rape']:
    top_5 = df.sort_values(by=col, ascending=False)[['State', col]].head(5).to_dict(orient='records')
    print(f"Top 5 states for {col}: {top_5}")
    
    
'''
Inference:

Murder: Heavily concentrated in Southern states — Georgia (17.4), Mississippi (16.1), 
Florida (15.4), Louisiana (15.4), and South Carolina (14.4).

Assault: Highest in North Carolina (337), Florida (335), Maryland (300), Arizona (294), and 
New Mexico (285). Florida ranks in the top 3 for both Assault and Murder.

Rape: Highest in Western/Southwestern states — Nevada (46.0), Alaska (44.5), California (40.6), 
Colorado (38.7), and Michigan (35.1).
'''

# 7. Visualizations
plt.figure(figsize=(14, 10))

# Correlation Heatmap
plt.subplot(2, 2, 1)
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", square=True)
plt.title('Correlation Heatmap')

# Distribution of Crimes
plt.subplot(2, 2, 2)
df[numeric_cols].boxplot()
plt.title('Distribution & Outlier Spread (Boxplots)')
plt.ylabel('Rate / Percentage')

# Murder vs Assault Scatter Plot
plt.subplot(2, 2, 3)
sns.regplot(data=df, x='Assault', y='Murder', color='darkred')
plt.title('Murder vs Assault (r = 0.80)')
plt.xlabel('Assault (per 100k)')
plt.ylabel('Murder (per 100k)')

# UrbanPop vs Rape Scatter Plot
plt.subplot(2, 2, 4)
sns.regplot(data=df, x='UrbanPop', y='Rape', color='darkblue')
plt.title('UrbanPop vs Rape (r = 0.41)')
plt.xlabel('Urban Population (%)')
plt.ylabel('Rape (per 100k)')

plt.tight_layout()
plt.show()

'''
Inference:

Feature scaling (such as StandardScaler or MinMaxScaler) is mandatory prior to applying 
distance-based machine learning algorithms (like K-Means, Hierarchical Clustering, or PCA) 
because Assault has a magnitude scale over 15–20 times larger than Murder and Rape.
'''