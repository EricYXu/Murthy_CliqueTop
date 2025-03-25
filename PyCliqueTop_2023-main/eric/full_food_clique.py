""" Script that displays the Betti curves for dataset from Venkatesh Murthy lab """

# Package imports and scripts from current working directory
import sys
import pandas as pd
import numpy as np
import scipy
import scipy.io
import matplotlib.pyplot as plt 
from load_concentration_data import get_concentration_matrix

# Appending file path to import clique-top specific libraries (or use '~' for home directory)
sys.path.append('/Users/ericxu/Documents/Github/Murthy_CliqueTop/PyCliqueTop_2023-main') 

# Other script imports
from compute_betti_curves import compute_betti_curves
from plot_betti_curves import plot_betti_curves

# Imports the full food dataset with load_concentration_data script; place into a two-dimension np_array with shape (1384, 8729), with individual entries corresponding to the concentration of that chemical in that food
pre_concentration_matrix = get_concentration_matrix()
concentration_matrix = np.zeros((pre_concentration_matrix.shape[0], pre_concentration_matrix.shape[1]))
for i in range(concentration_matrix.shape[0]):
    for j in range(concentration_matrix.shape[1]):
        concentration_matrix[i,j] = pre_concentration_matrix[i,j,0]

# Attributes
geometry_dim = 8729 # im not sure what this value would be? is it equal to the number of chemical components/dimension of correlation matrix
n_samples = 1384

# Computes the correlation matrix between the various chemical compounds --> i think this means our correlation matrix would have shape (8729, 8729)
# TODO: Find out how to deal with foods that are missing concentration data 
food_correlation_matrix = np.corrcoef(concentration_matrix)
[betti_curves, edge_densities] = compute_betti_curves(food_correlation_matrix, similarity=True)

# Plots the Betti curves
fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (12,7))
colors = ['black','orange','red','blue']
ax[0].imshow(food_correlation_matrix, cmap='jet')
ax[1] = plot_betti_curves(ax[1], betti_curves, edge_densities, colors, title_string = 'euclidean correlations')

# Shows the matrix and Betti curves 
plt.suptitle('full_food_clique.py: compute_betti_curves() with Ndim=' + str(geometry_dim) + ' and ' + str(n_samples) + ' samples')
plt.show()




