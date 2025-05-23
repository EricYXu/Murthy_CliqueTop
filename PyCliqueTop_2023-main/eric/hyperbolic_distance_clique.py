""" Script to randomly sample points from Hyperbolic geometry and obtain their Betti curves """

# Package imports 
import sys
import numpy as np
import matplotlib.pyplot as plt

# Appending file path to import clique-top specific libraries
sys.path.append('/Users/ericxu/Documents/Github/Murthy_CliqueTop/PyCliqueTop_2023-main')  

# Script imports
from compute_betti_curves import compute_betti_curves
from plot_betti_curves import plot_betti_curves

# Returns the non-normalized hyperbolic cumulative density function found in Sharpee paper
def nonnormalized_hyperbolic_cdf(r, ndim):
    return np.cosh(((ndim-1) * r))

# Returns the normalized hyperbolic cumulative density function found in the Sharpee paper
def normalized_hyperbolic_cdf(r, ndim, Rmin, Rmax):
    numerator = ((1/(ndim-1)) * np.cosh(((ndim-1) * r)) - ((1/(ndim-1)) * np.cosh(np.radians((ndim-1) * Rmin))))
    denominator = ((1/(ndim-1)) * np.cosh(((ndim-1) * Rmax)) - ((1/(ndim-1)) * np.cosh(np.radians((ndim-1) * Rmin))))
    return numerator / denominator

# Samples hyperbolic angles and radii from the probability density function from the Sharpee paper
def sample_hyperbolic_points(n_samples, ndim, Rmin, Rmax):
    uniform_points = np.random.uniform(0,1,n_samples)
    hyperbolic_angles = np.random.uniform(0,360,n_samples)
    hyperbolic_radii = []

    # Plug each of these into the normalized inverse cdf of the hyperbolic sine
    for point in uniform_points:
        hyperbolic_radii_sample = (1/(ndim-1)) * np.arccosh(nonnormalized_hyperbolic_cdf(Rmin, ndim) + point * (nonnormalized_hyperbolic_cdf(Rmax, ndim) - nonnormalized_hyperbolic_cdf(Rmin, ndim)))
        hyperbolic_radii.append(hyperbolic_radii_sample)

    return hyperbolic_angles, np.array(hyperbolic_radii)

# Converts from polar coordinates to Cartesian coordinates
def polar_to_cartesian(angles, radii):
    # Store x-coordinates and y-coordinates in two arrays
    num_points = len(angles)
    x_coords = []
    y_coords = []
    for i in range(num_points):
        x_coords.append(radii[i] * np.cos(np.radians(angles[i])))
        y_coords.append(radii[i] * np.sin(np.radians(angles[i])))

    return x_coords, y_coords

# Computes hyperbolic distance metric between two points
def hyperbolic_distance(x1, x2, y1, y2):
    # Calculate the hyperbolic functions
    cosh_y1 = np.cosh(y1)
    cosh_y2 = np.cosh(y2)
    cosh_x_diff = np.cosh(x2 - x1)
    sinh_y1 = np.sinh(y1)
    sinh_y2 = np.sinh(y2)
    
    # Calculate the argument for arcosh
    arg = cosh_y1 * cosh_x_diff * cosh_y2 - sinh_y1 * sinh_y2
    
    # Return the distance
    return np.arccosh(arg)

# Computes a distance matrix from a point matrix
def get_distance_matrix(x_coords, y_coords):
    distance_matrix = np.zeros((len(x_coords), len(x_coords)))

    # Populate the distance matrix with inter-point distances
    for i in range(distance_matrix.shape[0]):
        for j in range(i+1, distance_matrix.shape[0]):
            distance_matrix[i,j] = hyperbolic_distance(x_coords[i], x_coords[j], y_coords[i], y_coords[j])
            distance_matrix[j,i] = hyperbolic_distance(x_coords[i], x_coords[j], y_coords[i], y_coords[j])

    return distance_matrix

# Generate random 1000 points on an ndim-dimensional hyperbolic ball and compute Betti curves
n_samples = 100
geometry_dim = 10
Rmax = 7
Rmin = 0.9 * Rmax

hyperbolic_angles, hyperbolic_radii = sample_hyperbolic_points(n_samples,geometry_dim, Rmin, Rmax)
x, y = polar_to_cartesian(hyperbolic_angles, hyperbolic_radii)


# TEST 1: Making a scatter plot of the hyperbolic-sampled points
# plt.scatter(x,y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Hyperbolic Sampled Points with Ndim=' + str(geometry_dim) + ' and Rmax=' + str(Rmax))
# plt.show()


# TEST 2: Getting Betti curves
random_hyperbolic_dist_matrix = get_distance_matrix(x, y)
[betti_curves, edge_densities] = compute_betti_curves(random_hyperbolic_dist_matrix, similarity=False)

# Plots the Betti curves
fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (12,7))
colors = ['black','orange','red','blue']
ax[0].imshow(random_hyperbolic_dist_matrix, cmap='jet')
ax[1] = plot_betti_curves(ax[1], betti_curves, edge_densities, colors, title_string = 'hyperbolic distances')

# Shows the matrix and Betti curves 
plt.suptitle('hyperbolic_clique.py: compute_betti_curves() with Ndim=' + str(geometry_dim) + ' and ' + str(n_samples) + ' samples')
plt.show()
