# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 18:21:29 2026

@author: Admin
"""

import pandas as pd
import numpy as np

# User-Item Matrix (0 - not rated, 1-5 - rating)
user_item_matrix = pd.DataFrame({
    'Game1': [5, 4, 0, 1],
    'Game2': [3, 0, 4, 1],
    'Game3': [0, 2, 5, 4],
    'Game4': [1, 0, 4, 0],
    'Game5': [0, 3, 0, 5]
}, index=['User1', 'User2', 'User3', 'User4'])

print("User-Item Matrix:")
print(user_item_matrix)

# Compute User Similarity (Cosine similarity)
from sklearn.metrics.pairwise import cosine_similarity

# Compute cosine similarity between users
user_similarity = cosine_similarity(user_item_matrix)
similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)


print("\nUser Similarity Matrix:")
print(similarity_df.round(2))


# Step 3: Recommendation function
def recommend(user):

    # Step 1: Find similarity of this user with all others
    sim_users = similarity_df[user]

    # Remove the user itself (similarity with self = 1, not useful)
    sim_users = sim_users.drop(user)

    # Step 2: Sort users by similarity (highest first)
    sim_users = sim_users.sort_values(ascending=False)

    # Take top 2 most similar users (closest "friends")
    top_users = sim_users.head(2)

    # Step 3: Get ratings of these similar users
    # We pick only those rows (users) from the original matrix
    top_user_ratings = user_item_matrix.loc[top_users.index]

    # Step 4: Compute weighted score
    # Multiply ratings with similarity → more similar users influence 
    #more
    scores = np.dot(top_users.values, top_user_ratings)

    # Normalize (divide by total similarity to balance scores)
    scores = scores / top_users.sum()

    # Step 5: Convert scores into a labeled format (Game → Score)
    scores_series = pd.Series(scores, index=user_item_matrix.columns)

    # Step 6: Find games not yet rated by the user
    unseen = user_item_matrix.loc[user] == 0

    # Keep only those unseen games
    unseen_scores = scores_series[unseen]

    # Step 7: Sort recommendations (highest score = best recommendation)
    sorted_scores = unseen_scores.sort_values(ascending=False)

    # Step 8: Return final recommendations
    return sorted_scores

# Step 4: Test
print(recommend("User2"))
    
    
