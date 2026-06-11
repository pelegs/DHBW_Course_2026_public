import numpy as np

with open("iris_data.csv", "r") as f:
    variables = f.readline().split(",")[:-1]

data = np.loadtxt("iris_data.csv", delimiter=",", skiprows=1)
plant_species = data[:, -1]
data = data[:, :-1]

X = data
B = (X - np.mean(X, axis=0)) / np.std(X, axis=0)

U, S, VT = np.linalg.svd(B, full_matrices=False)
print(U.shape, S.shape, VT.shape)
