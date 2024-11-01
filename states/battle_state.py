import pygame
import random
import math
import sys
from states.state_manager import *
from states.managers.Sprite_Manager import *
from states.managers.Input_Manager import *
from states.managers.Character_Manager import *
from states.managers.Audio_Manager import *

# START PYGAME WOOOOO pygame

class Battle(State):
    def __init__(self, game):
        State.__init__(self, game)
        # Initalizes Variables from Classes
    
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if timer.is_player_turn == True:
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.KEYDOWN and spell.enemy_selection_state == False:
                    key = pygame.key.name(event.key)
                    keyboard.key_press_action(key)

                elif event.type == pygame.MOUSEBUTTONDOWN and spell.enemy_selection_state == True:
                    spell.targeted_enemy(mouse_pos)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if keyboard.end_turn_button.is_clicked() == True:
                        timer.timer_duration = 1

    def render(self, display):
        battle_interface()
        display.blit(game_window, (0,0)) 

pygame.init()
# Create Display Window For Game
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

game_window = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Keyboard Battle")


# Set Colors used for Textures
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (130, 130, 130)
RED = (255, 0, 0)
KEY_PURPLE = (255, 0, 255)

# Set fonts Used for Text
font = pygame.font.Font('Assets/Fonts/minercraftory/Minercraftory.ttf', 20)
big_font = pygame.font.Font('Assets/Fonts/minercraftory/Minercraftory.ttf', 40)

# Get Sprite Sheet for Keyboard
keyboard_sprite_sheet_image = get_image('Assets/SimpleKeys/Classic/Light/Keys_Sprite_Sheet.png', 6)
keyboard_sprite_sheet = KeyboardSprites(keyboard_sprite_sheet_image)
keyboard_sprite_sheet.get_keyboard_sprites()

# Set Layers Class
class Layers:
    def __init__(self):
        self.background_layer = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.combat_layer = character.combat_layer
        self.selection_layer = character.selection_layer
        self.interface_layer = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.keyboard_layer = keyboard_sprite_sheet.keyboard_default_sprite()
        self.popup_layer = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))

# Define the Functions for keyboard updates
class Valid_Dictionary:
    def __init__(self):
        self.shared_dictionary = open('states/battle_data/SpellBook.txt', "r")
        self.valid_words = self.shared_dictionary.read() 
        self.valid_word_list = self.valid_words.split("\n")
        self.shared_dictionary.close()
    
    def validWordChecker(self, current_typed_word:str):
        if current_typed_word in self.valid_word_list:
            return True
        else:
            return False

class Timer:
    def __init__(self):
        self.timer_duration = 30  # seconds
        self.current_time = self.timer_duration
        self.is_player_turn = True
        self.start_ticks = pygame.time.get_ticks()
        self.center_x = 120
        self.center_y = 50
        self.radius = 30
        self.line_thickness = 5

    def update_time(self):
        self.seconds_passed = (pygame.time.get_ticks() - self.start_ticks) / 1000
        self.time_left = max(0, self.timer_duration - int(self.seconds_passed))
        angle = (self.time_left / self.timer_duration) * 2 * math.pi
        self.hand_x = self.center_x + self.radius * math.cos(-angle + math.pi / 2)
        self.hand_y = self.center_y + self.radius * math.sin(-angle + math.pi / 2)

        if self.time_left <= 0: # Turn switching
            if self.is_player_turn == True:
                self.time_left_text = big_font.render("ENEMY TURN", True, RED)
                layer.interface_layer.blit(self.time_left_text, (15, 15))
                update_game_screen()
                character.enemy_turn()
                update_game_screen()
                self.start_ticks = pygame.time.get_ticks()
                self.is_player_turn = False
                self.timer_duration = 1
            else: 
                self.timer_duration = 30
                self.is_player_turn = True
                keyboard.key_replenish()
                update_game_screen()
                clear_inputs()
                self.start_ticks = pygame.time.get_ticks()

    def draw(self):
        if self.is_player_turn == True:
            self.time_left_text = big_font.render(str(self.time_left), True, WHITE)
            layer.interface_layer.blit(self.time_left_text, (15, 15))
            pygame.draw.circle(layer.interface_layer, WHITE, (self.center_x, self.center_y), self.radius, self.line_thickness)
            pygame.draw.line(layer.interface_layer, RED, (self.center_x, self.center_y), (self.hand_x, self.hand_y), self.line_thickness)

