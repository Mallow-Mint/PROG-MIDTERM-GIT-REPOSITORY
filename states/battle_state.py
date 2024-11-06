import pygame
import random
import math
import sys
from states.state_manager import *
from states.managers.Sprite_Manager import *
from states.managers.Input_Manager import *
from states.managers.Battle_Manager import *
from states.managers.Audio_Manager import *
from states.battle_data.battle_data import *

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
                    damage.targeted_enemy(mouse_pos)
                    if spell.enemy_selection_state == False:
                        layer.popup_layer.fill(KEY_PURPLE)
                        update_game_screen()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    potions.clicked_potion(mouse_pos)
                    if keyboard.end_turn_button.is_clicked() == True:
                        timer.timer_duration = 1

        character.battle_win()            
        if character.battle_state == 'WIN':
            keyboard.key_replenish()
            keyboard.save_key_amounts()
            self.exit_state()
        if character.battle_state == 'LOSS':
            self.exit_state()

    def render(self, display):
        battle_interface()
        display.blit(game_window, (0,0))

pygame.init()
# Create Display Window For Game
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

game_window = pygame.display.set_mode((1600, 900))

# Set Colors used for Textures
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (130, 130, 130)
RED = (255, 0, 0)
KEY_PURPLE = (255, 0, 255)


# Set fonts Used for Text
def get_font(font_size):
    font = pygame.font.Font('Assets/Fonts/minercraftory/Minercraftory.ttf', font_size)
    return font

# Get Sprite Sheet for Keyboard
keyboard_sprite_sheet_image = get_image('Assets/SimpleKeys/Classic/Light/Keys_Sprite_Sheet.png', 6)
keyboard_sprite_sheet = KeyboardSprites(keyboard_sprite_sheet_image)
keyboard_sprite_sheet.get_keyboard_sprites()

Background_Image = pygame.image.load('Assets/Background/bg_11/bg_11.png')
Background_Image = pygame.transform.scale(Background_Image, (1600, 900))
Interface_Image = pygame.image.load('Assets/Interface/interface_bg.png')
Typing_area = pygame.image.load('Assets/Interface/typing_area.png')
Word_holder = pygame.image.load('Assets/Interface/book_text_holder.png')
Popup_box = pygame.image.load('Assets/Interface/popup_box.png')

