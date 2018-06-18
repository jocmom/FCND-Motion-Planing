import numpy as np
import matplotlib.pyplot as plt
from planning_utils import a_star, heuristic, create_grid, prune_path


def plot_grid(grid):
    plt.imshow(grid, origin='lower') 
    plt.xlabel('EAST')
    plt.ylabel('NORTH')
    plt.show()
    
def plot_path(grid, path, start_ne, goal_ne):
    plt.imshow(grid, cmap='Greys', origin='lower')
    # For the purposes of the visual the east coordinate lay along
    # the x-axis and the north coordinates long the y-axis.
    plt.plot(start_ne[1], start_ne[0], 'x')
    plt.plot(goal_ne[1], goal_ne[0], 'x')

    pp = np.array(path)
    plt.plot(pp[:, 1], pp[:, 0], 'g')

    plt.xlabel('EAST')
    plt.ylabel('NORTH')
    plt.show()   