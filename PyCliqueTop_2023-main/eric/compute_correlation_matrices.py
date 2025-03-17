import pandas as pd
import numpy as np
import math

# Computes the correlation matrices for a given CSV file of concentrations

def get_mean_concentrations(odor_csv_filename):
    """ Returns the average concentrations of each chemical component in a 1-dimensional array """

    # Loads the files
    odor_csv_filename = str(odor_csv_filename)
    odor_df = pd.read_csv(odor_csv_filename)
    component_averages = []

    # Iteratively computes averages
    num_samples = odor_df.shape[0]
    for i in range(1,len(odor_df.columns)-1):
        component_averages.append(odor_df.iloc[:,i].sum() / float(num_samples))

    return component_averages


def get_correlation_matrices(odor_csv_filename, component_means):
    """ Returns the 2-dimensional correlation matrix from a CSV containing the concentrations of different chemical components """
    """ Note that the odor indices start at 1 and go until 82"""

    # Loads the files
    odor_csv_filename = str(odor_csv_filename)
    odor_df = pd.read_csv(odor_csv_filename)
    num_samples = odor_df.shape[0]
    num_odors = odor_df.shape[1]-1

   # Initializes correlation variables and correlation matrix using NumPy
    correlation_matrix = np.zeros((num_odors, num_odors))

    # Iterate through every odor pair
    for odor1 in range(1,num_odors-1):
        for odor2 in range(odor1+1,num_odors):
            corr_num = 0
            corr_denom = 0

            # Compute the odor pair correlation numerator
            for i in range(1,num_samples):
                corr_num += (odor_df.iloc[i,odor1] - component_means[odor1 - 1]) * (odor_df.iloc[i,odor2]  - component_means[odor2 - 1])

            # Compute the odor pair correlation denominator
            odor1_squared_error = 0
            odor2_squared_error = 0

            for i in range(1,num_samples):
                odor1_squared_error += pow(odor_df.iloc[i,odor1] - component_means[odor1-1],2)
                odor2_squared_error += pow(odor_df.iloc[i,odor2] - component_means[odor2-1],2)

            corr_denom = math.sqrt(odor1_squared_error) * math.sqrt(odor2_squared_error)
            
            # Place value in correlation matrix
            correlation_matrix[odor1,odor2] = float(corr_num) / corr_denom
            correlation_matrix[odor2,odor1] = float(corr_num) / corr_denom

    return correlation_matrix

# Function that centers and scales a matrix
def center_and_scale(s):
    s = s - np.reshape(np.mean(s, axis=1), (s.shape[0], 1))
    s = s / np.reshape(np.var(s, axis=1), (s.shape[0], 1))
    return s

def get_covariance_matrix(odor_csv_filename):
    """ Returns the 2-dimensional covariance matrix from a CSV """

    # Loads the files
    odor_csv_filename = str(odor_csv_filename)
    odor_df = pd.read_csv(odor_csv_filename)

    # Remove the first column to avoid having strings and numbers
    odor_df.drop('Strawberry Type/Chemical Label (Each entry is the volatility of the sample in ng / gFW hr)', axis=1, inplace=True)
    
    # Computes scaled and centered covariance matrix
    odor_array = odor_df.to_numpy().T
    odor_covmatrix = np.cov(center_and_scale(odor_array))

    # Taking the log and absolute value of the matrix
    adjusted_covmatrix = np.log(np.abs(odor_covmatrix))

    return adjusted_covmatrix
