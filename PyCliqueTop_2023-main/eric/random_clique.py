# Package imports
import sys
import numpy as np
import scipy
import scipy.io
import matplotlib.pyplot as plt 

# Appending file path to import clique-top specific libraries
sys.path.append('/Users/ericxu/Documents/Github/Murthy_CliqueTop/PyCliqueTop_2023-main')  

# Other script imports
from compute_betti_curves import compute_betti_curves
from plot_betti_curves import plot_betti_curves

# HELPER FUNCTIONS
def center_and_scale(s):
    """
    Centering and scaling the matrix function
    """
    s = s - np.reshape(np.mean(s, axis=1), (s.shape[0], 1))
    s = s / np.reshape(np.var(s, axis=1), (s.shape[0], 1))
    return s

# Draws 10000 observations of 88 independent uniformly-distributed random variables; creates pairwise correlation matrix
random_unif_matrix = np.random.uniform(0,1,(100,88))
cov_matrix = np.cov(random_unif_matrix)
[betti_curves, edge_densities] = compute_betti_curves(cov_matrix)

# Plots the Betti curves
fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (12,7))
colors = ['black','orange','red','blue']
ax[0].imshow(cov_matrix, cmap='jet')
ax[1] = plot_betti_curves(ax[1], betti_curves, edge_densities, colors, title_string = 'correlations')

# Shows the matrix and Betti curves 
plt.suptitle('random.py: compute_betti_curves() with N=88 and 10000 samples')
plt.show()

