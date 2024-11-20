import numpy as np
from config import *
import matplotlib.pyplot as plt
import pygame

def gaussian(x, mu = 0, sig = 1) -> float:
    return (
        1.0 / (np.sqrt(2.0 * np.pi) * sig) * np.exp(-np.power((x - mu) / sig, 2.0) / 2)
    )

def get_height(point : float) -> float:
    return np.sum([gaussian(point, mu = mu, sig = sig) for i, (mu, sig) in enumerate(zip(MEANS, SIGMAS))], axis= 0)

def metric(point : float) -> float:
    return get_height(point)

class Map:
    def __init__(self) -> None:
        self.grid = None
        self.fill_grid()

    def get_height_in_img(self, point : int) -> int:
        return WINDOW_HEIGHT - self.hill_fill_height[point]
        
    def fill_grid(self) -> None:

        cols_on_surface = np.linspace(start, end, WINDOW_WIDTH)
        rows_on_surface = get_height(cols_on_surface)

        upper_bound_in_img = int(0.8 * WINDOW_HEIGHT)
        lower_bound_in_img = int(0.2 * WINDOW_HEIGHT)
        bound_difference_in_img = upper_bound_in_img - lower_bound_in_img
        self.hill_fill_height = rows_on_surface / (np.max(rows_on_surface) - np.min(rows_on_surface)) * (bound_difference_in_img) + lower_bound_in_img
        
        self.hill_fill_height = self.hill_fill_height.astype(int)
        self.grid = np.zeros([WINDOW_HEIGHT, WINDOW_WIDTH])

        for i in range(WINDOW_HEIGHT):
            for j in range(WINDOW_WIDTH):
                if self.hill_fill_height[j] > i:
                    self.grid[WINDOW_HEIGHT - i - 1][j] = 1
        self.grid = self.grid.transpose()
        self.grid = np.stack([self.grid, self.grid, self.grid], axis = 2)

    def render(self, screen : pygame.Surface) -> None:
        img = self.grid * np.array(HILL_COLOUR)
        img += (1 - self.grid) * np.array(WHITE)
        screen.blit(pygame.surfarray.make_surface(img), (0, 0))

if __name__ == "__main__":
    map = Map()
    plt.imshow(map.grid)
    plt.show()
    img = map.grid * np.array(HILL_COLOUR)
    # x = np.linspace(start, end, N_points)
    # y = np.sum([((1) ** i) * gaussian(x, mu = mu, sig = sig) for i, (mu, sig) in enumerate(zip(MEANS, SIGMAS))], axis= 0)
    # plt.plot(x, y)
    # plt.show()