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

def sample_euclidean(npoints, ndim):
    """ Returns a matrix containing row vector points from a Euclidean unit cube """
    random_sphere_points = np.random.uniform(0,1,(n_samples,geometry_dim))
    return random_sphere_points

# Draws 100 observations of 'geometry_dim' independent uniformly-distributed random variables; creates pairwise correlation matrix --> same as sampling from n-dimensional unit cube
n_samples = 100
geometry_dim = 5
random_euclidean_matrix = sample_euclidean(n_samples,geometry_dim)
cov_matrix = np.corrcoef(random_euclidean_matrix) # Uses correlation matrix
[betti_curves, edge_densities] = compute_betti_curves(cov_matrix, similarity=True)

# Plots the Betti curves
fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (12,7))
colors = ['black','orange','red','blue']
ax[0].imshow(cov_matrix, cmap='jet')
ax[1] = plot_betti_curves(ax[1], betti_curves, edge_densities, colors, title_string = 'euclidean correlations')

# Shows the matrix and Betti curves 
plt.suptitle('euclidean_correlation_clique.py: compute_betti_curves() with Ndim=' + str(geometry_dim) + ' and ' + str(n_samples) + ' samples')
plt.show()

