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

playerchoices = ["Human", "None", "Pure Random", "Random with Avoidance", "Zig Zag", "Zig Zag Avoid", "Shield", "Hunter"]
playerNames = ["Player 1", "Player 2", "Player 3", "Player 4"]
playerJoysticks = [None, None, None, None]

def create_lightcyle(type: str, playernumber: int) -> Lightcycle:
    temp = NoneLightcycle()
    if type == playerchoices[0]:
        temp = Lightcycle(STARTINGVALUES[playernumber -1][0], STARTINGVALUES[playernumber -1][1],
                          STARTINGVALUES[playernumber -1][2], STARTINGVALUES[playernumber -1][3],
                          STARTINGVALUES[playernumber -1][4], STARTINGVALUES[playernumber -1][5])
        temp.map_keys(KEYPRESSES[playernumber -1][0], KEYPRESSES[playernumber -1][1],
                      KEYPRESSES[playernumber -1][2], KEYPRESSES[playernumber -1][3])
        if playerJoysticks[playernumber-1] is not None: temp.set_joystick(playerJoysticks[playernumber-1])
    elif type == playerchoices[2]:
        temp = RandomLightCycle(STARTINGVALUES[playernumber -1][0], STARTINGVALUES[playernumber -1][1],
                          STARTINGVALUES[playernumber -1][2], STARTINGVALUES[playernumber -1][3],
                          STARTINGVALUES[playernumber -1][4], STARTINGVALUES[playernumber -1][5])
    elif type == playerchoices[3]:
        temp = RandomLightCycleAvoid(STARTINGVALUES[playernumber -1][0], STARTINGVALUES[playernumber -1][1],
                          STARTINGVALUES[playernumber -1][2], STARTINGVALUES[playernumber -1][3],
                          STARTINGVALUES[playernumber -1][4], STARTINGVALUES[playernumber -1][5])
    elif type == playerchoices[4]:
        temp = ZigZagLightcycle(STARTINGVALUES[playernumber -1][0], STARTINGVALUES[playernumber -1][1],
                          STARTINGVALUES[playernumber -1][2], STARTINGVALUES[playernumber -1][3],
                          STARTINGVALUES[playernumber -1][4], STARTINGVALUES[playernumber -1][5])
    elif type == playerchoices[5]:
        temp = ZigZagAvoidLightcycle(STARTINGVALUES[playernumber -1][0], STARTINGVALUES[playernumber -1][1],
                          STARTINGVALUES[playernumber -1][2], STARTINGVALUES[playernumber -1][3],
                          STARTINGVALUES[playernumber -1][4], STARTINGVALUES[playernumber -1][5])  
    elif type == playerchoices[6]:
        temp = ShieldLightcycle(STARTINGVALUES[playernumber -1][0], STARTINGVALUES[playernumber -1][1],
                          STARTINGVALUES[playernumber -1][2], STARTINGVALUES[playernumber -1][3],
                          STARTINGVALUES[playernumber -1][4], STARTINGVALUES[playernumber -1][5])    
    elif type == playerchoices[7]:
        temp = HunterLightCycle(STARTINGVALUES[playernumber -1][0], STARTINGVALUES[playernumber -1][1],
                          STARTINGVALUES[playernumber -1][2], STARTINGVALUES[playernumber -1][3],
                          STARTINGVALUES[playernumber -1][4], STARTINGVALUES[playernumber -1][5])                      
    return temp
def init(player1type: str, player2type: str, player3type: str, player4type: str):
    global lightcycles
    lightcycles = []

    WIN.fill((0, 0, 0)) # Fill with black
    pygame.draw.rect(pygame.display.get_surface(), BORDER, Rect((0,VERTICALOFFSET),(WIDTH,HEIGHT-VERTICALOFFSET)),SIZE)

    lightcycles.append(create_lightcyle(player1type,1))    
    lightcycles.append(create_lightcyle(player2type,2))    
    lightcycles.append(create_lightcyle(player3type,3))    
    lightcycles.append(create_lightcyle(player4type,4))

    if player1type == playerchoices[7]:    
        lightcycles[0].assignTargets([lightcycles[1], lightcycles[2], lightcycles[3]])
    if player2type == playerchoices[7]:    
        lightcycles[1].assignTargets([lightcycles[0], lightcycles[2], lightcycles[3]])
    if player3type == playerchoices[7]:    
        lightcycles[2].assignTargets([lightcycles[0], lightcycles[1], lightcycles[3]])
    if player4type == playerchoices[7]:    
        lightcycles[3].assignTargets([lightcycles[0], lightcycles[1], lightcycles[2]])