class EndTurnButton:
    def __init__(self, x, y, width, height, text, font):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font = font 

        self.color = WHITE  # Black
        self.hover_color = RED  # Yellow
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.color = self.hover_color
        else:
            self.color = self.color  # Transparent

        pygame.draw.rect(screen, self.color, self.rect)  # Fill the rect with the color
        # Render the text and draw it centered on the button
        text_surface = self.font.render(str(self.text), True, BLACK)  # White text
        screen.blit(text_surface, (1400, 480))

    def is_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            return True
        return False

class Keyboard:
    def __init__(self):
        self.typed_text = ""
        self.cursor_position = 0
        self.max_character_count = 20
        self.valid_letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 
                              'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                              'z', 'x', 'c', 'v', 'b', 'n', 'm' ]
        self.key_state = 1 #1 is default 0 is pressed

        # Popup Messages
        self.no_letter_left = font.render("You Have None of this Character Left!", True, WHITE)
        self.no_character_left = font.render("You Have No Characters Left!", True, WHITE)   
        self.not_in_dictionary = font.render("Word Not in your Dictionary", True, WHITE)
        self.select_target = font.render("Please Select a Target", True, WHITE)

    def keyboard_amount_position(self):
        self.Key_Amount_Position = {}

        self.Letter_Positions_File = open('states/battle_data/Letter_Amount_Positions.txt' , "r")
        self.Letter_Positions_File_Lines = self.Letter_Positions_File.readlines()

        for line in self.Letter_Positions_File_Lines:
            self.letter_pos = line[0]
            if line[7] == ",":
                self.position_x = int(line[4:7])
                self.position_y = int(line[9:12])
            else: 
                self.position_x = int(line[4:8])
                self.position_y = int(line[10:13])
            self.Key_Amount_Position[self.letter_pos] = (self.position_x, self.position_y)
        self.Letter_Positions_File.close()

    def key_amounts(self):
        self.Key_Count_Remaining = {}

        self.Letter_Amounts_File = open('states/battle_data/Letter_Amount.txt' , "r")
        self.Letter_Amounts_File_Lines = self.Letter_Amounts_File.readlines()

        for line in self.Letter_Amounts_File_Lines:
            self.letter_count = line[0]
            self.letter_amount = line[2]
            self.Key_Count_Remaining[self.letter_count] = int(self.letter_amount)
        self.Letter_Amounts_File.close

    def key_press_action(self, key:str,):
        self.pressed_key = key
        match self.pressed_key:
            case self.pressed_key if self.pressed_key in self.valid_letters and self.max_character_count > 0:
                layer.popup_layer.fill(KEY_PURPLE)
                if self.Key_Count_Remaining[self.pressed_key] > 0:
                    layer.keyboard_layer = keyboard_sprite_sheet.pressed_key_animation(self.pressed_key)
                    sfx.keyboard_press_sound()
                    self.typed_text = self.typed_text[:self.cursor_position] + self.pressed_key + self.typed_text[self.cursor_position:]
                    self.cursor_position += 1
                    self.Key_Count_Remaining[self.pressed_key] -= 1
                    self.max_character_count -=1
                else:
                    layer.keyboard_layer = keyboard_sprite_sheet.keyboard_default_sprite()
                    update_game_screen()
                    layer.popup_layer.blit(self.no_letter_left, (530, 425))

            case self.pressed_key if self.pressed_key in self.valid_letters and self.max_character_count == 0:
                layer.keyboard_layer = keyboard_sprite_sheet.keyboard_default_sprite()
                update_game_screen()
                layer.popup_layer.blit(self.no_character_left, (580, 425))

            case self.pressed_key if self.pressed_key == 'backspace' and self.cursor_position > 0:
                layer.popup_layer.fill(KEY_PURPLE)
                layer.keyboard_layer = keyboard_sprite_sheet.keyboard_default_sprite()
                update_game_screen()
                self.deleted_key = self.typed_text[self.cursor_position - 1]  # Store the deleted key
                self.typed_text = self.typed_text[:self.cursor_position - 1] + self.typed_text[self.cursor_position:]
                self.cursor_position -= 1
                if self.deleted_key in self.valid_letters:
                    self.Key_Count_Remaining[self.deleted_key] += 1  # Add 1 to the count of the deleted key
                    self.max_character_count += 1

            case self.pressed_key if self.pressed_key == 'return':
                layer.popup_layer.fill(KEY_PURPLE)
                layer.keyboard_layer = keyboard_sprite_sheet.keyboard_default_sprite()
                update_game_screen()
                if dictionary.validWordChecker(self.typed_text) == True:
                # Update Max Character Count and Display enterd word at top of Screen
                    self.displayed_text = font.render(self.typed_text.upper(), True, WHITE) 
                    layer.popup_layer.blit(self.select_target, (650, 50))
                    update_game_screen()
                    spell.spellcast(self.typed_text)
                    self.typed_text = ""
                    self.cursor_position = 0
                else:
                    layer.popup_layer.fill(KEY_PURPLE)
                    layer.popup_layer.blit(self.not_in_dictionary, ((600), 425))


    def keyboard_display(self):
        # Make Typing Area
        layer.interface_layer.fill(KEY_PURPLE)
        pygame.draw.rect(layer.interface_layer, WHITE, (520, typing_area_y, 520, typing_area_height))
        pygame.draw.rect(layer.interface_layer, RED, (520, 880, 520, typing_area_height))

        # Draw typed text and cursor
        typed_text_surface = font.render(keyboard.typed_text.upper(), True, BLACK)
        layer.interface_layer.blit(typed_text_surface, (530, typing_area_y + 12))
        character_counter = big_font.render(str(keyboard.max_character_count), True, WHITE)
        layer.interface_layer.blit(character_counter, (1050, 473))

        for key, pos in keyboard.Key_Amount_Position.items():
            count_text = font.render(str(keyboard.Key_Count_Remaining[key]), True, BLACK)
            layer.interface_layer.blit(count_text, (pos[0], pos[1]))
            
        # End Turn Button
        self.end_turn_button = EndTurnButton(1400, 470, 1500, 40, "End Turn", font)

    def key_replenish(self):
        for key, amount in keyboard.Key_Count_Remaining.items():
            if keyboard.Key_Count_Remaining[key] < 5:
                keyboard.Key_Count_Remaining[key] += 1
        self.max_character_count = 20

