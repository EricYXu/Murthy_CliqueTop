""" Script to randomly sample points from Euclidean geometry and obtain their Betti curves """

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
def sample_spherical(npoints, ndim):
    """ Returns a matrix containing row vector points from a Euclidean unit ball """
    random_sphere_points = np.random.randn(npoints, ndim)
    for i in range(len(random_sphere_points)):
        random_sphere_points[i] = random_sphere_points[i] / np.linalg.norm(random_sphere_points[i])
    return random_sphere_points

# Generate random 100 points on a unit ball
n_samples = 100
geometry_dim = 10
random_ball_matrix = sample_spherical(n_samples,geometry_dim)
cov_matrix = np.corrcoef(random_ball_matrix)
[betti_curves, edge_densities] = compute_betti_curves(cov_matrix)

# Plots the Betti curves
fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (12,7))
colors = ['black','orange','red','blue']
ax[0].imshow(cov_matrix, cmap='jet')
ax[1] = plot_betti_curves(ax[1], betti_curves, edge_densities, colors, title_string = 'correlations')

# Shows the matrix and Betti curves 
plt.suptitle('euclidean.py: compute_betti_curves() with Ndim=' + str(geometry_dim) + ' and ' + str(n_samples) + ' samples')
plt.show()