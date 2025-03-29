""" Script to randomly sample points from Hyperbolic geometry and obtain their Betti curves """

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
def hyperbolic_density(Rmin, Rmax, r):
    """
    Returns the probability density of sampling a random radius on a hyperbolic ball
    """
    pass


def sample_hyperbolic(ndim, Rmax):
    """ Generate random points on an ndim-dimensional hyperbolic ball """
    sample_point = np.zeros((ndim,))

    # Pick a random radii from 0.9Rmax to Rmax = 7 using UoU
    uniform = np.random.uniform(0,1)
    random_radii = 0

    # Pick a uniform random angle
    angle = np.random.uniform(0,360)


def compute_distance(p1, p2):
    """ Compute the distance between points according to hyperbolic geometry """
    # TODO: Figure out how to compute the distance between two points in hyperbolic geometry

    pass


# Generate random 100 points on an ndim-dimensional hyperbolic ball
n_samples = 100
geometry_dim = 5
random_ball_matrix = sample_hyperbolic(n_samples,geometry_dim)
cov_matrix = np.corrcoef(random_ball_matrix)
[betti_curves, edge_densities] = compute_betti_curves(cov_matrix, similarity=False)

# Plots the Betti curves
fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (12,7))
colors = ['black','orange','red','blue']
ax[0].imshow(cov_matrix, cmap='jet')
ax[1] = plot_betti_curves(ax[1], betti_curves, edge_densities, colors, title_string = 'hyperbolic distances')

# Shows the matrix and Betti curves 
plt.suptitle('hyperbolic_clique.py: compute_betti_curves() with Ndim=' + str(geometry_dim) + ' and ' + str(n_samples) + ' samples')
plt.show()
