import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from scipy.ndimage import convolve

M, N = 100, 100
num_steps = 1000
game_mat = np.random.randint(0, 2, size=(num_steps, M, N), dtype=np.uint8)
kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]], dtype=np.uint8)
# kernel = np.ones((3, 3))
# kernel[1, 1] = 0

# Main loop
for step in range(num_steps - 1):
    convolved_mat = convolve(
        game_mat[step],
        kernel,
        mode="wrap",
    )
    game_mat[step + 1] = (
        (game_mat[step] == 1) & (convolved_mat == 2)
        | (convolved_mat == 3)
        | (game_mat[step] == 0) & (convolved_mat == 3)
    ).astype(np.uint8)


# Animation
def update_animation(frame):
    im.set_data(game_mat[frame])
    return [im]


fig, ax = plt.subplots()
ax.set_aspect("equal")
ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
im = ax.imshow(game_mat[0], cmap="hot")
animation = FuncAnimation(
    fig, update_animation, frames=num_steps, interval=10, blit=True
)
plt.show()
