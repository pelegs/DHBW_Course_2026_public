import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm

# Load and separate data
with open("iris_data.csv", "r") as csv_file:
    var_labels = csv_file.readline().split(",")[:-1]
data = np.genfromtxt("iris_data.csv", delimiter=",", skip_header=1)
species = data[:, -1]
data = data[:, :-1]
num_samples = data.shape[0]
num_components = data.shape[1]

# Normalize data
B = (data - np.mean(data, axis=0)) / np.std(data, axis=0)

# SVD
U, S, VT = np.linalg.svd(B, full_matrices=False)

# Plot statistics
components = np.arange(1, num_components + 1)
variance = S**2 / num_samples
variance /= np.sum(variance)
csum = np.cumsum(variance)

# First plot (PCs significance)
fig, ax = plt.subplots(1, 2)

ax[0].set_title("Singular values", size=25)
ax[0].set_xlabel("Component", size=20)
ax[0].set_ylabel("Statistical significance (variance)", size=20)
ax[0].set_xticks(components)
bars = ax[0].bar(components, variance)
ax[0].bar_label(
    bars, labels=[f"{var:0.2f}" for var in variance], color="black", fontsize=14
)

ax[1].set_title("Cumulative statistical value", size=25)
ax[1].set_xlabel("Component", size=20)
ax[1].set_ylabel("Cumulative value", size=20)
ax[1].set_xticks(components)
ax[1].plot(components, csum, "-", color="orange")
ax[1].plot(components, csum, ".", color="red")
for i, v in enumerate(csum, start=1):
    ax[1].annotate(
        f"{v:0.2f}", xy=(i, v), xytext=(0, 10), textcoords="offset points", color="red"
    )

plt.show()

# More PCA stuff (only PC1 and PC2)
projections = U[:, :2] @ np.diag(S[:2])
V = VT.T
loadings = (V * S / np.sqrt(num_samples - 1))[:, :2]
load_vecs = np.c_[np.zeros(shape=(4, 2)), loadings]

# Color test
colors = ["red", "green", "blue"]
cmap = ListedColormap(colors)
bounds = [-0.1, 0.9, 1.9, 2.9]
norm = BoundaryNorm(bounds, cmap.N)

# Second plot (scatter + biplot)
fig, ax = plt.subplots()
ax.set_title("PCA, Iris data")
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
scatter = ax.scatter(
    projections[:, 0], projections[:, 1], c=species, cmap=cmap, norm=norm
)
biplot = ax.quiver(
    load_vecs[:, 0],
    load_vecs[:, 1],
    load_vecs[:, 2],
    load_vecs[:, 3],
    angles="xy",
    scale_units="xy",
    scale=0.5,
    color=["purple", "orange", "black", "grey"],
    width=0.005,
)
# ax.quiverkey(biplot, X=2.5, Y=2.5, U=0.05, label="Quiver key")

plt.show()
