import numpy as np
from config import *

class Agent:

    def __init__(self, initial_position : float = None):
        if initial_position is not None:
            self.position = initial_position
        else:
            self.position = (np.random.rand() - 0.5) * (end - start) / 2 
        
    def take_action(self, action : str) -> None:
        if action != "left" and action != "right":
            raise Exception("Invalid action")

        self.position += self.get_actions()[action]
        
    def undo_action(self, action : str) -> None:
        if action != "left" and action != "right":
            raise Exception("Invalid action")

        self.position -= self.get_actions()[action]

    def get_state(self) -> dict:
        return {
            "position" : self.position
            }
    def get_actions(self) -> dict:
        if self.position < end and self.position > start:
            return {
                "left" : -agent_step,
                "right" : agent_step
                }
        elif self.position >= end:
            return {
                "left" : -agent_step,
                "right" : 0
                }
        elif self.position <= start:
            return {
                "left" : 0,
                "right" : agent_step
                }

if __name__ == "__main__":
    agent: Agent = Agent()
    print(agent.position)   
    print(agent.get_actions())
    print(agent.get_state())
    agent.take_action("left")
    print(agent.get_state())