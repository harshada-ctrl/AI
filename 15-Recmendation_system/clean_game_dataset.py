# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:46:28 2026

@author: Admin
"""

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load data
data = pd.read_csv('C:/15-Recmendation_system/cleaned_game_dataset.csv')

# Step 1: Create user-item matrix
user_item = data.pivot_table(index='userId', columns='game', values='rating')

# Step 2: Replace NaN with 0
user_item_filled = user_item.fillna(0)

# Step 3: Compute item-item similarity
item_similarity = cosine_similarity(user_item_filled.T)

# Convert to DataFrame for easy handling
item_similarity_df = pd.DataFrame(item_similarity,
                                  index=user_item_filled.columns,
                                  columns=user_item_filled.columns)

print("Total users:", len(user_item))

print("Total users:", len(user_item_filled.index))
print(user_item_filled.index[:20])


def recommend_games(user_id, num_recommendations=5):
    if user_id not in user_item_filled.index:
        print("User not found in dataset")
        return None

    user_ratings = user_item_filled.loc[user_id]
    rated_games = user_ratings[user_ratings > 0]

    scores = {}

    for game, rating in rated_games.items():
        similar_games = item_similarity_df[game]
        
        for sim_game, similarity in similar_games.items():
            if sim_game not in rated_games.index:
                
                if similarity > 0: # important
                
                 if sim_game not in scores:
                    scores[sim_game] = 0
                    
                    scores[sim_game] += similarity * rating
                    
    if len(scores) == 0:
        print("No recommendations found")
        return none
    
    return pd.Series(scores).sort_values(ascending=False).head(num_recommendations)
print(recommend_games(6))


        