"""

.. _tutorials-dag:

======================
Directed Acyclic Graph
======================

This example demonstrates how to create a random directed acyclic graph (DAG), which is useful in a number of contexts including for Git commit history.
"""

import igraph as ig
import matplotlib.pyplot as plt
import random
import secrets


# %%
# First, we set a random seed for reproducibility.
seed = secrets.randbelow(1_000_000_000)
print(seed)
random.seed(seed)

# %%
# First, we generate a random undirected graph with a fixed number of edges, without loops.
g = ig.Graph.Erdos_Renyi(n=15, m=30, directed=True, loops=False)

# %%
# Then we convert it to a DAG *in place*. This method samples DAGs with a given number of edges and vertices uniformly.
g.to_directed(mode="acyclic")

# %%
# We can print out a summary of the DAG.
# ig.summary(g)


# %%
# Finally, we can plot the graph using the Sugiyama layout from :meth:`igraph.Graph.layout_sugiyama`:
fig, ax = plt.subplots()
ig.plot(
    g,
    target=ax,
    layout="sugiyama",
    vertex_size=50,
    vertex_color=["blue", "red", "green", "yellow"],
    edge_color="#00AAFF",
    edge_width=2,
)
plt.show()
