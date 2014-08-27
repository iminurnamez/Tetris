__author__ = 'marclund'

import sys
import os
import random

from pygame.locals import *
from block import *


WIDTH = 500
HEIGHT = 500
FPS = 60

#Colours     R    G    B
colours = {
"BLACK" : (  0,   0,   0),
"WHITE" : (255, 255, 255),
"GREEN" : (  0, 255,   0),
"RANDOM": (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))}

def exit_game():
    pygame.quit()
    sys.exit()

pygame.init()
os.environ["SDL_VIDEO_CENTERED"] = "True"
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen_rect = screen.get_rect()
backround = pygame.Surface(screen.get_size())
clock = pygame.time.Clock()

blocks = [Block(WIDTH / 40, HEIGHT / 20, WIDTH / 20, HEIGHT / 20, colours["GREEN"])]
num = 0

while True:
    backround.fill(colours["RANDOM"])
    screen.blit(backround, (0, 0))
    for block in blocks:
        block.display(screen)

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            exit_game()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit_game()
            if event.key == K_DOWN:
                pass
            if event.key == K_RIGHT and blocks[num].rect.right < screen_rect.right:
                blocks[num].rect.left = blocks[num].rect.right
            if event.key == K_LEFT and blocks[num].rect.left > screen_rect.left:
                blocks[num].rect.right = blocks[num].rect.left
            if event.key == K_UP:
                pass
            if event.key == K_SPACE:
                blocks[num].speed += 10

    pygame.display.set_caption("FPS: %d" % clock.get_fps())
    pygame.display.update()
    blocks[num].update()

    if blocks[num].rect.bottom >= screen_rect.bottom:
        blocks[num].speed = 0
        blocks[num].rect.bottom = screen_rect.bottom
        blocks.append(Block(WIDTH / 40, HEIGHT / 20, WIDTH / 20, HEIGHT / 20, colours["GREEN"]))
        num += 1
    for block in blocks:
        if not blocks.index(block) == num:
            if blocks[num].rect.bottom >= block.rect.top and blocks[num].rect.centerx == block.rect.centerx:
                blocks[num].speed = 0
                blocks[num].rect.bottom = block.rect.top
                blocks.append(Block(WIDTH / 40, HEIGHT / 20, WIDTH / 20, HEIGHT / 20, colours["GREEN"]))
                num += 1



