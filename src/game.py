__author__ = 'marclund'

import os
import pygame
from pygame.locals import *

from block import *
from functions import *

pygame.init()
os.environ["SDL_VIDEO_CENTERED"] = "True"
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen_rect = screen.get_rect()
backround = pygame.Surface(screen.get_size())
clock = pygame.time.Clock()

current_blocks = Blockgroup().block_group
blocks = []
block_group = Blockgroup()

while True:
    backround.fill(colours["RANDOM"])
    screen.blit(backround, (0, 0))
    print len(current_blocks)
    for block in blocks:
        block.display(screen)

    for current_block in current_blocks:
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

            if event.key == K_RIGHT and check_right_collision(current_blocks, screen_rect):
                clear = True
                for block in blocks:
                    for current_block in current_blocks:
                        if block.rect.top < current_block.rect.bottom and block.rect.bottom > current_block.rect.top and block.rect.left == current_block.rect.right:
                            clear = False
                            break
                if not clear:
                    break
                if clear:
                    for current_block in current_blocks:
                        current_block.rect.left = current_block.rect.right

            if event.key == K_LEFT and check_left_collision(current_blocks, screen_rect):
                clear = True
                for block in blocks:
                    if block.rect.top < current_block.rect.bottom and block.rect.bottom > current_block.rect.top and block.rect.right == current_block.rect.left:
                        clear = False
                        break

                if clear:
                    for current_block in current_blocks:
                        current_block.rect.right = current_block.rect.left

            if event.key == K_UP:
                pass

            if event.key == K_SPACE:
                for current_block in current_blocks:
                    current_block.speed += 10

    pygame.display.set_caption("FPS: %d" % clock.get_fps())
    pygame.display.update()

    current_block_stopped = False
    distance_to_raise = 0

    for current_block in current_blocks:
        current_block.update()

        if current_block.rect.bottom >= screen_rect.bottom:
            distance_to_raise = screen_rect.bottom - current_block.rect.bottom
            current_block_stopped = True
            break

    if not current_block_stopped:
        for block in blocks:
            for current_block in current_blocks:
                if current_block.rect.bottom >= block.rect.top and current_block.rect.centerx == block.rect.centerx:
                    distance_to_raise = block.rect.top - current_block.rect.bottom
                    current_block_stopped = True
                    break
            if current_block_stopped:
                break

    if current_block_stopped:
        for current_block in current_blocks:
            current_block.speed = 0
            current_block.rect.bottom += distance_to_raise
            blocks.append(current_block)
            current_blocks = Blockgroup().block_group




