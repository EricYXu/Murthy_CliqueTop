""" Script to randomly sample points from Euclidean geometry and obtain their Betti curves, SAME AS RANDOM_CLIQUE.PY """

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
def sample_euclidean(npoints, ndim):
    """ Returns a matrix containing row vector points from a Euclidean unit cube """
    random_sphere_points = np.random.uniform(0,1,(n_samples,geometry_dim))
    return random_sphere_points

def compute_distance_matrix(point_matrix):
    """ 
    Returns the pairwise distance matrix for an NxD matrix of random Euclidean points according to the Euclidean metric/L2 norm 
    """
    distance_matrix = np.zeros((point_matrix.shape[0], point_matrix.shape[0]))

    # Populate the distance matrix with inter-point distances
    for i in range(point_matrix.shape[0]):
        for j in range(i+1, point_matrix.shape[0]):
            distance_matrix[i,j] = np.linalg.norm(point_matrix[i] - point_matrix[j])
            distance_matrix[j,i] = np.linalg.norm(point_matrix[i] - point_matrix[j])

    return distance_matrix


# def compute_correlation_matrix(point_matrix):
#     """ Test script """
#     correlation_matrix = np.zeros((point_matrix.shape[0], point_matrix.shape[0]))

#     # Populate the distance matrix with inter-point distances
#     for i in range(point_matrix.shape[0]):
#         for j in range(i+1, point_matrix.shape[0]):
#             correlation_matrix[i,j] = np.corrcoef(point_matrix[i],point_matrix[j])[0,1]
#             correlation_matrix[j,i] = np.corrcoef(point_matrix[i],point_matrix[j])[0,1]

#     return correlation_matrix


# Generate random 100 points on an ndim-dimensional unit cube, and then compute the distances between points to put into matrix form
n_samples = 100
geometry_dim = 3
random_euclidean_matrix = sample_euclidean(n_samples,geometry_dim)
euclidean_distance_matrix = compute_distance_matrix(random_euclidean_matrix)
[betti_curves, edge_densities] = compute_betti_curves(euclidean_distance_matrix, similarity=False)

# Plots the Betti curves
fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (12,7))
colors = ['black','orange','red','blue']
ax[0].imshow(euclidean_distance_matrix, cmap='jet')
ax[1] = plot_betti_curves(ax[1], betti_curves, edge_densities, colors, title_string = 'euclidean distances')

# Shows the matrix and Betti curves 
plt.suptitle('euclidean_distance_clique.py: compute_betti_curves() with Ndim=' + str(geometry_dim) + ' and ' + str(n_samples) + ' samples')
plt.show()