def main():

    while 1:
        get_options()
        #play_game()

def get_options():
    manager.clear_and_reset()

    defaultAI = "Hunter"
    joysticktext = ["None"]
    for joystick in joysticks:
        joysticktext.append(joystick.get_name())
    #Create all possible joystick options
    joystickSelectors = []
    if pygame.joystick.get_count() > 0:
        joystickSelectors.append(pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((100, 150), (200, 50)), options_list=joysticktext, starting_option="None", manager=manager))
        joystickSelectors.append(pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((100, 250), (200, 50)), options_list=joysticktext, starting_option="None", manager=manager))
        joystickSelectors.append(pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((100, 350), (200, 50)), options_list=joysticktext, starting_option="None", manager=manager))
        joystickSelectors.append(pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((100, 450), (200, 50)), options_list=joysticktext, starting_option="None", manager=manager))
        

    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((100, 100), (150, 50)), text="Player 1 Selection",
                                manager=manager)
    player1Choice = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((250, 100), (200, 50)),options_list=playerchoices, starting_option="Human", manager=manager)
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((450, 100), (150, 50)), text="Player 1 Name", manager=manager)
    player1NameTextBox = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((600, 100), (150, 50)),initial_text=playerNames[0], manager=manager)
    player1NameTextBox.set_text_length_limit(15)

    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((100, 200), (150, 50)), text="Player 2 Selection",
                                manager=manager)
    player2Choice = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((250, 200), (200, 50)),options_list=playerchoices, starting_option=defaultAI, manager=manager)
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((450, 200), (150, 50)), text="Player 2 Name", manager=manager)
    player2NameTextBox = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((600, 200), (150, 50)),initial_text=playerNames[1], manager=manager)
    player2NameTextBox.set_text_length_limit(15)

    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((100, 300), (150, 50)), text="Player 3 Selection",
                                manager=manager)
    player3Choice = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((250, 300), (200, 50)),options_list=playerchoices, starting_option=defaultAI, manager=manager)
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((450, 300), (150, 50)), text="Player 3 Name", manager=manager)
    player3NameTextBox = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((600, 300), (150, 50)),initial_text=playerNames[2], manager=manager)
    player3NameTextBox.set_text_length_limit(15)

    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((100, 400), (150, 50)), text="Player 4 Selection",
                                manager=manager)
    player4Choice = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((250, 400), (200, 50)),options_list=playerchoices, starting_option=defaultAI, manager=manager)
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((450, 400), (150, 50)), text="Player 4 Name", manager=manager)
    player4NameTextBox = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((600, 400), (150, 50)),initial_text=playerNames[3], manager=manager)
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
            if event.type == pygame.JOYDEVICEADDED or event.type == pygame.JOYDEVICEREMOVED:
                    for element in joystickSelectors: element.kill()
                    joystickSelectors.clear()
                    joysticktext = ["None"]
                    joysticks.clear()
                    for x in range(pygame.joystick.get_count()):
                        joysticks.append(pygame.joystick.Joystick(x))
                    for joystick in joysticks:
                        joysticktext.append(joystick.get_name())
                    if pygame.joystick.get_count() > 0:
                        joystickSelectors.append(pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((100, 150), (200, 50)), options_list=joysticktext, starting_option="None", manager=manager))
                        joystickSelectors.append(pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((100, 250), (200, 50)), options_list=joysticktext, starting_option="None", manager=manager))
                        joystickSelectors.append(pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((100, 350), (200, 50)), options_list=joysticktext, starting_option="None", manager=manager))
                        joystickSelectors.append(pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((100, 450), (200, 50)), options_list=joysticktext, starting_option="None", manager=manager))

            manager.process_events(event)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == launch_button:
                    done = True
            if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if pygame.joystick.get_count() > 0:
                    if event.ui_element == joystickSelectors[0]:
                        if joystickSelectors[1].selected_option[0] == joystickSelectors[0].selected_option[0]:
                            joystickSelectors[1] = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((100, 250), (200, 50)), options_list=joysticktext, starting_option="None", manager=manager)
                        if joystickSelectors[2].selected_option[0] == joystickSelectors[0].selected_option[0]:
                            joystickSelectors[2] = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((100, 350), (200, 50)), options_list=joysticktext, starting_option="None", manager=manager)
                        if joystickSelectors[3].selected_option[0] == joystickSelectors[0].selected_option[0]:
                            joystickSelectors[3] = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((100, 450), (200, 50)), options_list=joysticktext, starting_option="None", manager=manager)

                    elif event.ui_element == joystickSelectors[1]:
                        if joystickSelectors[0].selected_option[0] == joystickSelectors[1].selected_option[0]:
                            joystickSelectors[0] = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((100, 150), (200, 50)), options_list=joysticktext, starting_option="None", manager=manager)
                        if joystickSelectors[2].selected_option[0] == joystickSelectors[1].selected_option[0]:
                            joystickSelectors[2] = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((100, 350), (200, 50)), options_list=joysticktext, starting_option="None", manager=manager)
                        if joystickSelectors[3].selected_option[0] == joystickSelectors[1].selected_option[0]:
                            joystickSelectors[3] = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((100, 450), (200, 50)), options_list=joysticktext, starting_option="None", manager=manager)
                    elif event.ui_element == joystickSelectors[2]:
                        if joystickSelectors[0].selected_option[0] == joystickSelectors[2].selected_option[0]:
                            joystickSelectors[0] = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((100, 150), (200, 50)), options_list=joysticktext, starting_option="None", manager=manager)
                        if joystickSelectors[1].selected_option[0] == joystickSelectors[2].selected_option[0]:
                            joystickSelectors[1] = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((100, 250), (200, 50)), options_list=joysticktext, starting_option="None", manager=manager)
                        if joystickSelectors[3].selected_option[0] == joystickSelectors[2].selected_option[0]:
                            joystickSelectors[3] = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((100, 450), (200, 50)), options_list=joysticktext, starting_option="None", manager=manager)

                    elif event.ui_element == joystickSelectors[3]:
                        if joystickSelectors[0].selected_option[0] == joystickSelectors[3].selected_option[0]:
                            joystickSelectors[0] = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((100, 150), (200, 50)), options_list=joysticktext, starting_option="None", manager=manager)
                        if joystickSelectors[1].selected_option[0] == joystickSelectors[3].selected_option[0]:
                            joystickSelectors[1] = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((100, 250), (200, 50)), options_list=joysticktext, starting_option="None", manager=manager)
                        if joystickSelectors[2].selected_option[0] == joystickSelectors[3].selected_option[0]:
                            joystickSelectors[2] = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((100, 350), (200, 50)), options_list=joysticktext, starting_option="None", manager=manager)
        manager.update(time_delta)
        WIN.fill((0, 0, 0))
        manager.draw_ui(WIN)
        pygame.display.update() # Update the display

    playerNames[0] = player1NameTextBox.get_text()
    playerNames[1] = player2NameTextBox.get_text()
    playerNames[2] = player3NameTextBox.get_text()
    playerNames[3] = player4NameTextBox.get_text()

    if pygame.joystick.get_count() > 0:
        for i in range (0,4):
            if joystickSelectors[i].selected_option[0] != "None":
                for joystick in joysticks:
                    if joystick.get_name() == joystickSelectors[i].selected_option[0]:
                        playerJoysticks[i] = joystick

    init(player1Choice.selected_option[0], player2Choice.selected_option[0], 
         player3Choice.selected_option[0], player4Choice.selected_option[0])
    play_game()

