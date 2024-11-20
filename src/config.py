import numpy as np
from numpy import random as rand
SEED : int = 42
rng = rand.RandomState(SEED)

COLUMNS = 17
ROWS = 13

TILESIZE = 32

WINDOW_WIDTH = COLUMNS * TILESIZE
WINDOW_HEIGHT = ROWS * TILESIZE

FPS = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

HILL_COLOUR = GREEN

start : int = -4
end : int = 4

assert end > start 

N_waves : int = 30
N_points : int = 1000

MEANS : np.ndarray = rng.randn(N_waves)
SIGMAS : np.ndarray = rng.rand(N_waves) 

agent_step : float = 0.01
AGENT_RADIUS : float = 2
actions : list = ['left', 'right']

N_iters: int = 10000
Rand_action_thres: float = 0.99


