import random
import pygame

from direction import Direction
from lightcycle import Lightcycle

MIN_TICKS = 10
MAX_TICKS = 100
class RandomLightCycle(Lightcycle):
    def __init__(self, x: int, y: int, speed: int, direction: Direction, color: pygame.Color, size: int):
        Lightcycle.__init__(self,x,y,speed,direction,color,size)
        self.ticks = random.randint(MIN_TICKS, MAX_TICKS)
        self.tick_counter = 0
    def update(self):
        if self.destroyed == False:
            self.tick_counter += 1
            if self.tick_counter >= self.ticks:
                self.tick_counter = 0
                done = False
                while not done:
                    dir = random.choice(list(Direction))
                    if dir != self.direction:
                        if  (self.direction == Direction.DOWN and dir == Direction.UP) or \
                            (self.direction == Direction.UP and dir == Direction.DOWN) or \
                            (self.direction == Direction.LEFT and dir == Direction.RIGHT) or \
                            (self.direction == Direction.RIGHT and dir == Direction.LEFT):
                            pass
                        else:
                            self.direction = dir
                            done = True
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
