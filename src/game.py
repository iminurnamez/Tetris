__author__ = 'marclund'

import os
import pygame
from pygame.locals import *

from constants import *
from block import *
from functions import *

pygame.init()
os.environ["SDL_VIDEO_CENTERED"] = "True"
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen_rect = screen.get_rect()
backround = pygame.Surface(screen.get_size())
clock = pygame.time.Clock()

current_block = Block(WIDTH / 40, HEIGHT / 20, WIDTH / 20, HEIGHT / 20, colours["GREEN"])
blocks = []
#num = 0

while True:
    backround.fill(colours["RANDOM"])
    screen.blit(backround, (0, 0))

    for block in blocks:
        block.display(screen)

    current_block.display(screen)

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            exit_game()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit_game()
            if event.key == K_DOWN:
                pass
            if event.key == K_RIGHT and current_block.rect.right < screen_rect.right:
                clear = True
                for block in blocks:
                    pass
                    #if block.rect.top
                current_block.rect.left = current_block.rect.right
            if event.key == K_LEFT and current_block.rect.left > screen_rect.left:
                current_block.rect.right = current_block.rect.left
            if event.key == K_UP:
                pass
            if event.key == K_SPACE:
                current_block.speed += 10

    pygame.display.set_caption("FPS: %d" % clock.get_fps())
    pygame.display.update()
    current_block.update()

    if current_block.rect.bottom >= screen_rect.bottom:
        current_block.speed = 0
        current_block.rect.bottom = screen_rect.bottom
        blocks.append(current_block)
        current_block = Block(WIDTH / 40, HEIGHT / 20, WIDTH / 20, HEIGHT / 20, colours["GREEN"])
        #blocks.append(Block(WIDTH / 40, HEIGHT / 20, WIDTH / 20, HEIGHT / 20, colours["GREEN"]))
        #num += 1
    for block in blocks:
        if current_block.rect.bottom >= block.rect.top and current_block.rect.centerx == block.rect.centerx:
            current_block.speed = 0
            current_block.rect.bottom = block.rect.top
            blocks.append(current_block)
            current_block = Block(WIDTH / 40, HEIGHT / 20, WIDTH / 20, HEIGHT / 20, colours["GREEN"])
            #blocks.append(Block(WIDTH / 40, HEIGHT / 20, WIDTH / 20, HEIGHT / 20, colours["GREEN"]))
            #num += 1



