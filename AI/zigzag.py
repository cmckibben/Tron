import random
import pygame

from direction import Direction
from lightcycle import Lightcycle


class ZigZagLightcycle(Lightcycle):
    def __init__(self, x: int, y: int, speed: int, direction: Direction, color: pygame.Color, size: int):
        Lightcycle.__init__(self,x,y,speed,direction,color,size)
        self.ticks = 1
        self.tick_counter = 0
 
        self.setDirectionList()

 

    def setDirectionList(self):
        self.directionList = []
        self.directionIndex = 0
        if self.direction == Direction.UP:
            self.directionList = [Direction.LEFT,Direction.UP]
        if self.direction == Direction.DOWN:
            self.directionList = [Direction.RIGHT,Direction.DOWN]    
        if self.direction == Direction.LEFT:
            self.directionList = [Direction.UP,Direction.LEFT]
        if self.direction == Direction.RIGHT:
            self.directionList = [Direction.DOWN,Direction.RIGHT]               
    def update(self):
        if not self.destroyed:
            self.tick_counter += 1
            if self.tick_counter >= self.ticks:
                self.tick_counter = 0
                self.directionIndex +=1
                if self.directionIndex >= len(self.directionList):
                    self.directionIndex = 0
                self.direction = self.directionList[self.directionIndex]
            if self.direction == Direction.DOWN:
                self.y += self.speed
            if self.direction == Direction.UP:
                self.y -= self.speed
            if self.direction == Direction.RIGHT:
                self.x += self.speed
            if self.direction == Direction.LEFT:
                self.x -= self.speed 
            if pygame.Surface.get_at(self.screen, (int(self.x), int(self.y))) != pygame.Color(0, 0, 0):
                self.destroyed = True
