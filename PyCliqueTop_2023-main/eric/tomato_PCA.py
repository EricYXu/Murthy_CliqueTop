""" Conducts principal component analysis on the olfactory data points """

# Package imports
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Loading data
tomato_odor_df = pd.read_csv('../../fruit_data/revised_tomato_dataset.csv')
# strawberry_odor_df.drop('Strawberry Type/Chemical Label (Each entry is the volatility of the sample in ng / gFW hr)', axis=1, inplace=True)
X = tomato_odor_df.to_numpy()
    
# Standardize the data (important for PCA)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
    
# Choose the number of components
n_components = min(X_scaled.shape[0], X_scaled.shape[1]) # Maximum possible components

# Apply PCA
pca = PCA(n_components=3)
pca.fit(X_scaled)
    
#Transform data to the new PCA space
X_pca = pca.transform(X_scaled)
    
# Create a new DataFrame with the PCA results
print(pca.explained_variance_ratio_)
pca_df = pd.DataFrame(data=X_pca)
pca_df.columns = ["PC1", "PC2", "PC3"]

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the points
ax.scatter(pca_df['PC1'], pca_df['PC2'], pca_df['PC3'])

# Set labels for axes
ax.set_xlabel('Principal Component 1')
ax.set_ylabel('Principal Component 2')
ax.set_zlabel('Principal Component 3')
plt.title("PCA with 3 Principal Components on Tomato Data")

plt.show()
