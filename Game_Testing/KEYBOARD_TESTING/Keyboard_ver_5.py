import pygame
import random
from Sprite_Manager import *
from Input_Manager import *
from Character_Manager import *
# START PYGAME WOOOOO pygame
pygame.init()

# Create Display Window For Game
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

game_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
keyboard_sprite_sheet_image = pygame.image.load('Assets/SimpleKeys/Classic/Light/Keys_Sprite_Sheet.png').convert_alpha()
keyboard_sprite_sheet = SpriteSheet(keyboard_sprite_sheet_image)
keyboard_sprite_sheet.get_keyboard_sprites()

# Set Layers Class
class Layers:
    def __init__(self):
        self.background_layer = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.combat_layer = character.enemy_layer
        self.interface_layer = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()
        self.keyboard_layer = keyboard_sprite_sheet.keyboard_default_sprite(6)
        self.popup_layer = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT)).convert_alpha()

# Define the Functions for keyboard updates
class Valid_Dictionary:
    def __init__(self):
        self.shared_dictionary = open('TESTS/SpellBook.txt', "r")
        self.valid_words = self.shared_dictionary.read() 
        self.valid_word_list = self.valid_words.split("\n")
        self.shared_dictionary.close()
    
    def validWordChecker(self, current_typed_word:str):
        if current_typed_word in self.valid_word_list:
            return True
        else:
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

        
        self.no_letter_left = font.render("You Have None of this Character Left!", True, WHITE)
        self.no_character_left = font.render("You Have No Characters Left!", True, WHITE)   
        self.not_in_dictionary = font.render("Word Not in your Dictionary", True, WHITE)

    def keyboard_amount_position(self):
        self.Key_Amount_Position = {}

        self.Letter_Positions_File = open('TESTS/Letter_Amount_Positions.txt' , "r")
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

        self.Letter_Amounts_File = open('TESTS/Letter_Amount.txt' , "r")
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
                    layer.keyboard_layer = keyboard_sprite_sheet.pressed_key_animation(self.pressed_key, 6)
                    self.key_state = 0
                    update_game_screen()

                    while self.key_state < 1:
                        self.key_state += 1
                        layer.keyboard_layer = keyboard_sprite_sheet.keyboard_default_sprite(6)
                    self.typed_text = self.typed_text[:self.cursor_position] + self.pressed_key + self.typed_text[self.cursor_position:]
                    self.cursor_position += 1
                    self.Key_Count_Remaining[self.pressed_key] -= 1
                    self.max_character_count -=1

                else:
                    layer.interface_layer.blit(self.no_letter_left, (530, 350))

            case self.pressed_key if self.pressed_key in self.valid_letters and self.max_character_count == 0:
                layer.popup_layer.blit(self.no_character_left, (580, 350))

            case self.pressed_key if self.pressed_key == 'backspace' and self.cursor_position > 0:
                layer.popup_layer.fill(KEY_PURPLE)
                self.deleted_key = self.typed_text[self.cursor_position - 1]  # Store the deleted key
                self.typed_text = self.typed_text[:self.cursor_position - 1] + self.typed_text[self.cursor_position:]
                self.cursor_position -= 1
                if self.deleted_key in self.valid_letters:
                    self.Key_Count_Remaining[self.deleted_key] += 1  # Add 1 to the count of the deleted key
                    self.max_character_count += 1


    
            case self.pressed_key if self.pressed_key == 'return':
                layer.popup_layer.fill(KEY_PURPLE)
                if dictionary.validWordChecker(self.typed_text) == True:
                # Update Max Character Count and Display enterd word at top of Screen
                    self.displayed_text = font.render(self.typed_text, True, WHITE) 
                    layer.popup_layer.blit(self.displayed_text, ((SCREEN_WIDTH/2 - (len(self.typed_text)*5)), 50))
                    spell.spellcast(self.typed_text)
                    self.typed_text = ""
                    self.cursor_position = 0
                else:
                    layer.popup_layer.blit(self.not_in_dictionary, ((600), 350))
                
class Battle_State:
    def __init__(self):
        pass
    def amount_of_enemies(self):
        self.enemy_count = random.randint(1,4)
        return self.enemy_count

def update_game_screen():
    '''
    Updates Game Window and associated Layers in order
    '''
    game_window.blit(layer.background_layer, (0,0))
    layer.combat_layer.set_colorkey(KEY_GREEN)
    keyboard_sprite_sheet.keyboard_sprites.set_colorkey(KEY_GREEN)
    layer.interface_layer.set_colorkey(KEY_PURPLE)
    game_window.blit(layer.combat_layer, (0,0))
    game_window.blit(layer.keyboard_layer, (0,0))
    game_window.blit(layer.popup_layer, (0,0))
    game_window.blit(layer.interface_layer, (0,0))


    pygame.display.update()

# Intalize Variable for Typing Area
typing_area_height = 50
typing_area_y = 480

# Initalizes Variables from Classes

keyboard = Keyboard()
dictionary = Valid_Dictionary()
layer = Layers()
battle = Battle_State()

# Game loop
def battle_interface():
    running = True
    layer.interface_layer.fill((KEY_PURPLE))
    layer.interface_layer.set_colorkey(KEY_PURPLE)
    layer.popup_layer.fill(KEY_PURPLE)
    layer.popup_layer.set_colorkey(KEY_PURPLE)
    character.enemy_initalizer(random.randint(1,4))
    keyboard.key_amounts()
    keyboard.keyboard_amount_position()

    #Intialize amount of enemies


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                keyboard.key_press_action(key)

    # Printing Graphics Areaaaaaaaaaaa

        #Draw Box for Player
        pygame.draw.rect(layer.combat_layer, BLUE, (300, 200, 100, 200))


        # Make Typing Area
        layer.interface_layer.fill(KEY_PURPLE)
        pygame.draw.rect(layer.interface_layer, WHITE, (520, typing_area_y, 520, typing_area_height))

        # Draw typed text and cursor
        typed_text_surface = font.render(keyboard.typed_text, True, BLACK)
        layer.interface_layer.blit(typed_text_surface, (530, typing_area_y + 12))
        character_counter = big_font.render(str(keyboard.max_character_count), True, WHITE)
        layer.interface_layer.blit(character_counter, (1350, 50))

        for key, pos in keyboard.Key_Amount_Position.items():
            count_text = font.render(str(keyboard.Key_Count_Remaining[key]), True, BLACK)
            layer.interface_layer.blit(count_text, (pos[0], pos[1]))

        # Draw keyboard and key counts

        # Update display
        update_game_screen()

battle_interface()
