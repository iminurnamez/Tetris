__author__ = 'marclund'
import pygame
from constants import *
block_group = []

class Block:

    def __init__(self, x, y, width, height, colour):
        self.surface = pygame.Surface((width, height)).convert()
        self.rect = self.surface.get_rect()
        self.rect.center = (x, y)
        self.block1 = pygame.draw.rect(self.surface, (0, 0, 0), (0, 0, width, height))
        self.block = pygame.draw.rect(self.surface, colour, (width - (width * 0.95), height - (height * 0.95), width * 0.95, height * 0.95))
        self.speed = 1

    def display(self, surface):
        surface.blit(self.surface, self.rect)

    def update(self):
        self.rect.centery += self.speed

class Blockgroup_line:

    def __init__(self):
        block_group.append([
            Block(WIDTH / 40, HEIGHT / 20, WIDTH / 20, HEIGHT / 20, colours["GREEN"]),
            Block(WIDTH / 40, (HEIGHT / 20) + (HEIGHT / 10), WIDTH / 20, HEIGHT / 20, colours["GREEN"]),
            Block(WIDTH / 40, (HEIGHT / 20) + (2 * (HEIGHT / 10)), WIDTH / 20, HEIGHT / 20, colours["GREEN"]),
            Block(WIDTH / 40, (HEIGHT / 20) + (3 * (HEIGHT / 10)), WIDTH / 20, HEIGHT / 20, colours["GREEN"]),
            Block(WIDTH / 40, (HEIGHT / 20) + (4 * (HEIGHT / 10)), WIDTH / 20, HEIGHT / 20, colours["GREEN"])
        ])
