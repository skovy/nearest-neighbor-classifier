from sklearn.neighbors import NearestNeighbors
import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
nbrs = NearestNeighbors(n_neighbors=1, algorithm='auto').fit(X)
distances, indices = nbrs.kneighbors(X)
print(indices)
print(distances)
