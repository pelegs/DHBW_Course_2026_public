import igraph as ig
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import logging

# Create a logging for the results
logging.basicConfig(
    filename="page_rank.log",
    filemode="a",
    format="%(asctime)s,%(msecs)03d %(name)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)

# Load page links probability matrix
PM = np.load("page_rank_matrix.npy").T
num_pages = PM.shape[0]
logging.info("------------------------------------------------")
logging.info("Probability Matrix PM_ij of jumping from page j to page i:\n")
with np.printoptions(precision=3):
    logging.info(PM)

v = np.ones(shape=num_pages)
eval_next = v.T @ PM @ v.T
eval = np.random.uniform(0.0, 100.0)
itr, max_itrs = 0, 100000
threshold = 1.0e-10
while abs(eval - eval_next) >= threshold and itr < max_itrs:
    eval = eval_next
    v = PM @ v
    v = v / np.linalg.norm(v)
    eval_next = v.T @ PM @ v
    itr += 1
v = v / np.sum(v)
pages_by_rank = np.argsort(v)[::-1]
logging.info("------------------------------------------------")
logging.info(f"largest eigen value: {eval}")
logging.info(f"largest eigen vector (normalized by probability): {v}")
logging.info(f"num iterations for calculation: {itr}")
if itr == max_itrs:
    logging.info("(NOTE: calculation did not converge!)")
logging.info("------------------------------------------------")
logging.info(f"Pages by rank: {pages_by_rank}")

# Create a Graph object from the probability matrix
g = ig.Graph.Weighted_Adjacency(PM.tolist())
g.to_directed(mode="acyclic")

# Set edges widths, using the following procedure:
# -------------------------------------------------
# 1. Get weight of each width (since the graph was created
#    using a probability matrix, that is exactly the number
#    we're after). Scale by some float factor to make more visible.
# 2. Flatten the widths matrix and remove all elements that are too thin
#    (i.e. below a certain threshold, e.g. 0.05).
widths = np.zeros((num_pages, num_pages))
for edge in g.es:
    widths[edge.source, edge.target] = edge.attributes()["weight"] * 3.5
widths = widths.flatten()
widths = np.delete(widths, np.where(widths < 0.05)[0])

# Coloring the nodes using matplotlib's discrete color map
cmap = mpl.colormaps["Paired"]
colors = cmap(np.linspace(0, 1, num_pages)).tolist()

# Setting nodes size by rank
# -------------------------------------------------
# Create N sizes between min_size and max_size, where
# N is the number of pages, and order them according to
# the page's rank (conveniently already a numpy array)
min_size, max_size = 40, 150
vertex_size = np.linspace(min_size, max_size, num_pages)[pages_by_rank]

# Actual plot
fig, ax = plt.subplots()
ig.plot(
    g,
    target=ax,
    layout="auto",
    vertex_size=vertex_size,
    vertex_color=colors,
    vertex_label=list(range(num_pages)),
    vertex_label_size=15,
    edge_color="black",
    edge_width=widths,
)
plt.show()
