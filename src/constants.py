__author__ = 'marclund'
import random

WIDTH = 500
HEIGHT = 500
FPS = 60
CELL_SIZE = WIDTH // 20

#Colours     R    G    B
colours = {
    "BLACK" : (  0,   0,   0),
    "WHITE" : (255, 255, 255),
    "GREEN" : (  0, 255,   0),
    "RANDOM": (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))}

