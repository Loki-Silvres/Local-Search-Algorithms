import pygame
import numpy as np
from map import Map 
from config import *

class Agent:

    def __init__(self, initial_position : float = None):
        self.map = Map()
        if initial_position is not None:
            self.position = initial_position
        else:
            self.position = (np.random.rand() - 0.5) * (MAP_END - MAP_START) / 2 
    
    @property
    def position_in_img(self):
        return int((self.position - MAP_START) / (MAP_END - MAP_START) * WINDOW_WIDTH)
        
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
        if self.position < MAP_END and self.position > MAP_START:
            return {
                "left" : -AGENT_STEP,
                "right" : AGENT_STEP
                }
        elif self.position >= MAP_END:
            return {
                "left" : -AGENT_STEP,
                "right" : 0
                }
        elif self.position <= MAP_START:
            return {
                "left" : 0,
                "right" : AGENT_STEP
                }
        
    def update(self, new_position : float) -> None:
        self.position = new_position
    
    def render(self, screen : pygame.Surface) -> None:
        self.height_in_img = self.map.get_height_in_img(self.position_in_img)
        pygame.draw.circle(screen, RED, (self.position_in_img, self.height_in_img), AGENT_RADIUS)

if __name__ == "__main__":
    agent: Agent = Agent()
    print(agent.position)   
    print(agent.get_actions())
    print(agent.get_state())
    agent.take_action("left")
    print(agent.get_state())