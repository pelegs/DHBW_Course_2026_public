import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from scipy.ndimage import convolve

num_rows, num_columns = 50, 50
num_steps = 1000
game_mat = np.zeros((num_steps, num_rows, num_columns), dtype=np.uint8)

shapes = {
    "block": [[1, 1], [1, 1]],
    "blinker_h": [[1, 1, 1]],
    "blinker_v": [[1], [1], [1]],
    "glider": [[0, 1, 0], [0, 0, 1], [1, 1, 1]],
    "tee": [[0, 1, 0], [1, 1, 1]],
}


def put_shape(shape, game_mat, upper_left_corner=[0, 0]):
    shape_np = np.array(shapes[shape], dtype=np.uint8)
    r, c = upper_left_corner
    h, w = shape_np.shape
    game_mat[r : r + h, c : c + w] = shape_np
    return game_mat


game_mat[0] = put_shape("block", game_mat[0], [10, 10])
game_mat[0] = put_shape("glider", game_mat[0], [20, 10])
game_mat[0] = put_shape("blinker_h", game_mat[0], [30, 20])
game_mat[0] = put_shape("blinker_v", game_mat[0], [20, 30])
game_mat[0] = put_shape("tee", game_mat[0], [40, 40])


kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]], dtype=np.uint8)

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
    fig, update_animation, frames=num_steps, interval=100, blit=True
)
plt.show()
