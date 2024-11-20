import numpy as np
from agent import Agent
from map import Map
from config import *

class HillClimbing:
    def __init__(self, agent : Agent, map : Map) -> None:
        self.metric = Map().metric
        self.actions = ACTIONS
        self.agent = agent

    def evaluate(self, position : float) -> str:
        max_metric: float = 0
        best_action: str = ""
        for action in self.actions:
            metric = self.metric(position + self.agent.get_actions()[action])
            if metric > max_metric:
                max_metric = metric
                best_action = action
        take_rand_action: float = rand.rand()
        if take_rand_action < RANDOM_ACTION_THRES:
            best_action = rand.choice(self.actions)

        return best_action

class SimulatedAnnealing:
    def __init__(self, agent : Agent, map : Map) -> None:
        self.metric = Map().metric