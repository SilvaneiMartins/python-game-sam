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

# Classe do jogador
class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    GRAVITY = 1

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel)

        self.fall_count += 1

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, self.rect)

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
def draw(window, background, bg_image, player):
    for tile in background:
        window.blit(bg_image, tile)

    player.draw(window)

    pygame.display.update()

# Trata o movimento do jogador
def handle_movement(player):
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    if keys[pygame.K_LEFT]:
        player.move_left(PLAY_VEL)
    if keys[pygame.K_RIGHT]:
        player.move_right(PLAY_VEL)

# Função principal
def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")

    player = Player(100, 100, 50, 50)

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        player.loop(FPS)
        handle_movement(player)
        draw(window, background, bg_image, player)

    pygame.quit()
    quit()

# Inicializa o jogo
if __name__ == "__main__":
    main(window)
