import numpy as np
import matplotlib.pyplot as plt
from planning_utils import a_star, heuristic, create_grid, prune_path


def plot_grid(grid):
    plt.imshow(grid, cmap='Greys', origin='lower') 
    plt.xlabel('EAST')
    plt.ylabel('NORTH')
    plt.show()
    
def plot_path(grid, path, start, goal):
    plt.imshow(grid, cmap='Greys', origin='lower')
    # For the purposes of the visual the east coordinate lay along
    # the x-axis and the north coordinates long the y-axis.

    pp = np.array(path)
    plt.plot(pp[:, 1], pp[:, 0], 'b.')
    plt.plot(start[1], start[0], 'yo')
    plt.plot(goal[1], goal[0], 'ro')

    plt.xlabel('EAST')
    plt.ylabel('NORTH')
    plt.show()   