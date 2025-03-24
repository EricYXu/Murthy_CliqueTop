""" Script that displays the Betti curves for dataset from Venkatesh Murthy lab """

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

# Imports the full food dataset