# Set Layers Class
class Layers:
    def __init__(self):
        self.background_layer = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.combat_layer = character.combat_layer
        self.combat_action_layer = character.combat_action_layer
        #spell.action_layer
        self.selection_layer = character.selection_layer
        self.interface_layer = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.keyboard_layer = keyboard_sprite_sheet.keyboard_default_sprite()
        self.popup_layer = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT)).convert_alpha()

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
                self.time_left_text = get_font(40).render("ENEMY TURN", True, RED)
                layer.interface_layer.blit(self.time_left_text, (15, 15))
                layer.popup_layer.fill(KEY_PURPLE)
                book.Dictionary_Open = False
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
            self.time_left_text = get_font(40).render(str(self.time_left), True, WHITE)
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
        self.Dictionary_Open = False
        self.valid_letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 
                              'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                              'z', 'x', 'c', 'v', 'b', 'n', 'm' ]
        self.key_state = 1 #1 is default 0 is pressed

        # Popup Messages
        self.no_letter_left = get_font(20).render("You Have None of this Character Left!", True, BLACK)
        self.no_character_left = get_font(20).render("You Have No Characters Left!", True, BLACK)   
        self.not_in_dictionary = get_font(20).render("Word Not in your Dictionary", True, BLACK)
        self.select_target = get_font(20).render("Please Select a Target", True, BLACK)

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

    def get_key_amounts(self):
        self.Key_Count_Remaining = battle_data.Keys_Remaining

    def save_key_amounts(self):
        battle_data.Keys_Remaining = self.Key_Count_Remaining

    def key_press_action(self, key:str,):
        self.pressed_key = key
        match self.pressed_key:
            case self.pressed_key if self.pressed_key in self.valid_letters and self.max_character_count > 0:
                layer.popup_layer.fill(KEY_PURPLE)
                book.Dictionary_Open = False
                if self.Key_Count_Remaining[self.pressed_key] > 0:
                    layer.keyboard_layer = keyboard_sprite_sheet.pressed_key_animation(self.pressed_key)
                    sfx.keyboard_press_sound()
                    update_game_screen()
                    self.key_state = 0
                    update_game_screen()
                    while self.key_state < 1:
                        self.key_state += 0.1
                        layer.keyboard_layer = keyboard_sprite_sheet.keyboard_default_sprite()
                    self.typed_text = self.typed_text[:self.cursor_position] + self.pressed_key + self.typed_text[self.cursor_position:]
                    self.cursor_position += 1
                    self.Key_Count_Remaining[self.pressed_key] -= 1
                    self.max_character_count -=1
                else:
                    layer.popup_layer.fill(KEY_PURPLE)
                    book.Dictionary_Open = False
                    update_game_screen()
                    layer.popup_layer.blit(Popup_box, (450,40))
                    layer.popup_layer.blit(self.no_letter_left, (530, 50))

            case self.pressed_key if self.pressed_key in self.valid_letters and self.max_character_count == 0:
                layer.popup_layer.fill(KEY_PURPLE)
                book.Dictionary_Open = False
                layer.keyboard_layer = keyboard_sprite_sheet.keyboard_default_sprite()
                update_game_screen()
                layer.popup_layer.blit(Popup_box, (440,40))
                layer.popup_layer.blit(self.no_character_left, (580, 50))

            case self.pressed_key if self.pressed_key == 'backspace' and self.cursor_position > 0:
                layer.popup_layer.fill(KEY_PURPLE)
                book.Dictionary_Open = False
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
                book.Dictionary_Open = False
                layer.keyboard_layer = keyboard_sprite_sheet.keyboard_default_sprite()
                update_game_screen()
                if dictionary.validWordChecker(self.typed_text) == True:
                # Update Max Character Count and Display enterd word at top of Screen
                    spell.spellcast(self.typed_text)
                    if spell.enemy_selection_state == True:
                        self.displayed_text = get_font(20).render(self.typed_text.upper(), True, BLACK)
                        layer.popup_layer.blit(Popup_box, (460,40))
                        layer.popup_layer.blit(self.select_target, (650, 50))
                        update_game_screen()
                    self.typed_text = ""
                    self.cursor_position = 0
                else:
                    layer.popup_layer.fill(KEY_PURPLE)
                    layer.popup_layer.blit(Popup_box, (440,40))
                    layer.popup_layer.blit(self.not_in_dictionary, ((600), 50))
            
            case self.pressed_key if self.pressed_key == 'tab':
                if book.Dictionary_Open == False:
                    book.current_page = 0
                    layer.popup_layer.fill((0,0,0,150))
                    book.display_book()
                    book.display_word_holders()
                    book.update_current_page_forward()
                    book.display_current_word_set()
                    book.Dictionary_Open = True
                elif book.Dictionary_Open == True:
                    layer.popup_layer.fill(KEY_PURPLE)
                    book.current_page = 0
                    book.Dictionary_Open = False
            
            case self.pressed_key if self.pressed_key == 'right' and book.Dictionary_Open == True:
                layer.popup_layer.fill((0,0,0,150))
                book.display_book()
                book.display_word_holders()
                book.update_current_page_forward()
                book.display_current_word_set()
            
            case self.pressed_key if self.pressed_key == 'left' and book.Dictionary_Open == True:
                layer.popup_layer.fill((0,0,0,150))
                book.display_book()
                book.display_word_holders()
                book.update_current_page_backward()
                book.display_current_word_set()

    def keyboard_display(self):
        # Make Typing Area
        layer.background_layer.blit(Background_Image, (0,-440))
        layer.background_layer.blit(Interface_Image, (0,410))

        layer.interface_layer.fill(KEY_PURPLE)
        layer.interface_layer.blit(Typing_area, (540,480))

        # Draw typed text and cursor
        typed_text_surface = get_font(20).render(keyboard.typed_text.upper(), True, BLACK)
        layer.interface_layer.blit(typed_text_surface, (560, typing_area_y + 12))
        character_counter = get_font(40).render(str(keyboard.max_character_count), True, WHITE)
        layer.interface_layer.blit(character_counter, (1050, 473))

        for key, pos in keyboard.Key_Amount_Position.items():
            count_text = get_font(20).render(str(keyboard.Key_Count_Remaining[key]), True, BLACK)
            layer.interface_layer.blit(count_text, (pos[0], pos[1]))
            
        # End Turn Button
        self.end_turn_button = EndTurnButton(1400, 470, 1500, 40, "End Turn", get_font(20))

    def key_replenish(self):
        for key, amount in keyboard.Key_Count_Remaining.items():
            if keyboard.Key_Count_Remaining[key] < 5:
                keyboard.Key_Count_Remaining[key] += 1
        self.max_character_count = 20
        self.typed_text = ''
        self.cursor_position = 0

