#!/usr/bin/env python
import pygame
import pygame_gui
import sys
from pygame.locals import *

from AI.hunter import HunterLightCycle
from AI.randomlightcycle import RandomLightCycle
from AI.randomlightcycleavoid import RandomLightCycleAvoid
from AI.nonelightcyle import NoneLightcycle
from AI.zigzag import ZigZagLightcycle
from AI.zigzagavoid import ZigZagAvoidLightcycle
from AI.shield import ShieldLightcycle
from direction import Direction
from lightcycle import Lightcycle

from optionwindow import OptionWindow

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SPEED = 5
SIZE = 5
VERTICALOFFSET = 30
BORDER = pygame.Color(255,0,255)
P1COLOR = pygame.Color(255,0,0)
P2COLOR = pygame.Color(0,0,255)
P3COLOR = pygame.Color(0,255,0)
P4COLOR = pygame.Color(255,255, 0)
P1STARTX, P1STARTY = int(0), int(HEIGHT/2+VERTICALOFFSET)
P2STARTX, P2STARTY = int(WIDTH-SIZE), int(HEIGHT/2+VERTICALOFFSET)
P3STARTX, P3STARTY = int(WIDTH/2),int(VERTICALOFFSET)
P4STARTX, P4STARTY = int(WIDTH/2),int(HEIGHT-SIZE)
STARTINGVALUES = [
    [P1STARTX,P1STARTY,SPEED,Direction.RIGHT,P1COLOR, SIZE],
    [P2STARTX,P2STARTY,SPEED,Direction.LEFT,P2COLOR, SIZE],
    [P3STARTX,P3STARTY,SPEED,Direction.DOWN,P3COLOR, SIZE],
    [P4STARTX,P4STARTY,SPEED,Direction.UP,P4COLOR, SIZE]
]

KEYPRESSES = [
    [K_w, K_s,K_a,K_d],
    [K_UP,K_DOWN,K_LEFT,K_RIGHT],
    [K_t,K_g,K_f,K_h],
    [K_i,K_k,K_j,K_l]
]
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tron Lightcycles")
clock = pygame.time.Clock()
manager = pygame_gui.UIManager((WIDTH, HEIGHT), theme_path="theme.json")
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

player_choices = ["Human", "None", "Pure Random", "Random with Avoidance", "Zig Zag", "Zig Zag Avoid", "Shield", "Hunter"]
player_names = ["Player 1", "Player 2", "Player 3", "Player 4"]
player_joysticks = [None, None, None, None]

def create_lightcyle(lightcycle_type: str, player_number: int) -> Lightcycle:
    temp = NoneLightcycle()
    if lightcycle_type == player_choices[0]:
        temp = Lightcycle(STARTINGVALUES[player_number - 1][0], STARTINGVALUES[player_number - 1][1],
                          STARTINGVALUES[player_number - 1][2], STARTINGVALUES[player_number - 1][3],
                          STARTINGVALUES[player_number - 1][4], STARTINGVALUES[player_number - 1][5])
        temp.map_keys(KEYPRESSES[player_number - 1][0], KEYPRESSES[player_number - 1][1],
                      KEYPRESSES[player_number - 1][2], KEYPRESSES[player_number - 1][3])
        if player_joysticks[player_number - 1] is not None: temp.set_joystick(player_joysticks[player_number - 1])
    elif lightcycle_type == player_choices[2]:
        temp = RandomLightCycle(STARTINGVALUES[player_number - 1][0], STARTINGVALUES[player_number - 1][1],
                                STARTINGVALUES[player_number - 1][2], STARTINGVALUES[player_number - 1][3],
                                STARTINGVALUES[player_number - 1][4], STARTINGVALUES[player_number - 1][5])
    elif lightcycle_type == player_choices[3]:
        temp = RandomLightCycleAvoid(STARTINGVALUES[player_number - 1][0], STARTINGVALUES[player_number - 1][1],
                                     STARTINGVALUES[player_number - 1][2], STARTINGVALUES[player_number - 1][3],
                                     STARTINGVALUES[player_number - 1][4], STARTINGVALUES[player_number - 1][5])
    elif lightcycle_type == player_choices[4]:
        temp = ZigZagLightcycle(STARTINGVALUES[player_number - 1][0], STARTINGVALUES[player_number - 1][1],
                                STARTINGVALUES[player_number - 1][2], STARTINGVALUES[player_number - 1][3],
                                STARTINGVALUES[player_number - 1][4], STARTINGVALUES[player_number - 1][5])
    elif lightcycle_type == player_choices[5]:
        temp = ZigZagAvoidLightcycle(STARTINGVALUES[player_number - 1][0], STARTINGVALUES[player_number - 1][1],
                                     STARTINGVALUES[player_number - 1][2], STARTINGVALUES[player_number - 1][3],
                                     STARTINGVALUES[player_number - 1][4], STARTINGVALUES[player_number - 1][5])
    elif lightcycle_type == player_choices[6]:
        temp = ShieldLightcycle(STARTINGVALUES[player_number - 1][0], STARTINGVALUES[player_number - 1][1],
                                STARTINGVALUES[player_number - 1][2], STARTINGVALUES[player_number - 1][3],
                                STARTINGVALUES[player_number - 1][4], STARTINGVALUES[player_number - 1][5])
    elif lightcycle_type == player_choices[7]:
        temp = HunterLightCycle(STARTINGVALUES[player_number - 1][0], STARTINGVALUES[player_number - 1][1],
                                STARTINGVALUES[player_number - 1][2], STARTINGVALUES[player_number - 1][3],
                                STARTINGVALUES[player_number - 1][4], STARTINGVALUES[player_number - 1][5])
    return temp


