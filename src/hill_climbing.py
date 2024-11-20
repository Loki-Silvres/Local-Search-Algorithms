from map import Map
import numpy as np
from config import *
from agent import Agent
from local_search_algorithms import HillClimbing
import pygame

def main(debug = False) -> None:
    map = Map()
    agent = Agent()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    algorithm = HillClimbing(agent = agent, map = map)

    if debug:
        itr = 0
        
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        init_pos = agent.get_state()['position']
        best_action = algorithm.evaluate(init_pos)
        init_metric = map.metric(init_pos)
        agent.take_action(best_action)
        new_metric = map.metric(agent.get_state()['position'])

        if debug:
            if itr % 1000 == 0:
                print("Iteration: ", itr)
                print("Initial position:", init_pos)
                print("Initial metric: ", init_metric)
                print("Best action: ", best_action)
                print("Best action's metric: ", new_metric)
        itr += 1

        screen.fill(WHITE)
        map.render(screen)
        agent.render(screen) 
        pygame.display.update()

if __name__ == "__main__":
    main(debug=True)