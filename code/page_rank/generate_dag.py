import igraph as ig
import matplotlib.pyplot as plt
import numpy as np

PM = np.load("page_rank_matrix.npy")
# num_pages = 10
# probs = np.ones(num_pages) / num_pages

# First, we generate a random undirected graph with a fixed number of edges, without loops.
g = ig.Graph.Weighted_Adjacency(PM.tolist())

# %%
# Then we convert it to a DAG *in place*. This method samples DAGs with a given number of edges and vertices uniformly.
g.to_directed(mode="acyclic")

# %%
# Finally, we can plot the graph using the Sugiyama layout from :meth:`igraph.Graph.layout_sugiyama`:
# For edge width, check this out: https://stackoverflow.com/questions/23763382/igraph-set-edge-width-by-eid-python
fig, ax = plt.subplots()
ig.plot(
    g,
    target=ax,
    layout="auto",
    vertex_size=50,
    vertex_color=["blue", "red", "green", "purple"],
    edge_color="black",
    edge_width=1,
)
plt.show()
