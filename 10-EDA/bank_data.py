# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 22:18:40 2026

@author: Admin
"""

import numpy as np
import pandas as pd

# Load dataset
df = pd.read_csv('C:/10-EDA/bank_data.csv')

# Dataset shape and memory footprint
print(f'Dataset Dimensions: {df.shape[0]} rows, {df.shape[1]} columns')
print(f'Missing Values: {df.isnull().sum().sum()}')
print(f'Duplicate Rows: {df.duplicated().sum()}')

# Target variable distribution
target_counts = df['y'].value_counts()
target_pct = df['y'].value_counts(normalize=True) * 100
print('\nTarget Variable (y) Distribution:')
print(
    pd.DataFrame(
        {'Count': target_counts, 'Percentage (%)': target_pct.round(2)}
    )
)

'''Inference:

Clean Data Surface: The dataset contains 45,211 customer interactions across 32 features 
without missing values or duplicate rows.

Pre-encoded Categoricals: Categorical features (job, marital status, contact channel, 
 previous campaign outcome) have already been one-hot encoded into binary integer columns.

Severe Class Imbalance: Only 11.70% of clients subscribed to the term deposit (y = 1), while 88.30%
 declined (y = 0). Models evaluated solely on raw accuracy will be misleading (e.g., a naive baseline 
                                                                               
 predicting all 0s achieves 88.3% accuracy); PR-AUC, ROC-AUC, and class-weighted loss functions 
 are necessary.'''
 
 
num_cols = ['age', 'balance', 'duration', 'campaign', 'pdays', 'previous']
summary_stats = df[num_cols].describe().T[
    ['mean', 'std', 'min', '25%', '50%', '75%', 'max']
]
summary_stats['IQR'] = summary_stats['75%'] - summary_stats['25%']
print(summary_stats.round(2))

# Negative balances and pdays placeholder checks
print(
    f"\nClients with negative balances: {(df['balance'] < 0).sum()} ({(df['balance'] < 0).mean()*100:.2f}%)"
)
print(
    f"Clients not previously contacted (pdays == -1): {(df['pdays'] == -1).sum()} ({(df['pdays'] == -1).mean()*100:.2f}%)"
)

'''Inference:

Extreme Positive Skewness: balance (max 102,127 vs. median 448) and duration (max 4,918 sec vs. 
median 180 sec) exhibit long right tails. Over 3,766 clients (8.33%) carry a negative account 
balance.

Special Value Encoding in pdays: Exactly 81.74% of records have pdays = -1 (and previous = 0), 
indicating they were never contacted in earlier marketing campaigns. Treating pdays as a regular 
continuous variable will skew linear estimators; it requires a dedicated indicator flag (e.g., 
previously_contacted = 0/1).

Campaign Outliers: Most clients are contacted 1 to 3 times (75th percentile = 3),
 but upper extremes reach up to 63 calls for a single client.'''
 
 # Comparing metric central tendencies across conversion outcomes
grouped_comparison = df.groupby('y')[num_cols].agg(['mean', 'median']).T
print(grouped_comparison.round(2))

# Top positive and negative linear correlations with target variable
target_corr = df.corr()['y'].sort_values(ascending=False)
print('\nTop 5 Positive Correlations with y:\n', target_corr.iloc[1:6].round(3))
print(
    '\nTop 5 Negative Correlations with y:\n',
    target_corr.tail(5).sort_values().round(3),
)



'''
Inference:

Duration as the Single Strongest Predictor: Average call duration for successful 
conversions is 2.43x higher (537 seconds vs. 221 seconds). However, call duration is 
unknown before making the call; including raw duration in a prospective lead-scoring model 
creates target leakage.

Capital Buffer Matters: Customers who subscribe hold 38.4% higher average account 
balances (€1,804 vs. €1,304) and 75.8% higher median balances (€733 vs. €417).

Prior Success Transfer: poutsuccess holds a +0.307 correlation with current campaign 
conversion, indicating existing client satisfaction is highly reusable.
'''


job_cols = [c for c in df.columns if c.startswith('jo')]
con_cols = [c for c in df.columns if c.startswith('con_')]
pout_cols = [c for c in df.columns if c.startswith('pout')]
fin_cols = ['housing', 'loan', 'default']


def compute_rates(columns, label):
  records = []
  for col in columns:
    subset = df[df[col] == 1]
    records.append(
        {
            'Segment': col.replace(label, ''),
            'Total': len(subset),
            'Subscribers': subset['y'].sum(),
            'Conversion_Rate_%': round(subset['y'].mean() * 100, 2),
        }
    )
  return (
      pd.DataFrame(records)
      .sort_values(by='Conversion_Rate_%', ascending=False)
      .reset_index(drop=True)
  )


print('Conversion Rates by Job Profile:\n', compute_rates(job_cols, 'jo'))
print('\nConversion Rates by Contact Method:\n', compute_rates(con_cols, 'con_'))
print(
    '\nConversion Rates by Prior Outcome:\n', compute_rates(pout_cols, 'pout')
)

'''
Inference:

Bimodal Age & Employment Sweet Spots: Students (28.68%) and Retirees (22.79%) convert at more than 
double the baseline rate. Conversely, blue-collar workers (7.27%), entrepreneurs (8.27%), and 
housemaids (8.79%) show low responsiveness.

Massive Retention on Past Success: When the previous campaign outcome was successful (poutsuccess), 
the repeat conversion rate surges to 64.73%.

Debt Load Suppresses Deposit Uptake: Customers burdened by a housing loan have less than half 
the conversion probability of debt-free clients (7.70% vs. 16.70%).

Contact Channel Quality: Unknown communication channels yield only 4.07% conversion 
compared to ~14.9% on verified mobile numbers (con_cellular).
'''

# Binning campaign contacts to observe decay in conversion efficiency
df['campaign_bins'] = pd.cut(
    df['campaign'],
    bins=[0, 1, 2, 3, 5, 10, 100],
    labels=['1 call', '2 calls', '3 calls', '4-5 calls', '6-10 calls', '>10 calls'],
)

decay_df = df.groupby('campaign_bins', observed=False)['y'].agg(
    Leads='count',
    Conversions='sum',
    Conversion_Rate=lambda x: round(x.mean() * 100, 2),
)
print(decay_df)

'''
Inference:

Sharp Diminishing Returns: The initial call produces the highest conversion rate (14.60%).
 By the 4th contact, conversion drops to 8.63%, and beyond 10 calls it falls to 3.93%.

Operational Optimization: Capping outbound attempts at 3 contacts per campaign preserves 
over 86.6% of all convertible leads while eliminating thousands of redundant, high-friction 
sales calls.
'''