#!/usr/bin/env python
import pygame, math, sys, os, random, pygame_gui
from pygame.locals import *
from AI.randomlightcycleavoid import RandomLightCycleAvoid
from lightcycle import Lightcycle
from direction import Direction
from AI.randomlightcycle import RandomLightCycle

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SPEED = 5
SIZE = 5
BORDER = pygame.Color(255,0,255)
P1COLOR = pygame.Color(255,0,0)
P2COLOR = pygame.Color(0,0,255)
P3COLOR = pygame.Color(0,255,0)
P4COLOR = pygame.Color(255,255, 0)
P1STARTX, P1STARTY = 0, HEIGHT/2
P2STARTX, P2STARTY = WIDTH-SIZE, HEIGHT/2
P3STARTX, P3STARTY = WIDTH/2,0
P4STARTX, P4STARTY = WIDTH/2,HEIGHT-SIZE

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tron Lightcycles")
clock = pygame.time.Clock()
manager = pygame_gui.UIManager((WIDTH, HEIGHT), theme_path="theme.json")

playerchoices = ("Human", "None", "Pure Random", "Random with Avoidance")


def init(player1type: str, player2type: str, player3type: str, player4type: str):
    global lightcycles
    lightcycles = []

    WIN.fill((0, 0, 0)) # Fill with black
    pygame.draw.rect(pygame.display.get_surface(), BORDER, Rect((0,0),(WIDTH,HEIGHT)),SIZE)

    if player1type == playerchoices[0]:
        lightcycles.append(Lightcycle(P1STARTX,P1STARTY,SPEED,Direction.RIGHT,P1COLOR, SIZE))
        lightcycles[-1].map_keys(K_w, K_s,K_a,K_d)
    elif player1type == playerchoices[2]:
        lightcycles.append(RandomLightCycle(P1STARTX,P1STARTY,SPEED,Direction.RIGHT,P1COLOR, SIZE))
    elif player1type == playerchoices[3]:
        lightcycles.append(RandomLightCycleAvoid(P1STARTX,P1STARTY,SPEED,Direction.RIGHT,P1COLOR, SIZE))

    if player2type == playerchoices[0]:
        lightcycles.append(Lightcycle(P2STARTX,P2STARTY,SPEED,Direction.LEFT,P2COLOR, SIZE))
        lightcycles[-1].map_keys(K_UP,K_DOWN,K_LEFT,K_RIGHT)    
    elif player2type == playerchoices[2]:
        lightcycles.append(RandomLightCycle(P2STARTX,P2STARTY,SPEED,Direction.LEFT,P2COLOR, SIZE))
    elif player2type == playerchoices[3]:
        lightcycles.append(RandomLightCycleAvoid(P2STARTX,P2STARTY,SPEED,Direction.LEFT,P2COLOR, SIZE))

    if player3type == playerchoices[0]:
        lightcycles.append(Lightcycle(P3STARTX,P3STARTY,SPEED,Direction.DOWN,P3COLOR, SIZE))
        lightcycles[-1].map_keys(K_t,K_g,K_f,K_h)    
    elif player3type == playerchoices[2]:
        lightcycles.append(RandomLightCycle(P3STARTX,P3STARTY,SPEED,Direction.DOWN,P3COLOR, SIZE))
    elif player3type == playerchoices[3]:
        lightcycles.append(RandomLightCycleAvoid(P3STARTX,P3STARTY,SPEED,Direction.DOWN,P3COLOR, SIZE))

    if player4type == playerchoices[0]:
        lightcycles.append(Lightcycle(P4STARTX,P4STARTY,SPEED,Direction.UP,P4COLOR, SIZE))
        lightcycles[-1].map_keys(K_i,K_k,K_j,K_l)    
    elif player4type == playerchoices[2]:
        lightcycles.append(RandomLightCycle(P4STARTX,P4STARTY,SPEED,Direction.UP,P4COLOR, SIZE))
    elif player4type == playerchoices[3]:
        lightcycles.append(RandomLightCycleAvoid(P4STARTX,P4STARTY,SPEED,Direction.UP,P4COLOR, SIZE))    

def main():

    while 1:
        get_options()
        #play_game()

def get_options():
    player1Label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((100, 100), (150, 50)),text="Player 1 Selection", manager=manager)
    player1Choice = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((250, 100), (200, 50)),options_list=playerchoices, starting_option="Human", manager=manager)
    player1NameLabel = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((450, 100), (150, 50)),text="Player 1 Name", manager=manager)
    player1NameTextBox = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((600, 100), (150, 50)),initial_text="Player 1", manager=manager)
    player1NameTextBox.set_text_length_limit(15)

    player2Label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((100, 150), (150, 50)),text="Player 2 Selection", manager=manager)
    player2Choice = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((250, 150), (200, 50)),options_list=playerchoices, starting_option="Random with Avoidance", manager=manager)
    player2NameLabel = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((450, 150), (150, 50)),text="Player 2 Name", manager=manager)
    player2NameTextBox = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((600, 150), (150, 50)),initial_text="Player 2", manager=manager)
    player2NameTextBox.set_text_length_limit(15)

    player3Label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((100, 200), (150, 50)),text="Player 3 Selection", manager=manager)
    player3Choice = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((250, 200), (200, 50)),options_list=playerchoices, starting_option="Random with Avoidance", manager=manager)
    player3NameLabel = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((450, 200), (150, 50)),text="Player 2 Name", manager=manager)
    player3NameTextBox = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((600, 200), (150, 50)),initial_text="Player 3", manager=manager)
    player3NameTextBox.set_text_length_limit(15)

    player4Label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((100, 250), (150, 50)),text="Player 4 Selection", manager=manager)
    player4Choice = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((250, 250), (200, 50)),options_list=playerchoices, starting_option="Random with Avoidance", manager=manager)
    player4NameLabel = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((450, 250), (150, 50)),text="Player 4 Name", manager=manager)
    player4NameTextBox = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((600, 250), (150, 50)),initial_text="Player 4", manager=manager)
    player4NameTextBox.set_text_length_limit(15)
    
    launch_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((WIDTH/2-50, HEIGHT-100), (150, 50)),
                                                text='Launch Game',
                                                manager=manager)
    done = False
    while not done:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game()
            manager.process_events(event)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == launch_button:
                    done = True      
        manager.update(time_delta)
        WIN.fill((0, 0, 0))
        manager.draw_ui(WIN)
        pygame.display.update() # Update the display

    init(player1Choice.selected_option[0], player2Choice.selected_option[0], 
         player3Choice.selected_option[0], player4Choice.selected_option[0])
    play_game()

def play_game():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game()

        clock.tick(30) #30 fps

        if pygame.key.get_pressed()[K_ESCAPE]: end_game()

        for lightcycle in lightcycles:
            lightcycle.update()
            lightcycle.draw()


        pygame.display.update() # Update the display



def end_game():
    print('Thanks for playing')
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
