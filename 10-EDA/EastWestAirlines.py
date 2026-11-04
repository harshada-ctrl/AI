# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 22:18:57 2026

@author: Admin
"""

import numpy as np
import pandas as pd

# Load the Excel workbook and primary sheet
xls = pd.ExcelFile('C:/10-EDA/EastWestAirlines.xlsx')
print('Available Sheets:', xls.sheet_names)

df = pd.read_excel('C:/10-EDA/EastWestAirlines.xlsx', sheet_name='data')

# Shape, missing values, and duplicates
print(f'Dimensions: {df.shape[0]} rows, {df.shape[1]} columns')
print(f'Total Missing Values: {df.isnull().sum().sum()}')
print(f"Duplicate Customer Records: {df.drop(columns=['ID#']).duplicated().sum()}")
print('\nTarget Variable (Award?) Distribution:')
print(df['Award?'].value_counts(normalize=True).mul(100).round(2).astype(str) + '%')

'''
Inference:

Data Completeness: The dataset comprises 3,999 loyalty member records across 12 features with 
zero missing (NaN) entries.

Target Balance: 37.03% of members have redeemed or won a free award flight (Award? = 1), 
while 62.97% have not (Award? = 0). The distribution is moderately balanced; standard stratified 
sampling during validation is sufficient without aggressive oversampling.

Metadata Column: ID# is an arbitrary sequential primary key and must be dropped prior to 
statistical clustering or predictive modeling to avoid synthetic indexing bias.
'''


features = df.drop(columns=['ID#'])
summary_df = features.describe().T[['mean', 'std', 'min', '25%', '50%', '75%', 'max']]
summary_df['Skewness'] = features.skew()
print(summary_df.round(2))

'''
Inference:
Extreme Right Skewness: Features like Balance ($\text{skew} = 5.00$), Qual_miles ($7.51$), 
and Flight_miles_12mo ($7.45$) show heavy positive skew. For Balance, the maximum (1.70M) 
is nearly 40 times higher than the median (43.1k). Distance-based clustering (e.g., K-Means) 
will be severely biased unless robust scaling (RobustScaler) or power transformations ($\log(1+x)$) 
are applied.

Symmetric Tenure: Days_since_enroll is approximately normally distributed 
($\text{skew} = 0.12$) with a median tenure of ~4,096 days (~11.2 years), showing consistent 
enrollment spread across customer lifespans.
'''

# Calculating the sparsity / zero proportion per feature
zero_pct = (df == 0).mean().mul(100).sort_values(ascending=False)
print('Zero-Inflation Rates (% of zero values):')
print(zero_pct[zero_pct > 0].round(2).astype(str) + '%')


'''
Inference:

Dormancy on Qualification Miles: Over 94% of members have zero Qual_miles, indicating that 
qualification status is an elite tier achieved by less than 6% of the customer base.

Annual Flight Inactivity: 68.09% of members took zero flights in the past 12 months 
(Flight_miles_12mo = 0 and Flight_trans_12 = 0). The program's engagement is predominantly 
anchored around credit card and bonus accruals rather than active air travel.

Near-Zero Variance in Secondary Credit Cards: cc2_miles and cc3_miles have over 98% of 
values stuck at tier 1. They represent specialized cards with very low adoption across the 
broader membership base.
'''

# Comparing means across award status
award_comp = df.drop(columns=['ID#']).groupby('Award?').mean().T
award_comp.columns = ['No Award (0)', 'Award Redeemed (1)']
award_comp['Ratio (1 / 0)'] = (
    award_comp['Award Redeemed (1)'] / award_comp['No Award (0)']
).round(2)
print(award_comp.round(2))

# Correlation with target Award?
corr_target = (
    df.drop(columns=['ID#'])
    .corr()['Award?']
    .sort_values(ascending=False)
    .drop('Award?')
)
print('\nCorrelation with Award? Status:\n', corr_target.round(3))

'''
Inference:
    Primary Drivers of Redemptions: Bonus_miles ($r = 0.374$), cc1_miles ($r = 0.335$), 
and Bonus_trans ($r = 0.334$) exhibit the highest positive association with award redemption. 
Members actively accumulating reward points through airline co-branded credit cards are far 
more likely to redeem awards.

Flight Velocity: Active award redeemers fly nearly 4x more transactions (Flight_trans_12 = 2.60 vs. 0.65) 
and accumulate 2.8x more bonus miles (28.9k vs. 10.2k).

Tenure Effect: Longer-enrolled members 
have a modest positive bias toward award redemption (average tenure of ~12.7 years for 
award holders vs. ~10.5 years for non-holders).'''

# Correlation between flight engagement and bonus engagement metrics
key_corr = df[
    [
        'Bonus_miles',
        'cc1_miles',
        'Bonus_trans',
        'Flight_miles_12mo',
        'Flight_trans_12',
    ]
].corr()
print('Interaction Correlations:\n', key_corr.round(3))

'''
Inference:
    High Collinearity Pairs:Bonus_miles and cc1_miles ($r = 0.826$): Indicates that credit card 
    tier usage directly feeds the accumulated bonus miles pool.
    
    Flight_miles_12mo and Flight_trans_12 ($r = 0.869$): Indicates direct linear coupling between 
    distance flown and flight frequency in the past year.
    Independence of Flying vs. Card Usage: The correlation between cc1_miles and Flight_miles_12mo 
    is essentially zero ($r = 0.038$). 
    This points to two distinct personas: Credit Card Spenders (earn miles via spend without 
   frequent flights) and Frequent Flyers (earn miles primarily through flight segments).
