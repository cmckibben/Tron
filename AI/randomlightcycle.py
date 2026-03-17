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
        if not self.destroyed:
            self.tick_counter += 1
            if self.tick_counter >= self.ticks:
                self.tick_counter = 0
                done = False
                while not done:
                    direction = random.choice(list(Direction))
                    if direction != self.direction:
                        if  (self.direction == Direction.DOWN and direction == Direction.UP) or \
                            (self.direction == Direction.UP and direction == Direction.DOWN) or \
                            (self.direction == Direction.LEFT and direction == Direction.RIGHT) or \
                            (self.direction == Direction.RIGHT and direction == Direction.LEFT):
                            pass
                        else:
                            self.direction = direction
                            done = True
                self.move()
            if pygame.Surface.get_at(self.screen, (int(self.x), int(self.y))) != pygame.Color(0, 0, 0):
                self.destroyed = True
