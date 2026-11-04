# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 19:18:16 2026

@author: Admin
"""

# Association Rule Simulation with Explanations
from collections import Counter

# Sample transaction dataset
transactions = [
    {'milk', 'bread', 'butter'},
    {'milk', 'bread'},
    {'milk', 'butter'},
    {'bread', 'butter'},
    {'milk', 'bread', 'butter'},
    {'bread', 'butter', 'jam'},
    {'milk', 'bread'},
]

# Helper function: Calculate support
def support(itemset):
    count = sum(1 for t in transactions if itemset.issubset(t))
    return count / len(transactions)  
# Support = proportion of transactions containing the itemset

# Function to calculate Support, Confidence, Lift for a rule: A → B
def rule_metrics(A, B):
    supp_A = support(A)         # P(A) → how often A occurs
    supp_B = support(B)         # P(B) → how often B occurs
    supp_A_B = support(A | B)   
    # P(A ∩ B) → how often A and B occur together
    
    confidence = supp_A_B / supp_A  # P(B | A) → probability of B given A
    lift = confidence / supp_B      # Lift = confidence / P(B), checks association strength
    
    return supp_A_B, confidence, lift

# Example 1: Rule {milk} → {bread}
A = {'milk'}
B = {'bread'}

supp, conf, lift_val = rule_metrics(A, B)

print(f"Rule: {A} → {B}")
print(f"Support: {supp:.2f}  → {supp*100:.1f}% of transactions contain both milk and bread")
print(f"Confidence: {conf:.2f}  → When milk is bought, bread is also bought {conf*100:.1f}% of the time")
print(f"Lift: {lift_val:.2f}  → Customers buying milk are {lift_val:.2f} times more likely to buy bread than a random customer")

# Example 2: Rule {bread} → {jam}
A = {'bread'}
B = {'jam'}

supp, conf, lift_val = rule_metrics(A, B)

print(f"\nRule: {A} → {B}")
print(f"Support: {supp:.2f}  → {supp*100:.1f}% of transactions contain both bread and jam")
print(f"Confidence: {conf:.2f}  → When bread is bought, jam is also bought {conf*100:.1f}% of the time")
print(f"Lift: {lift_val:.2f}  → Customers buying bread are {lift_val:.2f} times more likely to buy jam than a random customer")

# ----------------------------
# Interpretation Guide:
# - Support: Higher means the combination is common in the dataset.
# - Confidence: Higher means the rule is more reliable in predicting B from A.
# - Lift:
#       > 1  → Positive association (A increases likelihood of B)
#       = 1  → No association (A and B occur together by chance)
#       < 1  → Negative association (A reduces likelihood of B)
# ----------------------------
1. Market Basket Analysis (Retail / E-commerce)

Example Rule: {Milk} → {Bread}

Practical Use: If a store sees that milk buyers often buy bread, they can:

Place milk and bread close to each other to boost sales.

Offer bundle discounts (buy milk, get bread at 10% off).

Create personalized recommendations (“You may also like…”).

Impact: Increases average basket size and revenue.

2. Cross-Selling in Online Shopping

Example Rule: {Laptop} → {Laptop Bag}

Practical Use: Amazon, Flipkart, etc., can automatically suggest laptop bags when a laptop is in the cart.

Impact: Improves customer convenience and boosts accessory sales.

3. Inventory Planning

Example Rule: {Ice cream} → {Chocolate Sauce}

Practical Use: Stock these items together during summer promotions so both are available simultaneously.

Impact: Reduces lost sales due to missing complementary products.

4. Customer Segmentation for Marketing

Example Rule: {Yoga Mat} → {Organic Smoothie Mix}

Practical Use: Send targeted email campaigns to yoga mat buyers with smoothie mix offers.

Impact: Higher conversion rates due to relevance.
5.Fraud Detection

Example Rule: {Unusual Login Location} → {Large Transfer}

Practical Use: In banking, if an unusual login location is often followed by a large transfer, flag for review.

Impact: Prevents fraudulent transactions.