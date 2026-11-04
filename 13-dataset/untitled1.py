# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:08:29 2026

@author: Admin
"""

import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create a simple matrix (like an image)
A = np.array([[3, 2, 2],
              [2, 3, -2]])

print("Original Matrix A:\n", A)

# Step 2: Perform SVD
U, S, VT = np.linalg.svd(A, full_matrices=False)
'''
full_matrices=False it produces reduced SVD
full_matrices=True  it produces Full SVD

'''
print("\nU Matrix:\n", U)
print("\nSingular Values (Σ):\n", S)
print("\nV Transpose:\n", VT)

#step 3: reconstruct A
Sigma = np.diag(S)
A_reconstructed = U @ Sigma @ VT
print("\nReconstructed Matrix A:\n", A_reconstructed)

#step 4: show effect of removing a singular value
'''
Why do we remove smaller singular values in SVD?
Think of SVD like separating an image (or matrix) into layers:
Big singular values → contain main patterns / important information
Small singular values → contain noise / less important details
So, when we remove the smaller singular values, we are:
 Removing noise
 Keeping only the strongest patterns
 Compressing the data
 Reducing dimensions

'''
Sigma_reduced = np.diag([S[0], 0])


'''
After SVD:U, S, VT = np.linalg.svd(A)
S is a 1-D array of singular values, for example:
    S = [5.0, 3.0]
S[0] = 5.0 → biggest singular value
S[1] = 3.0 → smaller singular value
What does np.diag([S[0], 0]) do?
[ S[0]     0   ]
[   0      0   ]
So if
S[0] = 5.0,
Sigma_reduced =
[[5.0, 0],
 [0,   0]]
3. Why do we do this?
Because we want to:
 Keep only the first (strongest) singular value
 Remove the second (weaker) singular value
This is how dimensionality reduction works in SVD.
'''

A_approx = U @ Sigma_reduced @ VT


#Step 5: Visualization
fig, axs = plt.subplots(1, 3, figsize=(12, 4))


'''
axs is a NumPy array of Axes objects — one for each subplot you create.

Here, plt.subplots(1, 3, ...) creates 1 row and 3 columns of plots.

That means:

axs[0] → first subplot (left)

axs[1] → second subplot (middle)

axs[2] → third subplot (right)

'''

axs[0].imshow(A, cmap='viridis')
# Show the original matrix A as a colored heatmap
axs[0].set_title("Original A")
# Set title for first subplot
axs[1].imshow(A_reconstructed, cmap='viridis')
# Show the reconstructed matrix from full SVD
axs[1].set_title("Reconstructed A")
# Set title for second subplot
axs[2].imshow(A_approx, cmap='viridis')
# Show the approximate matrix after removing smallest singular value
axs[2].set_title("After Removing Smallest sigma")
# Set title for third subplot
for ax in axs:
    ax.axis('off')
    # Hide axis ticks and labels
plt.show()











