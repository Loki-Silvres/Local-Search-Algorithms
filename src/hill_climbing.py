import numpy as np
from agent import Agent
from config import *

class HillClimbing:
    def __init__(self, metric : callable, agent : Agent) -> None:
        self.metric = metric
        self.actions = actions
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
        if take_rand_action > Rand_action_thres:
            best_action = rand.choice(self.actions)
            # best_action = rand.choice([ i for i in self.actions if i != best_action])

        return best_action