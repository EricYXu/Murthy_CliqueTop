""" Conducts principal component analysis on the olfactory data points """

# Package imports
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd

# Loading data
strawberry_odor_df = pd.read_csv('../../fruit_data/revised_strawberry_dataset.csv')
strawberry_odor_df.drop('Strawberry Type/Chemical Label (Each entry is the volatility of the sample in ng / gFW hr)', axis=1, inplace=True)
X = strawberry_odor_df.to_numpy().T

# Centering and scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA 
pca = PCA(n_components=5)  # Specify the number of components
pca.fit(X_scaled)

# Transform the data
X_pca = pca.transform(X_scaled)

# Analyze the data
explained_variance = pca.explained_variance_ratio_
print(explained_variance)
