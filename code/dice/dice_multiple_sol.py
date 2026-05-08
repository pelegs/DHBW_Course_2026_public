import numpy as np
import matplotlib.pyplot as plt
import argparse


# Parsing arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    "-d",
    "--num-dice",
    type=int,
    default=5,
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
    "-r",
    "--num-reps",
    type=int,
    default=10,
    help="Number of repetitions of dice rolls",
)
args = parser.parse_args()

# Actual "simulation"
results = np.random.randint(
    low=1, high=args.num_sides + 1, size=(args.num_reps, args.num_dice)
)
sums = np.sum(results, axis=1)

# Setting up histogram
bins = np.arange(np.min(sums) - 1, np.max(sums) + 2)
histogram, _ = np.histogram(sums, bins)

# Plotting results
fig, ax = plt.subplots()
ax.set_title("Rolling the dice", size=25)
ax.set_xlabel("Value", size=20)
ax.set_ylabel("Repetitions", size=20)
ax.tick_params(axis="both", which="major", labelsize=15)
ax.set_xlim(bins[0], bins[-1])
ax.bar(bins[:-1], histogram, width=0.5, edgecolor="black")
plt.show()
