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
        pass

    def render(self, screen : pygame.Surface) -> None:
        pass


if __name__ == "__main__":
    
    x = np.linspace(start, end, N_points)
    y = np.sum([((1) ** i) * gaussian(x, mu = mu, sig = sig) for i, (mu, sig) in enumerate(zip(MEANS, SIGMAS))], axis= 0)
    plt.plot(x, y)
    plt.show()