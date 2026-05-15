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
noise_std = 7.5
noise = np.random.normal(0, noise_std, size=(num_data_pts))
ys_noisy = ys_real + noise

# Linear regression (least squares)
A = np.vstack((xs, np.ones(num_data_pts))).T
LHS = np.dot(A.T, A)
RHS = np.dot(A.T, ys_noisy)
a_approx, b_approx = np.linalg.solve(LHS, RHS)
ys_linear_fit = a_approx * xs + b_approx

# R^2 calc
SS_res = np.sum((ys_noisy - ys_linear_fit) ** 2)
SS_tot = np.sum((ys_noisy - np.mean(ys_noisy)) ** 2)
R_sqr = 1 - SS_res / SS_tot

# Plot
fig, ax = plt.subplots()
ax.set_title("Real vs. noisy data", size=40)
ax.set_xlabel("$x$", size=30)
ax.set_ylabel("$y$", rotation=0, size=30)
ax.tick_params(axis="both", which="major", labelsize=25)
ax.plot(xs, ys_noisy, ".", color="blue")
ax.plot(xs, ys_linear_fit, color="red")
ax.text(0.05, 0.95, rf"Slope = ${a_approx:0.2f}$", size=30, transform=ax.transAxes)
ax.text(0.05, 0.90, rf"Intercept = ${b_approx:0.2f}$", size=30, transform=ax.transAxes)
ax.text(0.05, 0.85, rf"$R^{{{2}}}={R_sqr:0.2f}$", size=30, transform=ax.transAxes)
plt.get_current_fig_manager().set_window_title("Least squares fit (linear model)")
plt.show()
