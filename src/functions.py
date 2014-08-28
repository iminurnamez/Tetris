__author__ = 'marclund'
import pygame
import sys

def exit_game():
    pygame.quit()
    sys.exit()

def check_right_collision(current_blocks, screen_rect):
    for current_block in current_blocks:
        if current_block.rect.right < screen_rect.right:
            return True
        else:
            return False

def check_left_collision(current_blocks, screen_rect):
    for current_block in current_blocks:
        if current_block.rect.left > screen_rect.left:
            return True
        else:
            return False

