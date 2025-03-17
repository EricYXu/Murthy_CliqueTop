""" Script that displays the Betti curves for the Zhou 2018 strawberry dataset """

# Package imports
import sys
import pandas as pd
import numpy as np
import scipy
import scipy.io
import matplotlib.pyplot as plt 

# Appending file path to import clique-top specific libraries (or use '~' for home directory)
sys.path.append('/Users/ericxu/Documents/Github/Murthy_CliqueTop/PyCliqueTop_2023-main') 

# Other script imports
from compute_betti_curves import compute_betti_curves
from plot_betti_curves import plot_betti_curves

# Imports the strawberry dataset; Remove the first column to avoid having strings and numbers
strawberry_odor_csv_filename = str('../../fruit_data/revised_strawberry_dataset.csv')
strawberry_odor_df = pd.read_csv(strawberry_odor_csv_filename)
strawberry_odor_df.drop('Strawberry Type/Chemical Label (Each entry is the volatility of the sample in ng / gFW hr)', axis=1, inplace=True)
strawberry_odor_array = strawberry_odor_df.to_numpy().T

# Imports the tomato dataset
tomato_odor_csv_filename = str('../../fruit_data/revised_tomato_dataset.csv')
tomato_odor_df = pd.read_csv(tomato_odor_csv_filename)
tomato_odor_array = tomato_odor_df.to_numpy().T

# Imports the blueberry dataset
blueberry_odor_csv_filename = str('../../fruit_data/revised_blueberry_dataset.csv')
blueberry_odor_df = pd.read_csv(blueberry_odor_csv_filename)
blueberry_odor_array = blueberry_odor_df.to_numpy().T

# I will be temporarily skipping the mouse urine dataset because of ambiguities regarding volatile monomolecular compounds.

# Centering and scaling the matrix function
def center_and_scale(s):
    s = s - np.reshape(np.mean(s, axis=1), (s.shape[0], 1))
    s = s / np.reshape(np.std(s, axis=1), (s.shape[0], 1))
    return s

# Computes covariance matrix; gets covariance matrix and Betti curves --> repeat for strawberry, tomato, and blueberry
# sc = center_and_scale(odor_array) 
# cov_matrix = sc @ sc.T 
strawberry_cov_matrix = np.corrcoef(strawberry_odor_array)
[strawberry_betti_curves, strawberry_edge_densities] = compute_betti_curves(strawberry_cov_matrix)

tomato_cov_matrix = np.corrcoef(tomato_odor_array)
[tomato_betti_curves, tomato_edge_densities] = compute_betti_curves(tomato_cov_matrix)

blueberry_cov_matrix = np.corrcoef(blueberry_odor_array)
[blueberry_betti_curves, blueberry_edge_densities] = compute_betti_curves(blueberry_cov_matrix)

# Plots all the Betti curves
fig, ax = plt.subplots(nrows = 3, ncols = 2, figsize = (12,7))
colors = ['black','orange','red','blue']
ax[0,0].imshow(strawberry_cov_matrix,cmap='jet')
ax[0,1] = plot_betti_curves(ax[0,1], strawberry_betti_curves, strawberry_edge_densities, colors, title_string = 'strawberry correlations')

ax[1,0].imshow(tomato_cov_matrix,cmap='jet')
ax[1,1] = plot_betti_curves(ax[1,1], tomato_betti_curves, tomato_edge_densities, colors, title_string = 'tomato correlations')

ax[2,0].imshow(blueberry_cov_matrix,cmap='jet')
ax[2,1] = plot_betti_curves(ax[2,1], blueberry_betti_curves, blueberry_edge_densities, colors, title_string = 'blueberry correlations')

# Displays matrix and Betti curves
plt.suptitle('fruit_clique.py: compute_betti_curves()')
plt.show()


