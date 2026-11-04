# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:34:46 2026

@author: Admin
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler, PowerTransformer
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import VarianceThreshold
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE

#load the titanic dataset
df = sns.load_dataset('titanic')
print("initial shape:", df.shape)
df.head()

#check missing value
print("missing values:\n", df.isnull().sum())

#drop columns with too many missing values
df.drop(columns=['deck'], inplace=True)

#fill categorical missing values with mode, numerical with mean
cat_cols = df.select_dtypes(include='object').columns
num_cols = df.select_dtypes(include=['int64 ', 'float64']).columns

for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])
    
 '''   
if there are multiple modes:
returns
S
type: object
why [O] is required?
fillna() needs ONE single value
[O] selects the first most frequent value
ensures the code always works, even if multiple modes exist
'''

for col in num_cols:
    df[col] = df[col].fillna(df[col])
    
    
    
    
    
    
from scipy.stats import skew

#Import powertransformer (not used directly here, but commonly used for)
from sklearn.preprocessing import powertransformer


#calculate skewness of the fare column
#dropna() removes missing values because skew() cannot work with nans
skew_value = skew(df['fare'].dropna())

#print skew value for understanding(optional)
print("skewness value:", skew_value)

#if skewness is greater than 0, data is positively right skewd
if skew_value > 0:
    
    #inform user that right skew is detected
    print("positive skew detected -> applying log transformation")
    
    # Apply log(l + x) transformation
# loglp is used to safely handle zero values
# This compresses lar e values on the ri ht side

df['fare_transformed'] = np.log























