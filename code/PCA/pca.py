import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 1. Generate Synthetic 2D Data (correlated/skewed cloud)
np.random.seed(42)
x = np.random.normal(0, 1, 300)
y = 0.5 * x + np.random.normal(0, 0.3, 300)
data = np.vstack((x, y))  # Shape: (2, 300)

# Center the data (mean = 0)
data_centered = data - np.mean(data, axis=1, keepdims=True)

# 2. Compute Covariance Matrix and Eigenvectors
cov_matrix = np.cov(data_centered)
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Sort eigenvectors by eigenvalues in descending order
idx = np.argsort(eigenvalues)[::-1]
eigenvectors = eigenvectors[:, idx]

# 3. Setup Matplotlib Figure
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.axhline(0, color="gray", lw=1, ls="--")
ax.axvline(0, color="gray", lw=1, ls="--")

# Initialize scatter plot and lines for eigenvectors
scat = ax.scatter(data_centered[0], data_centered[1], alpha=0.6, color="purple")
(line_v1,) = ax.plot([], [], color="red", lw=3, label="PC1 (Eigenvector 1)")
(line_v2,) = ax.plot([], [], color="blue", lw=3, label="PC2 (Eigenvector 2)")
ax.legend()
ax.set_title("Rotating Data onto Eigenvector Axes (PCA)")

# Calculate total rotation angle needed to align PC1 with X-axis
target_angle = np.arctan2(eigenvectors[1, 0], eigenvectors[0, 0])
frames = 100


# 4. Animation Function
def update(frame):
    # Gradually rotate back to 0 degrees
    current_angle = target_angle * (1 - frame / frames)

    # Creation of a 2D Rotation Matrix
    c, s = np.cos(current_angle), np.sin(current_angle)
    R = np.array(((c, -s), (s, c)))

    # Rotate the data points
    rotated_data = R.T @ data_centered
    scat.set_offsets(rotated_data.T)

    # Rotate the eigenvector lines dynamically
    v1 = R.T @ (eigenvectors[:, 0] * eigenvalues[0] * 2)
    v2 = R.T @ (eigenvectors[:, 1] * eigenvalues[1] * 2)

    line_v1.set_data([0, v1[0]], [0, v1[1]])
    line_v2.set_data([0, v2[0]], [0, v2[1]])

    return scat, line_v1, line_v2


# 5. Run Animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=40, repeat=False)
plt.show()
