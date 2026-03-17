import random
import pygame

from AI.randomlightcycle import RandomLightCycle
from direction import Direction

class RandomLightCycleAvoid(RandomLightCycle):
    def update(self):
        RandomLightCycle.update(self)
        if self.destroyed:
            valid_directions = []
            if self.direction == Direction.DOWN:
                if pygame.Surface.get_at(self.screen, (int(self.x-self.speed), int(self.y-self.speed))) == pygame.Color(0, 0, 0):
                    valid_directions.append(Direction.LEFT)
                if pygame.Surface.get_at(self.screen, (int(self.x+self.speed), int(self.y-self.speed))) == pygame.Color(0, 0, 0):
                    valid_directions.append(Direction.RIGHT)
                if len(valid_directions) > 0:                    
                    self.y -= self.speed
            if self.direction == Direction.UP:
                if pygame.Surface.get_at(self.screen, (int(self.x-self.speed), int(self.y+self.speed))) == pygame.Color(0, 0, 0):
                    valid_directions.append(Direction.LEFT)
                if pygame.Surface.get_at(self.screen, (int(self.x+self.speed), int(self.y+self.speed))) == pygame.Color(0, 0, 0):
                    valid_directions.append(Direction.RIGHT)
                if len(valid_directions) > 0:                    
                    self.y += self.speed            
            if self.direction == Direction.RIGHT:
                if pygame.Surface.get_at(self.screen, (int(self.x-self.speed), int(self.y+self.speed))) == pygame.Color(0, 0, 0):
                    valid_directions.append(Direction.DOWN)
                if pygame.Surface.get_at(self.screen, (int(self.x-self.speed), int(self.y-self.speed))) == pygame.Color(0, 0, 0):
                    valid_directions.append(Direction.UP)
                if len(valid_directions) > 0:                 
                    self.x -= self.speed
            if self.direction == Direction.LEFT:
                if pygame.Surface.get_at(self.screen, (int(self.x+self.speed), int(self.y+self.speed))) == pygame.Color(0, 0, 0):
                    valid_directions.append(Direction.DOWN)
                if pygame.Surface.get_at(self.screen, (int(self.x+self.speed), int(self.y-self.speed))) == pygame.Color(0, 0, 0):
                    valid_directions.append(Direction.UP)
                if len(valid_directions) > 0:                 
                    self.x += self.speed
            if len(valid_directions) > 0:
                self.destroyed = False
                self.direction = random.choice(valid_directions)
                self.move()