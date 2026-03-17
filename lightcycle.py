import pygame
from pygame.locals import *
from direction import Direction

class Lightcycle:
    def __init__(self, x: int, y: int, speed: int, direction: Direction, color: pygame.Color, size: int):
        self.joystick = None
        self.left = None
        self.right = None
        self.down = None
        self.up = None
        self.x  = x
        self.y  = y
        self.speed = speed
        self.direction = direction
        self.color = color
        self.size = size
        self.destroyed = False
        self.screen = pygame.display.get_surface()
        self.has_joystick = False
    
    def map_keys(self, up = 0, down = 0, left = 0, right = 0):
        self.up = up
        self.down = down
        self.right = right
        self.left = left

    def set_joystick(self, joystick: pygame.joystick):
        self.joystick = joystick
        self.has_joystick = True

    def update(self):
        
        if pygame.key.get_pressed()[self.up]:    self.change_direction(Direction.UP)
        if pygame.key.get_pressed()[self.down]:  self.change_direction(Direction.DOWN)
        if pygame.key.get_pressed()[self.left]:  self.change_direction(Direction.LEFT)
        if pygame.key.get_pressed()[self.right]: self.change_direction(Direction.RIGHT)
        if self.has_joystick:
            if self.joystick.get_axis(0) > 0.5: self.change_direction(Direction.RIGHT)
            if self.joystick.get_axis(0) < -0.5: self.change_direction(Direction.LEFT)
            if self.joystick.get_axis(1) > 0.5: self.change_direction(Direction.DOWN)
            if self.joystick.get_axis(1) < -0.5: self.change_direction(Direction.UP)
        self.move()
        if pygame.Surface.get_at(self.screen, (int(self.x), int(self.y))) != pygame.Color(0, 0, 0):
            self.destroyed = True
            self.speed = 0

    def move(self):
        if self.direction == Direction.DOWN:
            self.y += self.speed
        if self.direction == Direction.UP:
            self.y -= self.speed
        if self.direction == Direction.RIGHT:
            self.x += self.speed
        if self.direction == Direction.LEFT:
            self.x -= self.speed

    def is_destroyed(self)-> bool:
        return self.destroyed
    
    def change_direction(self, direction: Direction):
        if self.direction == Direction.DOWN and direction == direction.UP:
            return
        if self.direction == Direction.UP and direction == direction.DOWN:
            return
        if self.direction == Direction.LEFT and direction == direction.RIGHT:
            return
        if self.direction == Direction.RIGHT and direction == direction.LEFT:
            return                        
        self.direction = direction

    def draw(self):
        if not self.destroyed:
            pygame.draw.rect(self.screen,self.color, Rect((self.x,self.y),(self.size,self.size)))

    
