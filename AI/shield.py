import pygame

from direction import Direction
from lightcycle import Lightcycle


class ShieldLightcycle(Lightcycle):
    def __init__(self, x: int, y: int, speed: int, direction: Direction, color: pygame.Color, size: int):
        Lightcycle.__init__(self,x,y,speed,direction,color,size)
        self.ticks = 5
        self.tick_counter = 0
          
    def update(self):
        if not self.destroyed:
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
        if self.destroyed:
            if self.direction == Direction.UP:
                if pygame.Surface.get_at(self.screen, (int(self.x-self.speed), int(self.y+self.speed))) == pygame.Color(0, 0, 0):
                    self.y += self.speed
                    self.direction = Direction.LEFT
                    self.destroyed = False
                    self.update()
            if self.direction == Direction.DOWN:
                if pygame.Surface.get_at(self.screen, (int(self.x+self.speed), int(self.y-self.speed))) == pygame.Color(0, 0, 0):
                    self.y -= self.speed
                    self.direction = Direction.RIGHT
                    self.destroyed = False
                    self.update()
            if self.direction == Direction.LEFT:
                if pygame.Surface.get_at(self.screen, (int(self.x+self.speed), int(self.y+self.speed))) == pygame.Color(0, 0, 0):
                    self.x += self.speed
                    self.direction = Direction.DOWN
                    self.destroyed = False
                    self.update()
            if self.direction == Direction.RIGHT:
                if pygame.Surface.get_at(self.screen, (int(self.x-self.speed), int(self.y-self.speed))) == pygame.Color(0, 0, 0):
                    self.x -= self.speed
                    self.direction = Direction.UP
                    self.destroyed = False
                    self.update()                                        