import random
import pygame
from direction import Direction
from lightcycle import Lightcycle


class HunterLightCycle(Lightcycle):
    def __init__(self, x: int, y: int, speed: int, direction: Direction, color: pygame.Color, size: int):
        Lightcycle.__init__(self,x,y,speed,direction,color,size)
        self.target_index = None
        self.targets = None

    def assign_targets(self, targets: list[Lightcycle]):
        self.targets = targets
        self.target_index = random.randint(0, len(self.targets) - 1)
    def update(self):
        self.move()
        if pygame.Surface.get_at(self.screen, (int(self.x), int(self.y))) != pygame.Color(0, 0, 0):
            self.destroyed = True
        else:
            #check if target is destroyed and then pick another
            if self.targets[self.target_index].is_destroyed():
                self.targets.pop(self.target_index)
                if len(self.targets) > 0:
                    self.target_index = random.randint(0, len(self.targets) - 1)
            
            if len(self.targets) > 0:
                #attempt to get closer to target
                distance_x = abs(self.x - self.targets[self.target_index].x)
                distance_y = abs(self.y - self.targets[self.target_index].y)

                if distance_x > distance_y:
                    if self.x > self.targets[self.target_index].x and self.direction != Direction.RIGHT:
                        if pygame.Surface.get_at(self.screen, (int(self.x-self.speed), int(self.y))) == pygame.Color(0, 0, 0):
                            self.direction = Direction.LEFT
                    elif self.direction != Direction.LEFT:
                        if pygame.Surface.get_at(self.screen, (int(self.x+self.speed), int(self.y))) == pygame.Color(0, 0, 0):
                            self.direction = Direction.RIGHT
                else:
                    if self.y > self.targets[self.target_index].y and self.direction != Direction.DOWN:
                        if pygame.Surface.get_at(self.screen, (int(self.x), int(self.y-self.speed))) == pygame.Color(0, 0, 0):
                            self.direction = Direction.UP
                    elif self.direction != Direction.UP:
                        if pygame.Surface.get_at(self.screen, (int(self.x), int(self.y+self.speed))) == pygame.Color(0, 0, 0):
                            self.direction = Direction.DOWN


    
        #Avoid

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
            else: 
                self.speed = 0
