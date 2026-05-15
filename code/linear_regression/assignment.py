import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["text.usetex"] = True


# Generate data
# (y = ax + b)
a = 2.5
b = -1.5
xmin, xmax = 0.5, 10
num_data_pts = 150
xs = np.linspace(xmin, xmax, num_data_pts)
ys_real = a * xs + b

# Add noise
noise_std = 0.75
noise = np.random.normal(0, noise_std, size=(num_data_pts))
ys_noisy = ys_real + noise

# Linear regression (least squares)
# TODO: implement!

# R^2 calc
# TODO: we'll discuss this

# Plot
# TODO: implement!
