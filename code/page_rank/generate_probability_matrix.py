import numpy as np

# Read data into an N×2 matrix, where each row represents a link clicked
# (source is at index 0, destination at index 1)
data = np.loadtxt("navigation.log", delimiter=":").astype(np.int32)

# Calculate number of pages from matrix
# (because I'm lazy and don't want to enter this manually)
num_pages = np.max(data) + 1

# Initialize an zero matrix of dimensions N×N
page_rank_matrix = np.zeros(shape=(num_pages, num_pages))

# Iterate over data matrix, adding 1 each time user pressed
# link to page [to_num] from page [from_num]
for from_num, to_num in data:
    page_rank_matrix[from_num, to_num] += 1

# Create a vector of row sums and use it to normalize page_rank_matrix
# (the normalization in this case is a probability one, i.e. the L1 norm)
row_sums = page_rank_matrix.sum(axis=1)
# Make the sum 1 in case its 0, to avoid division by 0
for i, sum in enumerate(row_sums):
    if sum == 0:
        row_sums[i] = 1
# Matrix normalization
page_rank_matrix = page_rank_matrix / row_sums[:, np.newaxis]

# Save the results
np.save("page_rank_matrix.npy", page_rank_matrix)
