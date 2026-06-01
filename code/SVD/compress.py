# Credit for pics 3 and 4: https://www.duda.news/tier-abc/tapir/
from PIL import Image
import numpy as np
from sys import argv
from pathlib import Path
import matplotlib.pyplot as plt

filepath = Path(argv[1])
output_filepath = (
    f"{filepath.parent.absolute()}/{filepath.stem}_reduced{filepath.suffix}"
)
K = int(argv[2])
R, G, B = 0, 1, 2

# Convert image to numpy array
img_file = Image.open(filepath).convert("RGB")
img_matrix = np.array(img_file)
num_rows, num_cols = img_matrix.shape[:2]
reduced_matrix = np.zeros((num_rows, num_cols, 3))

# SVD
for color in [R, G, B]:
    U, S, Vh = np.linalg.svd(img_matrix[:, :, color])
    reduced_matrix[:, :, color] = U[:, :K] @ np.diag(S[:K]) @ Vh[:K]

# Show image
# plt.imshow(reduced_matrix.astype(np.uint8), interpolation="nearest")
# plt.show()

print(f"Original size: {img_matrix.nbytes}")
print(f"Reduced size: {reduced_matrix.astype(np.uint8).nbytes}")

# TODO: add argparse, optional save/view file, etc.
