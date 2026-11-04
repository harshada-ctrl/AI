# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 18:49:45 2026

@author: Admin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#create the dataframe
data = {
        'person name': ['rob', 'tom', 'xi', 'mohan', 'pooja', 'sofiya'],
        'credit score':[750, 310, 475, 600, 820, 780],
        'income':[80000, 32000, 77000, 65000, 550000, 750000],
        'age':[32, 45, 33, 51, 35, 31],
        'loan approved?': ['y', 'n', 'y', 'n', 'y', 'y']
        }
df = pd.DataFrame(data)

#apply log transformation to income
df['log_income'] = np.log(df['income'])

#plotting
plt.figure(figsize=(10, 6))

#original income
plt.bar(df['person name'], df['income'], color='skyblue', label='original income')

#log-transformed income (plotted next to original)
plt.bar(df['person name'], df['log_income'] * 10000, color='orange', alpha=0.7, label='log(income) X 10000')

plt.xlabel('person name')
plt.ylabel('income')
plt.title( 'original vs log-transformed income ')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt. show()
