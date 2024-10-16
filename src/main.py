from map import metric
import numpy as np
from config import *
from agent import Agent
from hill_climbing import HillClimbing
# import pygame as pg

def main() -> None:
    agent = Agent()
    algorithm = HillClimbing(metric = metric, agent = agent)
    for i in range(N_iters):

        init_pos = agent.get_state()['position']
        best_action = algorithm.evaluate(init_pos)
        init_metric = metric(init_pos)
        agent.take_action(best_action)
        new_metric = metric(agent.get_state()['position'])
        
        # if new_metric < init_metric:
        #     agent.undo_action(best_action)
        #     print("No improvement in metric. Iteration:", i)
        #     print("Position:", init_pos)
        #     break

        if i % 1000 == 0:
            print("Iteration: ", i)
            print("Initial position:", init_pos)
            print("Initial metric: ", init_metric)
            print("Best action: ", best_action)
            print("Best action's metric: ", new_metric)


if __name__ == "__main__":
    main()