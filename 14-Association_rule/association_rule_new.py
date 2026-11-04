# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 18:46:01 2026

@author: Admin
"""

# @Author: Dell

# Import required libraries
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

# Sample dataset
transactions = [
    ['Milk', 'Bread', 'Butter'],
    ['Bread', 'Eggs'],
    ['Milk', 'Bread', 'Eggs', 'Butter'],
    ['Bread', 'Eggs', 'Butter'],
    ['Milk', 'Bread', 'Eggs']
]

# Step 1: Convert the dataset into a format suitable for Apriori
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Step 2: Apply the Apriori algorithm to find frequent itemsets
frequent_itemsets = apriori(df, min_support=0.5, use_colnames=True)

# Step 3: Generate association rules from the frequent itemsets
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

# Step 4: Output the results
print("Frequent Itemsets:")
print(frequent_itemsets)

print("\nAssociation Rules:")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

# Interpretation Guide for Students:
# - Support: Higher = more common combo in all transactions
#- confidence: higher = rule is more reliable for predicting RHS from LHS
#- lift:
    > 1 -> positive association (A increses likelihood of B)
    = 1 -> No association(A and B occur toghether by chance)
    < 1 -> Negative association