import igraph as ig
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from itertools import permutations

# Load page links probability matrix
PM = np.load("page_rank_matrix.npy")
num_pages = PM.shape[0]
# probs = np.ones(num_pages) / num_pages

# Create a Graph object from the probability matrix
g = ig.Graph.Weighted_Adjacency(PM.tolist())
g.to_directed(mode="acyclic")

# Set edges witdths, using the following procedure:
# 1. Create a default widths list (all ones)
# 2. Create a list of indices 0,1,...,num_pages
# 3. Using python's itertools permutations function,
#    create a list of all pairs of nodes except those
#    that where the two nodes are the same (e.g. (0,0), (1,1), etc.)
# 4. Iterate over edges list and use the probability matrix to set the
#    width of the respective edge (if it exsits, hence the try/except block)
widths = np.ones(num_pages**2)
idx_list = list(range(num_pages))
edges = list(permutations(idx_list, 2))
for src, dest in edges:
    try:
        id = g.get_eid(src, dest)
        widths[id] = PM[src, dest]
    except Exception:
        print(f"No edge between vertices {src} and {dest}.")

# Coloring the nodes using matplotlib's discrete color map
cmap = mpl.colormaps["Paired"]
colors = cmap(np.linspace(0, 1, num_pages)).tolist()

# Actual plot
fig, ax = plt.subplots()
ig.plot(
    g,
    target=ax,
    layout="auto",
    vertex_size=75,
    vertex_color=colors,
    vertex_label=idx_list,
    edge_color="black",
    edge_width=widths * 2,
)
plt.show()
