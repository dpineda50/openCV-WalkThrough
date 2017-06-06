import numpy as np
import pygame

height = 480
width = 360

pygame.init()

screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("Maze Runner")

def check_game_state():
    for event in pygame.event.get():
        if event.type == pygame.K_SPACE:
            return false
while True:
    pygame.display.flip()
    if check_game_state() is False:
        break

