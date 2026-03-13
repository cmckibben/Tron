import pygame
import pygame_gui

class OptionWindow(pygame_gui.elements.ui_window.UIWindow):
    def __init__(self, rect,manager, player_number, player_choices, initial_name, starting_player_type="Human"):
        super(OptionWindow, self).__init__(rect=rect,manager=manager,window_display_title=f"Player {player_number}")
        self.manager = manager
        self.has_joystick=False
        self.selectionLabel = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 0), (-1, 30)), 
                                text=f"Player {player_number} Selection",
                                manager=manager, container=self,
                                anchors={'top':'top','left':'left'})
        self.playerChoice = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((10, 0), (200, 30)),
                                options_list=player_choices, 
                                starting_option=starting_player_type, 
                                manager=manager, container=self,
                                anchors={'left': 'left','bottom': 'bottom', 
                                    'left_target':self.selectionLabel, 
                                    'bottom_target': self.selectionLabel})
        self.nameLabel = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((10, 0), (-1, 30)), 
                                text=f"Player {player_number} Name", 
                                manager=manager, container=self,
                                anchors={'left': 'left','bottom': 'bottom', 
                                    'left_target':self.playerChoice, 'bottom_target': self.playerChoice})
        self.nameTextBox = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((10, 0), (150, 30)),
                                initial_text=initial_name, 
                                manager=manager, container=self,
                                anchors={'left': 'left','bottom': 'bottom', 
                                    'left_target':self.nameLabel, 'bottom_target': self.nameLabel})
        self.nameTextBox.set_text_length_limit(15)
    
    def addJoystick(self, joysticktext):
        if self.has_joystick == True: self.joystickDropdown.kill()
        self.has_joystick = True
        self.joystickDropdown = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((10, 5), (200, 30)), 
                                    options_list=joysticktext, starting_option="None", 
                                    manager=self.manager, container = self, 
                                    anchors={'left': 'left','top': 'top', 
                                    'left_target':self.selectionLabel, 'top_target': self.selectionLabel})
    def removeJoystick(self):
        if self.has_joystick: self.joystickDropdown.kill()
        self.has_joystick = False

    def getName(self) -> str:
        return self.nameTextBox.get_text()
    
    def getPlayerType(self) -> str:
       return self.playerChoice.selected_option[0]
    
    def getJoystick(self) -> str:
        if self.has_joystick:
            return self.joystickDropdown.selected_option[0]
        else: 
            return ""
        
    def on_close_window_button_pressed(self):
        self.hidden = True
        super.hide()
    
    def getJoystickDropdown(self):
        return self.joystickDropdown