class Book:
    def __init__(self):
        self.Dictionary_Open = False
        self.book_img = get_image('Assets/Interface/book_display.png')
        self.book_sprite = General_Spritesheet(self.book_img, 19200, 1080, 10, 1, 10, layer.popup_layer)
        self.current_page = 0
    
    def get_page_count(self):
        self.page_count = len(dictionary.valid_word_list) // 10 + 1
    
    def display_book(self):
        book.book_sprite.display_sprite(-150, -200)
        layer.popup_layer.fill(KEY_PURPLE)
        while book.book_sprite.current_frame > 0:
            layer.popup_layer.fill(KEY_PURPLE)
            layer.popup_layer.fill((0,0,0,150))
            book.book_sprite.display_sprite(-150, -200)
            update_game_screen()
            clear_inputs()
    
    def display_word_holders(self):
        for x in range(10):
            if x % 2 == 0:
                layer.popup_layer.blit(Word_holder, (360, 100 + (125*int(x/2))))
            else:
                layer.popup_layer.blit(Word_holder, (900, 100 + (125 *int(x//2))))
    
    def display_current_word_set(self):
        if self.current_page == 1:
            current_word_set_start = 0
            current_word_set_end = 10
        elif self.current_page < self.page_count: 
            current_word_set_start = 10 * (self.current_page - 1)
            current_word_set_end = 10 * (self.current_page)
        elif self.current_page == self.page_count: 
            current_word_set_start = 10 * (self.current_page - 1)
            current_word_set_end = len(dictionary.valid_word_list)
        
        for word in range(current_word_set_start, current_word_set_end):
            word_display = get_font(20).render(dictionary.valid_word_list[word], True, BLACK)
            if word % 2 == 0 and self.current_page == 1:
                layer.popup_layer.blit(word_display, (380,110 + (125*int(word/2))))
            elif word % 2 != 0 and self.current_page == 1:
                layer.popup_layer.blit(word_display, (920, 110 + (125 *int(word//2))))
            elif word % 2 == 0 and self.current_page > 1:
                layer.popup_layer.blit(word_display, (380, 110 + (125*int((word%10)/2))))
            elif word % 2 != 0 and self.current_page > 1:
                layer.popup_layer.blit(word_display, (920, 110 + (125 *int((word%10)//2))))

    def update_current_page_forward(self):
        self.current_page += 1
        if self.current_page > self.page_count:
            self.current_page = 1
    def update_current_page_backward(self):
        self.current_page -= 1
        if self.current_page == 0:
            self.current_page = self.page_count

class Player_Inventory:
    def __init__(self):
        sprite_sheet_HpS = get_image('Assets/Shop_Assets/Healing potion OG.png', 2)
        sprite_sheet_HpXL = get_image('Assets/Shop_Assets/XL Healing potion OG.png', 2)
        sprite_sheet_ALpotion = get_image('Assets/Shop_Assets/All Leter Potion OG.png',2)
        sprite_sheet_Lpotion = get_image('Assets/Shop_Assets/Letter Potion OG.png', 2)
        self.Health_Pot_Sprite = General_Spritesheet(sprite_sheet_HpS, 285, 38, 15, 2, 75, layer.interface_layer)
        self.Health_Pot_XL_Sprite = General_Spritesheet(sprite_sheet_HpXL, 432, 34, 24, 2, 75, layer.interface_layer)
        self.All_Letter_Potion_Sprite = General_Spritesheet(sprite_sheet_ALpotion, 288, 39, 12, 2, 75, layer.interface_layer)
        self.Letter_Potion_Sprite = General_Spritesheet(sprite_sheet_Lpotion, 396, 35, 22, 2, 75, layer.interface_layer)

            
    def display_invetory(self):
        for i in range(len(battle_data.inventory_slots)):
            if battle_data.inventory_slots[0] is not None:
                if battle_data.inventory_slots[0] == "Healing Potion S":
                    self.Health_Pot_Sprite.display_sprite(120, 590)
                elif battle_data.inventory_slots[0] == "Healing Potion XL":
                    self.Health_Pot_XL_Sprite.display_sprite(120, 590)
                elif battle_data.inventory_slots[0] == "All Letter Potion":
                    self.All_Letter_Potion_Sprite.display_sprite(120, 590)
                elif battle_data.inventory_slots[0] == "Letter Potion":
                    self.Letter_Potion_Sprite.display_sprite(120, 590) 

            if battle_data.inventory_slots[1] is not None: 
                if battle_data.inventory_slots[1] == "Healing Potion S":
                    self.Health_Pot_Sprite.display_sprite(120, 730) 
                elif battle_data.inventory_slots[1] == "Healing Potion XL":
                    self.Health_Pot_XL_Sprite.display_sprite(120, 730)
                elif battle_data.inventory_slots[1] == "All Letter Potion":
                    self.All_Letter_Potion_Sprite.display_sprite(120, 730) 
                elif battle_data.inventory_slots[1] == "Letter Potion":
                    self.Letter_Potion_Sprite.display_sprite(120, 730)

            if battle_data.inventory_slots[2] is not None:
                if battle_data.inventory_slots[2] == "Healing Potion S":
                    self.Health_Pot_Sprite.display_sprite(1440, 590) 
                elif battle_data.inventory_slots[2] == "Healing Potion XL":
                    self.Health_Pot_XL_Sprite.display_sprite(1440, 590) 
                elif battle_data.inventory_slots[2] == "All Letter Potion":
                    self.All_Letter_Potion_Sprite.display_sprite(1440, 590) 
                elif battle_data.inventory_slots[2] == "Letter Potion":
                    self.Letter_Potion_Sprite.display_sprite(1440, 590)

            if battle_data.inventory_slots[3] is not None:
                if battle_data.inventory_slots[3] == "Healing Potion S":
                    self.Health_Pot_Sprite.display_sprite(1440, 730) 
                elif battle_data.inventory_slots[3] == "Healing Potion XL":
                    self.Health_Pot_XL_Sprite.display_sprite(1440, 730)
                elif battle_data.inventory_slots[3] == "All Letter Potion":
                    self.All_Letter_Potion_Sprite.display_sprite(1440, 730)
                elif battle_data.inventory_slots[3] == "Letter Potion":
                    self.Letter_Potion_Sprite.display_sprite(1440, 730) 

typing_area_height = 50
typing_area_y = 480

def update_game_screen():
    '''
    Updates Game Window and associated Layers in order
    '''
    game_window.blit(layer.background_layer, (0,0))
    layer.combat_layer.set_colorkey(KEY_GREEN)
    layer.combat_action_layer.set_colorkey(KEY_GREEN)
    layer.selection_layer.set_colorkey(KEY_GREEN)
    keyboard_sprite_sheet.keyboard_sprites.set_colorkey(KEY_GREEN)
    layer.interface_layer.set_colorkey(KEY_PURPLE)
    game_window.blit(layer.combat_layer,(0,0))
    game_window.blit(layer.combat_action_layer,(0,0))
    game_window.blit(layer.selection_layer, (0,0))
    game_window.blit(layer.keyboard_layer, (0,0))
    game_window.blit(layer.interface_layer, (0,0))
    game_window.blit(layer.popup_layer, (0,0))
    pygame.display.flip()

def clear_inputs():
    pygame.event.clear(pygame.MOUSEBUTTONDOWN)
    pygame.event.clear(pygame.MOUSEBUTTONUP)
    pygame.event.clear(pygame.KEYDOWN)

layer = Layers()
book = Book()
keyboard = Keyboard()
timer = Timer()
player_inventory = Player_Inventory()

# Game loop
def initalize_battle():
    timer.timer_duration = 30
    timer.start_ticks = pygame.time.get_ticks()
    character.battle_state = None
    timer.is_player_turn = True
    layer.interface_layer.fill((KEY_PURPLE))
    layer.interface_layer.set_colorkey(KEY_PURPLE)
    layer.popup_layer.fill(KEY_PURPLE)
    layer.popup_layer.set_colorkey(KEY_PURPLE)
    character.enemy_initalizer(random.randint(2,4))
    damage.chain_word_damage_multipler = 1
    keyboard.max_character_count = 20
    keyboard.get_key_amounts()
    keyboard.keyboard_amount_position() 
    character.player_initalizer()
    book.get_page_count()
    music.Battle_BGM_1()
    print(character.amount_of_enemies)
    print(character.current_enemies_alive_hp)

def battle_interface():
    # Printing Graphics Areaaaaaaaaaaa
    keyboard.keyboard_display()
    keyboard.end_turn_button.draw(layer.interface_layer)
    character.display_idle_enemy()
    character.player_idle_displayer()
    potions.display_inventory_buttons()
    player_inventory.display_invetory()
    timer.update_time()
    timer.draw()
    update_game_screen()

