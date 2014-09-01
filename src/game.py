__author__ = 'marclund'

import os
import sys
from random import choice, randint
import pygame as pg
from block import IBlock, LBlock
from constants import WIDTH, HEIGHT, CELL_SIZE, colours



class Tetris(object):
    def __init__(self):       
        pg.init()
        os.environ["SDL_VIDEO_CENTERED"] = "True"
        self.screen = pg.display.set_mode((WIDTH,
                                                             HEIGHT))
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = 60
        self.done = False
        self.show_grid = True
        self.speed = 1
        self.base_speed = 1
        self.grid_squares = [pg.Rect((x * CELL_SIZE, y * CELL_SIZE), (CELL_SIZE, CELL_SIZE))
                                      for x in range(WIDTH // CELL_SIZE)
                                      for y in range(HEIGHT // CELL_SIZE)]
        self.blocks = []
        block_classes = [IBlock, LBlock]
        self.block_stack = []
        for _ in range(20):
            klass = choice(block_classes)
            index = (randint(5, 12), 0)
            color = choice(("red", "green", "blue"))
            direct = choice(("up","down", "left", "right"))
            self.block_stack.append(klass(index, color, direct))
        self.current_block = self.block_stack.pop()

    def event_loop(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            self.speed = 10
        else:
            self.speed = self.base_speed
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.done = True
                elif event.key == pg.K_DOWN:
                    self.current_block.rotate("down")
                elif event.key == pg.K_UP:
                    self.current_block.rotate("up")    
                elif event.key == pg.K_RIGHT:
                    if self.current_block.can_move(self):
                        self.current_block.move((CELL_SIZE, 0))
                elif event.key == pg.K_LEFT:
                    if self.current_block.can_move(self):
                        self.current_block.move((-CELL_SIZE, 0))
                elif event.key == pg.K_g:
                    self.show_grid = not self.show_grid

    def update(self):
        self.current_block.update(self)
        if self.current_block.placed:
            self.current_block = self.block_stack.pop()        
        
    def draw(self):    
        self.screen.fill(pg.Color("black"))
        if self.show_grid:
            for square in self.grid_squares:
                pg.draw.rect(self.screen, pg.Color("white"), square, 1)
        for block in self.blocks:
            block.draw(self.screen)
        self.current_block.draw(self.screen)
        
    def run(self):
        while not self.done:
            self.event_loop()
            self.update()
            self.draw()
            pg.display.update()
            self.clock.tick(self.fps)
            pg.display.set_caption("FPS: %d" % self.clock.get_fps())
    
    
if __name__ == "__main__":
    game = Tetris()
    game.run()
    pg.quit()
    sys.exit()    
    

 