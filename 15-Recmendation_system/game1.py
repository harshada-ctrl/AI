# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 19:44:39 2026

@author: Admin
"""

# Import necessary libraries
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load the CSV file
file_path = 'C:/15-Recmendation_system/game.csv'
data = pd.read_csv(file_path)

# Step 1: Create a user-item matrix
user_item_matrix = data.pivot_table(index='userId', columns='game', values='rating')

# Step 2: Fill NaN values with 0
user_item_matrix_filled = user_item_matrix.fillna(0)

# Step 3: Compute cosine similarity between users
user_similarity = cosine_similarity(user_item_matrix_filled)
user_similarity_df = pd.DataFrame(
    user_similarity,
    index=user_item_matrix.index,
    columns=user_item_matrix.index)

# Step 4: Recommendation function
def get_collaborative_recommendations_for_user(user_id, num_recommendations=5):
    # Get similarity scores
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)
    similar_users = similar_users.drop(user_id)  # drop self

    # Top 50 most similar users
    top_similar_users = similar_users.head(50)

    # Weighted ratings (dot product of similarity scores with ratings matrix)
    weighted_ratings = top_similar_users.values @ user_item_matrix_filled.loc[top_similar_users.index]

    # Normalize by sum of similarities
    sum_of_similarities = top_similar_users.sum()
    if sum_of_similarities > 0:
        weighted_ratings = weighted_ratings / sum_of_similarities

    # Find games user has not rated
    user_ratings = user_item_matrix_filled.loc[user_id]
    unrated_games = user_ratings[user_ratings == 0]
    
    # Select recommendations only from unrated games
    game_recommendations = pd.Series(weighted_ratings,
                                     index=user_item_matrix_filled.columns).loc[unrated_games.index]
    
    
    return game_recommendations.sort_values(ascending=False).head(num_recommendations)

# Example usage
recommended_games = get_collaborative_recommendations_for_user(511)
print("Recommended games for user 511:")
print(recommended_games)
'''

Why you are getting all 0 recommendations
1. No overlap between users (MOST COMMON)