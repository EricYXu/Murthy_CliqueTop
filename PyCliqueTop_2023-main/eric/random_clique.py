# Package imports
import numpy as np
import scipy
import scipy.io
import matplotlib.pyplot as plt 

# Other script imports
from compute_betti_curves import compute_betti_curves
from plot_betti_curves import plot_betti_curves
from compute_correlation_matrices import get_mean_concentrations,get_correlation_matrices,get_covariance_matrix



# Draws from 88 independent uniformly distributed random variables and then computing the pairwise correlations
uniform_vector = np.random.uniform(0,1,(1,88))

print(uniform_vector)

