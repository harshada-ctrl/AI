# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 19:03:37 2026

@author: Admin
"""

# Import Pandas to load, clean, and manipulate tabular data
import pandas as pd

# Import CountVectorizer to convert text categories into numerical vectors
from sklearn.feature_extraction.text import CountVectorizer

# Import cosine_similarity to calculate similarity between items
from sklearn.metrics.pairwise import cosine_similarity

# STEP 1: LOAD THE DATASET

# Read the entertainment dataset from the CSV file
data = pd.read_csv('C:/15-Recmendation_system/Entertainment.csv')

# Display the first five records to understand the dataset
print("First five records:")
print(data.head())


# Display column names and data types
print("\nDataset information:")
print(data.info())

# STEP 2: HANDLE MISSING CATEGORY VALUES

# Replace missing Category values with empty strings

# This prevents errors during text processing
data['Category'] = data['Category'].fillna('')

# Convert all category values to strings
# This ensures that the text-processing function receives strings
data['Category'] = data['Category'].astype(str)

# STEP 3: CONVERT CATEGORIES INTO NUMERICAL VECTORS

# Create a CountVectorizer object
# Each distinct category becomes a separate numerical feature
# For example: Action, Comedy, Drama, Romance
vectorizer = CountVectorizer(
    tokenizer=lambda x: x.split(','),  # Split categories at commas
    token_pattern=None,                # Disable the default token pattern
    lowercase=True                     # Convert categories to lowercase
)

# Learn the category vocabulary and convert each item into a vector
# Each row represents one entertainment item
# Each column represents a category
category_matrix = vectorizer.fit_transform(data['Category'])

# Display the names of the category features
print("\nCategory features:")
print(vectorizer.get_feature_names_out())

# Display the shape of the resulting matrix
# Rows = number of items; columns = number of unique categories
print("\nCategory matrix shape:", category_matrix.shape)

# STEP 4: CALCULATE ITEM-TO-ITEM SIMILARITY

# Compare every item with every other item using cosine similarity
# Similar categories generally produce higher similarity scores
item_similarity = cosine_similarity(category_matrix)

# Display the similarity matrix dimensions
print("\nSimilarity matrix shape:", item_similarity.shape)

# STEP 5: CREATE A SIMILARITY DATAFRAME

# Use item titles as row and column labels
# This makes it easy to find similarity scores by title
item_similarity_df = pd.DataFrame(
    item_similarity,
    index=data['Titles'],
    columns=data['Titles']  # Note: cut off at bottom of image; standard completion
)

# Display the similarity scores for the first five items
print("\nItem similarity matrix:")
print(item_similarity_df.iloc[:5, :5])

# STEP 6: DEFINE THE RECOMMENDATION FUNCTION

def recommend_items(item_name, num_recommendations=5):
    # Check whether the requested item exists in the dataset
    if item_name not in item_similarity_df.index:
        print("Item not found in dataset.")
        return None

    # Retrieve similarity scores between the selected item
    # and all other items
    scores = item_similarity_df[item_name]

    # Remove the selected item itself because it should not
    # be recommended to the user
    scores = scores.drop(item_name)

    # Sort items from highest similarity to lowest similarity
    scores = scores.sort_values(ascending=False)

    # Select only the requested number of recommendations
    recommendations = scores.head(num_recommendations)
    
    # Create a readable DataFrame containing item names and scores
result = pd.DataFrame({
    'Recommended Item': recommendations.index,
    'Similarity Score': recommendations.values
})

#return the recommendation as a clean table
return result.reset_index(drop=True)


# STEP 7: TEST THE RECOMMENDATION SYSTEM[cite: 13]

# Specify the title of the item for which recommendations are required[cite: 13]
# Replace this example with an exact title from your dataset[cite: 13]
item_name = data['Titles'].iloc[0]

# Generate the top five similar-item recommendations[cite: 13]
recommended_items = recommend_items(
    item_name,
    num_recommendations=5
)

# Display the selected item and its recommendations
print("\nSelected item:", item_name)
print("\nRecommended items:")
print(recommended_items)



























