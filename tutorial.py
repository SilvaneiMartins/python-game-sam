import os
import random
import math
import pygame

from os import listdir
from os.path import isfile, join

# Inicializar Pygame
pygame.init()
pygame.display.set_caption("Platformer Sam Gamer")

# Defina as variáveis
BG_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 1000, 700
FPS = 60
PLAY_VEL = 5

# Defina a largura e a altura da tela [width, height]
window = pygame.display.set_mode((WIDTH, HEIGHT))

def main(window):
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)
