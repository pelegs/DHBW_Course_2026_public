import numpy as np
import matplotlib.pyplot as plt
import argparse


# Parsing arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    "-d",
    "--num-dice",
    type=int,
    default=60,
    help="Number of dice to be rolled",
)
parser.add_argument(
    "-s",
    "--num-sides",
    type=int,
    default=6,
    help="Number of sides per di(c)e",
)
parser.add_argument(
    "-b",
    "--num-bins",
    type=int,
    default=6,
    help="Number of bins for historgram",
)
args = parser.parse_args()

# Actual "simulation"
results = np.random.randint(low=1, high=args.num_sides + 1, size=(args.num_dice))

# Setting up histogram
bins = np.arange(1, args.num_bins + 2)
histogram, _ = np.histogram(results, bins)

# Some basic statistics
# First manually, so that you see some numpy properties
# Then we also compare to the native numpy functions
mean = np.sum(results) / args.num_dice
devs = (results - mean) ** 2
std = np.sqrt(np.sum(devs) / args.num_dice)
print(f"mean: manual = {mean:0.2f}, np = {np.mean(results):0.2f}")
print(f"std: manual = {std:0.2f}, np = {np.std(results):0.2f}")

# Plotting results
fig, ax = plt.subplots()
ax.set_title("Rolling the dice", size=25)
ax.set_xlabel("Value", size=20)
ax.set_ylabel("Repetitions", size=20)
ax.tick_params(axis="both", which="major", labelsize=15)
ax.set_xlim(0, args.num_bins + 1)
ax.bar(bins[:-1], histogram, width=0.5, edgecolor="black")
plt.show()
