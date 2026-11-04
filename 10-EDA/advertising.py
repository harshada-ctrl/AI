# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 22:18:22 2026

@author: Admin
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Load dataset and clean column names
df = pd.read_csv('C:/10-EDA/advertising.csv')
df.columns = (
    df.columns.str.strip().str.replace(' ', '_').str.replace('__', '_')
)

print('Dataset Dimensions:', df.shape)
print('\nMissing Values:\n', df.isnull().sum())
print('\nData Types:\n', df.dtypes)
print('\nTarget Class Distribution:\n', df['Clicked_on_Ad'].value_counts())

'''
Inference:

Dataset Scale: Contains 1,000 rows and 10 attributes without any missing (NaN) values.

Balanced Target: Exactly 500 instances for Clicked_on_Ad = 1 and 500 for Clicked_on_Ad = 0 
(50:50 distribution), removing the need for synthetic sampling techniques like SMOTE.

High Cardinality: City has 969 unique values and Country has 237 unique values across 1,000 rows, 
indicating that direct one-hot encoding on raw location columns would create excessive sparsity.
'''

numeric_cols = [
    'Daily_Time_Spent_on_Site',
    'Age',
    'Area_Income',
    'Daily_Internet_Usage',
]
print(df[numeric_cols].describe().T[['mean', 'std', 'min', '50%', 'max']])

'''Inference:

Demographics: The user base spans young to middle-aged adults (19 to 61 years), with 50% 
falling between 29 and 42 years.

Usage & Income Spread: The standard deviations and close alignment between mean and median 
values across all numerical features show relatively normal, symmetric distributions without 
severe extreme outliers.'''


# Group comparison between users who clicked vs. did not click
grouped_stats = df.groupby('Clicked_on_Ad')[numeric_cols].mean()
print(grouped_stats)

# Visualizing separation
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
for col, ax in zip(numeric_cols, axes.flatten()):
  sns.kdeplot(
      data=df,
      x=col,
      hue='Clicked_on_Ad',
      fill=True,
      common_norm=False,
      palette='Set1',
      ax=ax,
  )
  ax.set_title(f'Distribution of {col} by Click Status')
plt.tight_layout()
plt.show()

'''Inference:

High-Intent Profile: Users who click on ads spend substantially less time browsing the internet 
and site overall, have a lower average area income, and tend to be older (~40 years).

Low-Intent Profile: Heavy internet users (200+ min/day) and users spending over 75 minutes on the 
site rarely click on ads, likely exhibiting higher ad-blindness or intentional site navigation.'''


# Pearson correlation with target variable
corr_matrix = df[numeric_cols + ['Clicked_on_Ad', 'Male']].corr()
print('Correlation with Clicked_on_Ad:\n', corr_matrix['Clicked_on_Ad'])

# Heatmap
plt.figure(figsize=(7, 5))
sns.heatmap(
    corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5
)
plt.title('Correlation Heatmap')
plt.show()

'''Inference:Primary Predictive Drivers: Daily_Internet_Usage ($r = -0.79$) and Daily_Time_Spent_on_Site ($r = -0.75$) 
exhibit a very strong negative correlation with ad clicks.Secondary Drivers: Age ($r = 0.49$) 
shows a moderate positive relationship, while Area_Income ($r = -0.48$) shows a moderate negative
 relationship.Insignificant Features: Male shows negligible linear correlation ($r = -0.038$), 
 indicating gender distribution is balanced across both cohorts and has minimal individual 
 predictive power.'''
 
 # Parse timestamp into temporal components
df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%d/%m/%Y %H:%M')
df['Hour'] = df['Timestamp'].dt.hour
df['DayOfWeek'] = df['Timestamp'].dt.day_name()
df['Month'] = df['Timestamp'].dt.month_name()

# Check click rates across hours
hourly_clicks = df.groupby('Hour')['Clicked_on_Ad'].agg(['count', 'mean'])
print('Top 3 click-rate hours:\n', hourly_clicks.sort_values(by='mean', ascending=False).head(3))

'''Inference:

Ad engagement is evenly distributed across calendar months and days of the week without 
severe seasonality.

Hourly breakdowns show consistent baseline traffic with marginal click upticks during
late-evening/night hours (08:00 PM – 01:00 AM) and early mornings (07:00 AM – 09:00 AM).'''