# noinspection PyGlobalUndefined
def init(player1type: str, player2type: str, player3type: str, player4type: str):
    global lightcycles
    lightcycles = []
    lightcycles.clear()

    WIN.fill((0, 0, 0)) # Fill with black
    pygame.draw.rect(pygame.display.get_surface(), BORDER, Rect((0,VERTICALOFFSET),(WIDTH,HEIGHT-VERTICALOFFSET)),SIZE)

    lightcycles.append(create_lightcyle(player1type,1))    
    lightcycles.append(create_lightcyle(player2type,2))    
    lightcycles.append(create_lightcyle(player3type,3))    
    lightcycles.append(create_lightcyle(player4type,4))

    if player1type == player_choices[7]:
        lightcycles[0].assign_targets([lightcycles[1], lightcycles[2], lightcycles[3]])
    if player2type == player_choices[7]:
        lightcycles[1].assign_targets([lightcycles[0], lightcycles[2], lightcycles[3]])
    if player3type == player_choices[7]:
        lightcycles[2].assign_targets([lightcycles[0], lightcycles[1], lightcycles[3]])
    if player4type == player_choices[7]:
        lightcycles[3].assign_targets([lightcycles[0], lightcycles[1], lightcycles[2]])

def main():

    while 1:
        get_options()
        #play_game()


def get_options():
    manager.clear_and_reset()

    default_ai = "Hunter"
    joystick_text = ["None"]
    for joystick in joysticks:
        joystick_text.append(joystick.get_name())
    #Create all possible joystick options
        

    window_height = (HEIGHT-30)/4
    option_windows = [OptionWindow(rect=pygame.Rect((0, 0), (WIDTH, window_height)),
                                   manager=manager, player_number=1,
                                   player_choices=player_choices,
                                   initial_name=player_names[0], starting_player_type="Human"),
                      OptionWindow(rect=pygame.Rect((0, window_height), (WIDTH, window_height)),
                                   manager=manager, player_number=2,
                                   player_choices=player_choices,
                                   initial_name=player_names[1], starting_player_type=default_ai),
                      OptionWindow(rect=pygame.Rect((0, window_height * 2), (WIDTH, window_height)),
                                   manager=manager, player_number=3,
                                   player_choices=player_choices,
                                   initial_name=player_names[2], starting_player_type=default_ai),
                      OptionWindow(rect=pygame.Rect((0, window_height * 3), (WIDTH, window_height)),
                                   manager=manager, player_number=4,
                                   player_choices=player_choices,
                                   initial_name=player_names[3], starting_player_type=default_ai)]

    if pygame.joystick.get_count() > 0:
        for window in option_windows: window.add_joystick(joystick_text=joystick_text)
    launch_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, -30), (150, 30)),
                                                text='Launch Game',
                                                anchors={'centerx': 'centerx','bottom': 'bottom'},
                                                manager=manager)
    done = False
    while not done:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game()
            if event.type == pygame.JOYDEVICEADDED or event.type == pygame.JOYDEVICEREMOVED:
                    for element in option_windows: element.remove_joystick()
                    joystick_text = ["None"]
                    for x in range(pygame.joystick.get_count()):
                        joysticks.append(pygame.joystick.Joystick(x))
                    for joystick in joysticks:
                        joystick_text.append(joystick.get_name())
                    if pygame.joystick.get_count() > 0:
                        for window in option_windows: window.add_joystick(joystick_text=joystick_text)
            manager.process_events(event)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == launch_button:
                    done = True
            if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if pygame.joystick.get_count() > 0:
                    for window in option_windows:
                        if event.ui_element != window.get_joystick_dropdown():
                            window.add_joystick(joystick_text=joystick_text)
        manager.update(time_delta)
        WIN.fill((0, 0, 0))
        manager.draw_ui(WIN)
        pygame.display.update() # Update the display

    for i in range(0,4):
        player_names[i] = option_windows[i].get_name()
    if pygame.joystick.get_count() > 0:
        for i in range(0,4):
            if option_windows[i].get_joystick() != "None":
                for joystick in joysticks:
                    if joystick.get_name() == option_windows[i].get_joystick():
                        player_joysticks[i] = joystick


    init(option_windows[0].get_player_type(), option_windows[1].get_player_type(),
         option_windows[2].get_player_type(), option_windows[3].get_player_type())
    play_game()

