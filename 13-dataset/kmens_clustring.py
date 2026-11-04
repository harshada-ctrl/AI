# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 18:53:37 2026

@author: Admin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load University dataset
Univ1 = pd.read_excel("C:/13-dataset/University_Clustering.xlsx")

# Drop non-numeric column
Univ = Univ1.drop(['State'], axis=1)


# Apply Standardization
scaler = StandardScaler()
df_std = pd.DataFrame(scaler.fit_transform(Univ.iloc[:, 1:]),
                      columns=Univ.columns[1:])


# Finding optimal K using Elbow Method (with Standardized data)
TWSS = []
k_range = list(range(2, 8))

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(df_std)
    TWSS.append(kmeans.inertia_)

# Plot Elbow Curve
plt.plot(k_range, TWSS, 'ro-')
plt.xlabel("Number of Clusters")
plt.ylabel("Total Within Sum of Squares (TWSS)")
plt.title("Elbow Curve to Determine Optimal K")
plt.show()

# Apply KMeans with optimal clusters (e.g., K=3)
model = KMeans(n_clusters=3, random_state=42)
model.fit(df_std)


# Add cluster labels to the original dataset
Univ['Cluster'] = model.labels_

# Rearranging columns to bring Cluster first
Univ = Univ[['Cluster'] + list(Univ.columns[:-1])]
#now check the Univ1 dataframe
Univ.iloc[:, 2:].groupby(Univ.Cluster).mean()


"""
Cluster 0
Feature Value    Interpretation
SAT 1360         High SAT scores - academically strong students.
Top10 87.5%      Most students are top performers in high school.
Accept 34.5%     Selective college (Low acceptance rate).
SFRatio 6.5      Very low student-faculty ratio - more personalized attention.
Expenses $61,133 Very high expenses - likely elite, private colleges.
GradRate 84%     High graduation rate.

Summary: This cluster represents elite, expensive, and selective institutions, like...

Cluster 1
Feature Value    Interpretation
SAT 1114         Lower SAT scores.
Top10 47%        Fewer top-performing high school students.
Accept 67.8%     High acceptance rate - less selective.
SFRatio 17.0     High student-faculty ratio - large class sizes.
Expenses $13,385 Low cost - probably public or community colleges.
GradRate 74%     Moderate graduation rate.

Cluster 2
    Feature Value Interpretation
    SAT 1309 High SAT scores - strong academics.
    Top10 85.6% High percentage of top-performing students.
    Accept 29.6% Very selective.
    SFRatio 11.94 Moderate class sizes.
    Expenses $28,360 Mid-range cost.
    GradRate 91.5% Very high graduation rate.

    Summary: This cluster represents prestigious but more affordable schools - possibly
"""

# ===== Clustering Performance Metrics =====
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score

labels = model.labels_
silhouette = silhouette_score(df_std, labels)
silhouette
#0.42

'''
Silhouette Score = 0.42
Range: -1 to +1

Meaning: Measures how similar points are to their own cluster vs. other clusters.

Interpretation:

0.7 - 1.0: Strong, well-separated clusters

0.5 - 0.7: Reasonable separation

0.25 - 0.5: Weak to moderate separation
Your case (0.42):
    
    Moderate quality - clusters are somewhat distinct but still have overlap.
    
    This is acceptable, but not very strong - maybe some cluster boundaries aren't
'''



db_index = davies_bouldin_score(df_std, labels)
db_index
#0.73
    '''
    Davies-Bouldin Index = 0.73
    Range: 0 -> ∞
    
    Meaning: Lower means better separation and compactness.
    
    Interpretation:
    
    < 1.0: Good separation
    1.0 - 2.0: Acceptable

    > 2.0: Poor separation

    Your case (0.73):

    Very good - clusters are reasonably compact and well-separated.
    '''

ch_index = calinski_harabasz_score(df_std, labels)
ch_index

#22.20
'''
Calinski-Harabasz Index = 22.20
Range: No fixed max, higher is better.

Meaning: Ratio of between-cluster dispersion to within-cluster dispersion.

Interpretation:

Higher values indicate better-defined clusters.

Best used comparatively - check which k gives the highest value.

Your case (22.20):
On its own, not high or Low without a baseline— compare
with other k values to be sure.

Still indicates a fair degree of separation.'''


print("\nClustering Performance Metrics:")
print(f"Silhouette Score : {silhouette:.4f} (range: -1 to +1, higher is better)")
print(f"Davies-Bouldin Index : {db_index:.4f} (lower is better)")
print(f"Calinski-Harabasz Index : {ch_index:.4f} (higher is better)")


































