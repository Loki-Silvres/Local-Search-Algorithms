import numpy as np
from numpy import random as rand
SEED : int = 42
RNG = rand.RandomState(SEED)

COLUMNS: int = 17
ROWS: int = 13

TILESIZE: int = 32

WINDOW_WIDTH: int = COLUMNS * TILESIZE
WINDOW_HEIGHT: int = ROWS * TILESIZE

FPS: int = 30

BLACK: tuple[int, int, int] = (0, 0, 0)
WHITE: tuple[int, int, int] = (255, 255, 255)
RED: tuple[int, int, int] = (255, 0, 0)
GREEN: tuple[int, int, int] = (0, 255, 0)
BLUE: tuple[int, int, int] = (0, 0, 255)

HILL_COLOUR = GREEN

MAP_START : int = -4
MAP_END : int = 4

assert MAP_END > MAP_START 

N_waves : int = 30
N_points : int = 1000

MEANS : np.ndarray = RNG.randn(N_waves)
SIGMAS : np.ndarray = RNG.rand(N_waves) 

AGENT_STEP : float = 0.01
AGENT_RADIUS : float = 2
ACTIONS : list = ['left', 'right']

NUM_ITERS: int = 10000
RANDOM_ACTION_THRES: float = 0.99


