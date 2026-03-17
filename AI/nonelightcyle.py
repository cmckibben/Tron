import pygame

from direction import Direction
from lightcycle import Lightcycle


class NoneLightcycle(Lightcycle):
    def __init__(self, ):
        Lightcycle.__init__(self,0,0,0,Direction.LEFT,pygame.Color(0,0,0),0)
    def update(self):
        pass
    def is_destroyed(self)-> bool:
        return True
    def draw(self):
        pass

    
