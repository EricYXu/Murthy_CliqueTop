# Package imports
import numpy as np
import scipy
import scipy.io
import matplotlib.pyplot as plt 

# Other script imports
from compute_betti_curves import compute_betti_curves
from plot_betti_curves import plot_betti_curves
from compute_correlation_matrices import get_mean_concentrations,get_correlation_matrices,get_covariance_matrix

""" Script that displays the Betti curves for the Zhou 2018 strawberry dataset """

# Computes correlation matrices and Betti curves
# A_dataset_correlations = get_correlation_matrices("../strawberry_data/revised_strawberry_dataset.csv",get_mean_concentrations("../strawberry_data/revised_strawberry_dataset.csv"))
A_dataset_correlations = get_covariance_matrix("../strawberry_data/revised_strawberry_dataset.csv")
[dataset_correlation_bettis, dataset_correlation_edge_densities] = compute_betti_curves(A_dataset_correlations, max_dim = 3, similarity = True)

# Generates the Betti curves for the dataset
geometric_dim = 3
n = 81 
fig, ax = plt.subplots(nrows = 2, ncols = 2, figsize = (12,7))
colors = ['black','orange','red','blue']

# Generates random points in Euclidean geometry and generates correlation matrix
xy_coords = np.random.uniform(size=(n,geometric_dim))
A_euclidean_correlations = np.ones((n,n))
for i in range(n):
    for j in range(i+1,n):
        A_euclidean_correlations[i,j] = A_euclidean_correlations[j,i] = -1*scipy.spatial.distance.cosine(xy_coords[i,:],xy_coords[j,:]) + 1 

# Generates the Betti curves for random Euclidean matrix
[euclidean_correlation_bettis, euclidean_correlation_edge_densities] = compute_betti_curves(A_euclidean_correlations, max_dim = 3, similarity = True)

# Plots all the Betti curves
ax[0,0].imshow(A_dataset_correlations,cmap='jet')
ax[0,1] = plot_betti_curves(ax[0,1], dataset_correlation_bettis, dataset_correlation_edge_densities, colors, title_string = 'correlations')


ax[1,0].imshow(A_euclidean_correlations,cmap='jet')
ax[1,1] = plot_betti_curves(ax[1,1], euclidean_correlation_bettis, euclidean_correlation_edge_densities, colors, title_string = 'correlations')


plt.suptitle('strawberry_clique.py: compute_betti_curves() with n = %d, dim = %d' % (n,geometric_dim))
plt.show()