def play_game():
    manager.clear_and_reset()
    p1label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 0), (150, VERTICALOFFSET)), text=playerNames[0], manager=manager)
    p2label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((200, 0), (150, VERTICALOFFSET)), text=playerNames[1], manager=manager)
    p3label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((400, 0), (150, VERTICALOFFSET)), text=playerNames[2], manager=manager)
    p4label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((600, 0), (150, VERTICALOFFSET)), text=playerNames[3], manager=manager)

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

        aliveCount = 0
        for lightcycle in lightcycles:
            lightcycle.update()
            lightcycle.draw()
            if not lightcycle.is_destroyed(): aliveCount+=1
        
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

        if aliveCount <=1: game_over(aliveCount)

def game_over(aliveCount):
    manager.clear_and_reset()
    output = ""
    if aliveCount == 0:
        output += "Aww, no winner!"
    else:
        i = 0
        for j in range(0,3):
            if not lightcycles[j].is_destroyed(): i = j
        output += f"Congratulations {playerNames[i]}!!!!"
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((100, 100), (WIDTH-100, 30)), text=output,
                                manager=manager)   
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((100, 150), (WIDTH-100,30)), text="Would you like to play again?",
                                manager=manager)   
    yes_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((WIDTH/2-150, HEIGHT-100), (150, 50)),
                                                text='Yes',
                                                manager=manager)
    no_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((WIDTH/2+150, HEIGHT-100), (150, 50)),
                                                text='No',
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
        WIN.fill((0, 0, 0))
        manager.draw_ui(WIN)
        pygame.display.update() # Update the display    

def end_game():
    print('Thanks for playing')
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
