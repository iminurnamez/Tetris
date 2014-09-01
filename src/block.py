__author__ = 'marclund'

from random import randint
from itertools import cycle
import pygame as pg
from constants import CELL_SIZE

#unimplemented
class BlockStackGenerator:
    """"Generates block stacks"""

#unimplemented
class BlockStack:
    """Holds game pieces"""
    
    def show_next_blocks(self, n):
        """Returns n-length slice from end of self.blocks"""
        pass

    def get_next(self):
        return self.pop()
        
        
class BlockTile(object):
    """Represents an individual block that fills one grid cell"""
    def __init__(self, pos, color):
        self.pos = pos
        self.color = color
        self.surface = pg.Surface((CELL_SIZE, CELL_SIZE)).convert()
        self.rect = self.surface.get_rect()
        self.surface.fill(pg.Color("gray1"))
        margin = max(int(self.rect.width * .05), 1)
        pg.draw.rect(self.surface, pg.Color(self.color),
                            self.rect.inflate(-margin * 2, -margin * 2))
        self.rect.topleft = self.pos
        
    def draw(self, surface):
        pg.draw.rect(surface, pg.Color("white"), self.rect)
        surface.blit(self.surface, self.rect)
        
    def move(self, offset):
        self.pos = (self.pos[0] + offset[0],
                         self.pos[1] + offset[1])
        self.rect.topleft = self.pos
        
        
class BlockGroup(object):
    """Base class for game pieces.""" 
    def __init__(self, index, color): 
        self.color = color
        self.placed = False
        self.directs = cycle(["left", "down", "right", "up"])
        for _ in range(randint(1, 4)):
            self.direction = next(self.directs)
        self.footprint = (len(self.charmap[self.direction][0]), len(self.charmap[self.direction]))
        self.width = CELL_SIZE * self.footprint[0]
        self.height = CELL_SIZE * self.footprint[1]
        self.pos = index[0] * CELL_SIZE, 0 # topleft
        self.rect = pg.Rect(self.pos, (self.width, self.height))
        self.blocks = []
        self.make_blocks()
        
    def make_blocks(self):    
        self.blocks = []
        self.footprint = (len(self.charmap[self.direction][0]), len(self.charmap[self.direction]))
        self.width = CELL_SIZE * self.footprint[0]
        self.height = CELL_SIZE * self.footprint[1]
        self.rect = pg.Rect(self.pos, (self.width, self.height))        
        left, top = self.rect.topleft
        for row in self.charmap[self.direction]:
            for char in row:
                if char == "B":
                    self.blocks.append(BlockTile((left, top), self.color))
                left += CELL_SIZE
            top += CELL_SIZE        
            left = self.rect.left
            
    def can_move(self, game):
        game_blocks = game.blocks
        for b in self.blocks:
            bumper = b.rect.inflate(CELL_SIZE, -3) # deflating the height allows sliding under blocks
            bumper.bottom = b.rect.bottom
            for block in game_blocks:
                if block.rect.colliderect(bumper):
                   return False
        return True

    def move(self, offset):
        self.pos = (self.pos[0] + offset[0],
                         self.pos[1] + offset[1])
        self.rect.topleft = self.pos
        for block in self.blocks:
            block.move(offset)

    def rotate(self, up_or_down):
        if up_or_down == "up":
            self.direction = next(self.directs)
        else:
            for _ in range(3):
                self.direction = next(self.directs)
        self.change_direction()
        
    def change_direction(self):
        self.make_blocks() 
        
    def snap_to(self):
        """Snaps each block's rect to game grid coordinates"""
        for block in self.blocks:
            
            top_index = block.rect.top // CELL_SIZE
            print "BLOCK TOP: ", block.rect.top
            print "TOP INDEX: ", top_index
            print "RECT / SIZE: ", block.rect.top // CELL_SIZE
            block.pos = (block.rect.left, top_index * CELL_SIZE)
            block.rect.topleft = block.pos
            
    def place(self, game):
        """Adds blocks to game blocks and set placed flag""" 
        self.snap_to()
        for block in self.blocks:
            block.placed = True
            game.blocks.append(block)
        self.placed = True
    
    def clamp(self, game):
        """Keeps piece on board"""
        for block in self.blocks:
            clamped = block.rect.clamp(game.screen_rect)
            if clamped != block.rect:
                offset = (-(block.rect.left - clamped.left),
                              -(block.rect.top - clamped.top))
                self.move(offset)
                
    def collided(self, game):
        """Returns True if piece needs to be placed"""
        for block in self.blocks:
            if block.rect.bottom >= game.screen_rect.bottom:
                return True
            colliders = [x for x in game.blocks if x.rect.colliderect(block.rect)]
            bottom_colliders = [b for b in colliders if (b.rect.top <= block.rect.bottom
                                                                          and block.rect.left == b.rect.left)]
            
            if bottom_colliders:
                return True
            #elif colliders:
            #    self.snap_to()
            #    break
        
                
    def update(self, game):
        game_blocks = game.blocks
        if self.collided(game):
            self.place(game)
            return
        self.move((0, game.speed))
        self.clamp(game)       
            
    def draw(self, surface):
        for block in self.blocks:
            block.draw(surface)
            
    
class IBlock(BlockGroup):
    charmap = {"up": ["XXBX",
                                 "XXBX",
                                 "XXBX",
                                 "XXBX"],
                       "left": ["XXXX",
                                  "BBBB",
                                  "XXXX",
                                  "XXXX"],
                       "down": ["XBXX",
                                     "XBXX",
                                     "XBXX",
                                     "XBXX"],
                       "right": ["XXXX",
                                    "XXXX",
                                    "BBBB",
                                    "XXXX"]}
    charmap["down"] = charmap["up"]
    charmap["right"] = charmap["left"]
                             
    def __init__(self, index, color, direction):
        super(IBlock, self).__init__(index, color) 
    
        
class LBlock(BlockGroup):
    charmap = {"up": ["BXX",
                                "BXX",
                                "BBX"], 
                      "down": ["XBB",
                                    "XXB",
                                    "XXB"],
                      "left": ["XXX",
                                 "XXB",
                                 "BBB"],
                      "right": ["BBB",
                                   "BXX",
                                   "XXX"]}
    
    def __init__(self, index, color, direction):
        super(LBlock, self).__init__(index, color)    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    

                                                          