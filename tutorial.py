import os
import random
import math
import pygame

from os import listdir
from os.path import isfile, join

# Inicializar Pygame
pygame.init()
pygame.display.set_caption("Platformer Sam Gamer")

# Defina as variáveis globais
WIDTH, HEIGHT = 1000, 700
FPS = 60
PLAY_VEL = 5

# Defina a largura e a altura da tela [width, height]
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Pega o background
def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image

# Desenha o background
def draw(window, background, bg_image):
    for tile in background:
        window.blit(bg_image, tile)

    pygame.display.update()

# Função principal
def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(window, background, bg_image)

    pygame.quit()
    quit()

# Inicializa o jogo
if __name__ == "__main__":
    main(window)