def update_game_screen():
    '''
    Updates Game Window and associated Layers in order
    '''
    game_window.blit(layer.background_layer, (0,0))
    layer.combat_layer.set_colorkey(KEY_GREEN)
    layer.selection_layer.set_colorkey(KEY_GREEN)
    keyboard_sprite_sheet.keyboard_sprites.set_colorkey(KEY_GREEN)
    layer.interface_layer.set_colorkey(KEY_PURPLE)
    game_window.blit(layer.combat_layer,(0,0))
    game_window.blit(layer.selection_layer, (0,0))
    game_window.blit(layer.keyboard_layer, (0,0))
    game_window.blit(layer.popup_layer, (0,0))
    game_window.blit(layer.interface_layer, (0,0))

def clear_inputs():
    pygame.event.clear(pygame.MOUSEBUTTONDOWN)
    pygame.event.clear(pygame.MOUSEBUTTONUP)
    pygame.event.clear(pygame.KEYDOWN)

# Intalize Variable for Typing Area
typing_area_height = 50
typing_area_y = 480


keyboard = Keyboard()
dictionary = Valid_Dictionary()
layer = Layers()
timer = Timer()

# Game loop
def initalize_battle():
    timer.timer_duration = 30
    timer.start_ticks = pygame.time.get_ticks()
    layer.interface_layer.fill((KEY_PURPLE))
    layer.interface_layer.set_colorkey(KEY_PURPLE)
    layer.popup_layer.fill(KEY_PURPLE)
    layer.popup_layer.set_colorkey(KEY_PURPLE)
    character.enemy_initalizer(random.randint(1,4))
    keyboard.key_amounts()
    keyboard.keyboard_amount_position() 
    character.player_initalizer()

    

def battle_interface():
    # Printing Graphics Areaaaaaaaaaaa
    keyboard.keyboard_display()
    keyboard.end_turn_button.draw(layer.interface_layer)
    character.display_enemy()
    character.player_displayer()
    timer.update_time()
    timer.draw()
    update_game_screen()