def play_game():
    manager.clear_and_reset()
    p1label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 0), (150, VERTICALOFFSET)), text=player_names[0], manager=manager)
    p2label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((200, 0), (150, VERTICALOFFSET)), text=player_names[1], manager=manager)
    p3label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((400, 0), (150, VERTICALOFFSET)), text=player_names[2], manager=manager)
    p4label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((600, 0), (150, VERTICALOFFSET)), text=player_names[3], manager=manager)

    while 1:
        #Clear only the display area
        pygame.draw.rect(pygame.display.get_surface(),Color(0,0,0), Rect((0,0),(WIDTH,VERTICALOFFSET)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game()
            manager.process_events(event)                   

        time_delta = clock.tick(30)/1000.0

        if pygame.key.get_pressed()[K_ESCAPE]: end_game()

        manager.update(time_delta)        

        alive_count = 0
        for lightcycle in lightcycles:
            lightcycle.update()
            lightcycle.draw()
            if not lightcycle.is_destroyed(): alive_count+=1
        
        if lightcycles[0].is_destroyed():
            p1label.set_text("Destroyed")
        if lightcycles[1].is_destroyed():
            p2label.set_text("Destroyed")
        if lightcycles[2].is_destroyed():
            p3label.set_text("Destroyed")
        if lightcycles[3].is_destroyed():
            p4label.set_text("Destroyed")


        manager.draw_ui(WIN)
        pygame.display.update() # Update the display

        if alive_count <=1: game_over(alive_count)

def game_over(alive_count):
    manager.clear_and_reset()
    output = ""
    if alive_count == 0:
        output += "Aww, no winner!"
    else:
        i = 0
        for j in range(0,3):
            if not lightcycles[j].is_destroyed(): i = j
        output += f"Congratulations {player_names[i]}!!!!"
    
    congats_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 150), (-1, -1)), text=output,
                                                anchors={'centerx': 'centerx','top': 'top'},
                                                manager=manager)
    congats_text.set_text_scale(20.0) 
    congats_text.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR,params={'time_per_letter': 0.1} )  
    play_again = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 50), (-1,-1)), text="Would you like to play again?",
                                                anchors={'centerx': 'centerx','top': 'top',
                                                        'top_target': congats_text},
                                                manager=manager)   

    yes_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((-85, 100), (150, 50)),
                                                text='Yes',
                                                anchors={'centerx': 'centerx','top': 'top',
                                                         'top_target': play_again},
                                                manager=manager)
    no_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 0), (150, 50)),
                                                text='No',
                                                anchors={'left': 'left','bottom': 'bottom', 
                                                         'left_target':yes_button, 'bottom_target': yes_button},
                                                manager=manager)
    
    done = False
    while not done:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game()
            manager.process_events(event)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == yes_button:
                    done = True
                    get_options() 
                if event.ui_element == no_button:
                    done = True
                    end_game()                          
        manager.update(time_delta)
        congats_text.update_text_effect(time_delta)
        WIN.fill((0, 0, 0))
        manager.draw_ui(WIN)
        pygame.display.update() # Update the display    

def end_game():
    print('Thanks for playing')
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
