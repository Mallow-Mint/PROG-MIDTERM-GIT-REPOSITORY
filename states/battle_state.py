import pygame
import random
import math
import sys
from states.state_manager import *
from states.battle_data import *
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
                    player_action.targeted_enemy(mouse_pos)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    potions.clicked_potion(mouse_pos)
                    if keyboard.end_turn_button.is_clicked() == True:
                        timer.timer_duration = 1


        character.battle_win()            
        if character.battle_state == 'WIN':
            keyboard.end_turn_key_replenish()
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

game_window = pygame.display.set_mode((1600, 900), pygame.FULLSCREEN)

# Set Colors used for Textures
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (130, 130, 130)
RED = (255, 0, 0)
KEY_PURPLE = (255, 0, 255)
KEY_YELLOW = (255,255,0)


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
Interface_Image_Hover = pygame.image.load('Assets/Interface/interface_bg_hover.png')
Typing_area = pygame.image.load('Assets/Interface/typing_area.png')
Word_holder = pygame.image.load('Assets/Interface/book_text_holder.png')
Popup_box = pygame.image.load('Assets/Interface/popup_box.png')

# Set Layers Class
class Layers:
    def __init__(self):
        self.background_layer = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.combat_layer = character.combat_layer
        self.combat_action_layer = character.combat_action_layer
        self.spell_layer = spell.spell_animation_layer
        self.selection_layer = character.selection_layer
        self.interface_layer = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()
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

        if self.time_left <= 0: # Turn switching
            if self.is_player_turn == True:
                layer.popup_layer.fill(KEY_PURPLE)
                book.Dictionary_Open = False
                keyboard.typed_text = ''
                layer.interface_layer.blit(Typing_area, (540,480))
                self.time_left_text = get_font(25).render("ENEMY TURN", True, RED)
                layer.interface_layer.blit(self.time_left_text, (680, typing_area_y + 10))
                enemy_actions.enemy_turn()
                update_game_screen()
                self.start_ticks = pygame.time.get_ticks()
                self.is_player_turn = False
                self.timer_duration = 1
            else: 
                self.timer_duration = 30
                self.is_player_turn = True
                keyboard.end_turn_key_replenish()
                spell.reset_damage()
                update_game_screen()
                clear_inputs()
                self.start_ticks = pygame.time.get_ticks()

    def draw(self):
        if self.is_player_turn == True:
            self.time_left_text_border = get_font(55).render(str(self.time_left), True, BLACK)
            self.time_left_text = get_font(50).render(str(self.time_left), True, WHITE)
            layer.interface_layer.blit(self.time_left_text_border, (12, 5))
            layer.interface_layer.blit(self.time_left_text, (12, 5))

class EndTurnButton:
    def __init__(self, x, y, width, height, text, font):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font = font 

        self.color = WHITE 
        self.hover_color = WHITE
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.color = self.hover_color
            layer.background_layer.blit(Interface_Image_Hover, (0,-10))
        text_surface = self.font.render(str(self.text), True, self.color)
        screen.blit(text_surface, (self.x+30, self.y+15))

    def is_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            return True
        return False

class Keyboard:
    def __init__(self):
        self.typed_text = ""
        self.cursor_position = 0
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

    def key_press_action(self, key:str,):
        self.pressed_key = key
        match self.pressed_key:
            case self.pressed_key if self.pressed_key in self.valid_letters and battle_data.max_character_count > 0:
                layer.popup_layer.fill(KEY_PURPLE)
                book.Dictionary_Open = False
                if battle_data.Keys_Remaining[self.pressed_key] > 0:
                    layer.keyboard_layer = keyboard_sprite_sheet.pressed_key_animation(self.pressed_key)
                    sfx.keyboard_press_sound()
                    update_game_screen()
                    self.key_state = 0
                    while self.key_state < 1:
                        self.key_state += 0.1
                    self.typed_text = self.typed_text[:self.cursor_position] + self.pressed_key + self.typed_text[self.cursor_position:]
                    self.cursor_position += 1
                    battle_data.Keys_Remaining[self.pressed_key] -= 1
                    battle_data.max_character_count -=1
                else:
                    layer.popup_layer.fill(KEY_PURPLE)
                    book.Dictionary_Open = False
                    update_game_screen()
                    layer.popup_layer.blit(Popup_box, (450,40))
                    layer.popup_layer.blit(self.no_letter_left, (530, 50))

            case self.pressed_key if self.pressed_key in self.valid_letters and battle_data.max_character_count == 0:
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
                    battle_data.Keys_Remaining[self.deleted_key] += 1  # Add 1 to the count of the deleted key
                    battle_data.max_character_count += 1

            case self.pressed_key if self.pressed_key == 'return':
                layer.popup_layer.fill(KEY_PURPLE)
                book.Dictionary_Open = False
                layer.keyboard_layer = keyboard_sprite_sheet.keyboard_default_sprite()
                update_game_screen()
                if dictionary.validWordChecker(self.typed_text) == True:
                # Update Max Character Count and Display enterd word at top of Screen
                    spell.spellcast(self.typed_text)
                    if spell.enemy_selection_state == False:
                        if spell.damage_dealt == 0:
                            player_action.heal_spell(random.randint(spell.heal_range[0], spell.heal_range[1]))
                            layer.popup_layer.blit(Popup_box, (460,40))
                            spell.reset_damage()
                            heal_text = "You healed " + str(character.hp_healed) + " HP"
                            heal_text_surface = get_font(20).render(str(heal_text), True, BLACK)
                            layer.popup_layer.blit(heal_text_surface, (680, 50))
                        if spell.damage_dealt != 0:
                            player_action.AOE_spell(spell.damage_dealt)
                            layer.popup_layer.blit(Popup_box, (460,40))
                            damage_text = "You did " + str(spell.damage_dealt) + " Damage"
                            damage_text_surface = get_font(20).render(str(damage_text), True, BLACK)
                            layer.popup_layer.blit(damage_text_surface, (680, 50))
                            spell.reset_damage()
                    elif spell.enemy_selection_state == True:
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
        layer.background_layer.blit(Interface_Image, (0,-10))

        layer.interface_layer.fill(KEY_PURPLE)
        layer.interface_layer.blit(Typing_area, (540,480))
        layer.keyboard_layer = keyboard_sprite_sheet.keyboard_default_sprite()

        # Draw typed text and cursor
        typed_text_surface = get_font(20).render(keyboard.typed_text.upper(), True, BLACK)
        layer.interface_layer.blit(typed_text_surface, (560, typing_area_y + 12))
        character_counter = get_font(40).render(str(battle_data.max_character_count), True, WHITE)
        layer.interface_layer.blit(character_counter, (1050, 473))

        for key, pos in keyboard.Key_Amount_Position.items():
            if battle_data.Keys_Remaining[key] > 0:
                count_text = get_font(20).render(str(battle_data.Keys_Remaining[key]), True, BLACK)
                layer.interface_layer.blit(count_text, (pos[0], pos[1]))
            
        # End Turn Button
        self.end_turn_button = EndTurnButton(1300, 360, 190, 60, "End Turn", get_font(25))

    def end_turn_key_replenish(self):
        for key, amount in battle_data.Keys_Remaining.items():
            if battle_data.Keys_Remaining[key] < 5:
                battle_data.Keys_Remaining[key] += 1
        battle_data.max_character_count = 20
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

class Enemy_Actions:
    def __init__ (self):
        self.enemy_types = ['skeleton', 'zombie', 'bat_eye', 'goblin']
        
    def enemy_turn(self):
        for current_enemy_attacking in range(character.amount_of_enemies):
            if character.current_enemies_alive_hp[current_enemy_attacking] != 0:
                if current_enemy_attacking == 0:
                    self.enemy1_attack()
                if current_enemy_attacking == 1:
                    self.enemy2_attack()
                if current_enemy_attacking == 2:
                    self.enemy3_attack()
                if current_enemy_attacking == 3:
                    self.enemy4_attack()
                character.enemy_actions(character.current_enemy_type[current_enemy_attacking])
            update_game_screen()
        character.battle_win()

    #ENEMY ATTACK ANIMATIONS WOOOOO!!!!
    def enemy1_attack(self):
        character.display_enemy1_attack()
        while character.enemy1.enemy_attack_sprite.current_frame > 0:
            layer.combat_layer.fill(KEY_GREEN)
            layer.combat_action_layer.fill(KEY_GREEN)
            character.display_enemy1_attack()
            character.player_idle_displayer()
            character.display_enemy2()
            character.display_enemy3()
            character.display_enemy4()
            update_game_screen()
        player_action.player_hit()

    def enemy2_attack(self):
        character.display_enemy2_attack()
        while character.enemy2.enemy_attack_sprite.current_frame > 0:
            layer.combat_layer.fill(KEY_GREEN)
            layer.combat_action_layer.fill(KEY_GREEN)
            character.display_enemy2_attack()
            character.player_idle_displayer()
            character.display_enemy1()
            character.display_enemy3()
            character.display_enemy4()
            update_game_screen()
        player_action.player_hit()

    def enemy3_attack(self):
        character.display_enemy3_attack()
        while character.enemy3.enemy_attack_sprite.current_frame > 0:
            layer.combat_layer.fill(KEY_GREEN)
            layer.combat_action_layer.fill(KEY_GREEN)
            character.display_enemy3_attack()
            character.player_idle_displayer()
            character.display_enemy1()
            character.display_enemy2()
            character.display_enemy4()
            update_game_screen()
        player_action.player_hit()

    def enemy4_attack(self):
        character.display_enemy4_attack()
        while character.enemy4.enemy_attack_sprite.current_frame > 0:
            layer.combat_layer.fill(KEY_GREEN)
            layer.combat_action_layer.fill(KEY_GREEN)
            character.display_enemy4_attack()
            character.player_idle_displayer()
            character.display_enemy1()
            character.display_enemy2()
            character.display_enemy3()
            update_game_screen()
        player_action.player_hit()
    
    #ENMEY HIT ANIMATIONS ALMOST DONE WITH ANIMATIONS FOR ENEMIESSSS
    def enemy1_hit(self):
        character.display_enemy1_hit()
        while character.enemy1.enemy_hit_sprite.current_frame > 0:
            layer.combat_layer.fill(KEY_GREEN)
            layer.combat_action_layer.fill(KEY_GREEN)
            character.display_enemy1_hit()
            character.player_idle_displayer()
            character.display_enemy2()
            character.display_enemy3()
            character.display_enemy4()
            update_game_screen()
        layer.combat_action_layer.fill(KEY_GREEN)
        character.display_enemy1()

    def enemy2_hit(self):
        character.display_enemy2_hit()
        while character.enemy2.enemy_hit_sprite.current_frame > 0:
            layer.combat_layer.fill(KEY_GREEN)
            layer.combat_action_layer.fill(KEY_GREEN)
            character.display_enemy2_hit()
            character.player_idle_displayer()
            character.display_enemy1()
            character.display_enemy3()
            character.display_enemy4()
            update_game_screen()
        layer.combat_action_layer.fill(KEY_GREEN)
        character.display_enemy2()

    def enemy3_hit(self):
        character.display_enemy3_hit()
        while character.enemy3.enemy_hit_sprite.current_frame > 0:
            layer.combat_layer.fill(KEY_GREEN)
            layer.combat_action_layer.fill(KEY_GREEN)
            character.display_enemy3_hit()
            character.player_idle_displayer()
            character.display_enemy1()
            character.display_enemy2()
            character.display_enemy4()
            update_game_screen()
        layer.combat_action_layer.fill(KEY_GREEN)
        character.display_enemy3()

    def enemy4_hit(self):
        character.display_enemy4_hit()
        while character.enemy4.enemy_hit_sprite.current_frame > 0:
            layer.combat_layer.fill(KEY_GREEN)
            layer.combat_action_layer.fill(KEY_GREEN)
            character.display_enemy4_hit()
            character.player_idle_displayer()
            character.display_enemy1()
            character.display_enemy2()
            character.display_enemy3()
            update_game_screen()
        layer.combat_action_layer.fill(KEY_GREEN)
        character.display_enemy4()

class Player_Actions:
    def __init__(self):
        pass

    def enemy_status(self, current_enemy_status:int):
        self.current_enemies_alive_hp[current_enemy_status] = int(self.current_enemies_alive_hp[current_enemy_status]) 
        if self.current_enemies_alive_hp[current_enemy_status] <= 0:
            self.current_enemies_alive_hp[current_enemy_status] = 0
    
    def targeted_enemy(self, mouse_pos):
        self.current_click = mouse_pos
        if character.enemy_1_selector.is_clicked(self.current_click) == True or \
            character.enemy_2_selector.is_clicked(self.current_click) == True or \
            character.enemy_3_selector.is_clicked(self.current_click) == True or character.enemy_4_selector.is_clicked(self.current_click) == True:
            timer.is_player_turn = False
            self.saved_time_left = timer.time_left
            self.player_attack()
            #spell.spell_sound()
            if character.enemy_1_selector.is_clicked(self.current_click) == True and character.current_enemies_alive_hp[0] !=0:
                self.spell_display_animation((790,100))
                enemy_actions.enemy1_hit()
                character.do_damage_single_target(spell.damage_dealt, 1)
                if spell.lifesteal == True:
                    player_action.heal_spell(int(damage.damage_dealt/2))

            elif character.enemy_2_selector.is_clicked(self.current_click) == True and character.current_enemies_alive_hp[1] !=0:
                self.spell_display_animation((940,50))
                enemy_actions.enemy2_hit()
                character.do_damage_single_target(spell.damage_dealt, 2)
                if spell.lifesteal == True:
                    player_action.heal_spell(int(damage.damage_dealt/2))

            elif character.enemy_3_selector.is_clicked(self.current_click) == True and character.current_enemies_alive_hp[2] !=0:
                self.spell_display_animation((1090,100))
                enemy_actions.enemy3_hit()
                character.do_damage_single_target(spell.damage_dealt, 3)
                if spell.lifesteal == True:
                    player_action.heal_spell(int(damage.damage_dealt/2))

            elif character.enemy_4_selector.is_clicked(self.current_click) == True and character.current_enemies_alive_hp[3] !=0:
                self.spell_display_animation((1240,50))
                enemy_actions.enemy4_hit()
                character.do_damage_single_target(spell.damage_dealt, 4)
                if spell.lifesteal == True:
                    player_action.heal_spell(int(damage.damage_dealt/2))
                    #spell.spell_sound()
            damage_text = "You did " + str(spell.damage_dealt) + " Damage"
            damage_text_surface = get_font(20).render(str(damage_text), True, BLACK)
            update_game_screen()
            spell.reset_damage()
            print(character.current_enemies_alive_hp)
            timer.timer_duration = self.saved_time_left
            timer.time_left = self.saved_time_left
            timer.start_ticks = pygame.time.get_ticks()
            timer.is_player_turn = True
            layer.popup_layer.blit(Popup_box, (460,40))
            layer.popup_layer.blit(damage_text_surface, (680, 50))
            character.battle_win()
        
        else:
            pass

    def heal_spell(self, hp_healed):
        self.player_heal_animation()
        #spell.spell_sound()
        self.spell_display_animation((220, 110))
        character.player_heal(hp_healed)
        print(character.player_hp_health_bar.current_hp)

    def AOE_spell(self, damage_dealt):
        timer.is_player_turn = False
        self.saved_time_left = timer.time_left
        
        self.player_attack()
        #spell.spell_sound()
        self.spell_display_animation((1000,30))
        enemy_actions.enemy1_hit()
        enemy_actions.enemy2_hit()
        enemy_actions.enemy3_hit()
        enemy_actions.enemy4_hit()
        character.do_damage_AOE(damage_dealt)
        print(character.current_enemies_alive_hp)

        timer.timer_duration = self.saved_time_left
        timer.time_left = self.saved_time_left
        timer.start_ticks = pygame.time.get_ticks()
        timer.is_player_turn = True

    def player_hit(self):
        character.player_hit_displayer()
        while character.player_hit_sprite.current_frame > 0:
            layer.combat_layer.fill(KEY_GREEN)
            layer.combat_action_layer.fill(KEY_GREEN)
            character.player_hit_displayer()
            character.display_enemy1()
            character.display_enemy2()
            character.display_enemy3()
            character.display_enemy4()
            update_game_screen()
        layer.combat_action_layer.fill(KEY_GREEN)
        character.player_idle_displayer()
    
    def player_attack(self):
        character.player_attack_displayer()
        while character.player_attack_sprite.current_frame > 0:
            layer.combat_layer.fill(KEY_GREEN)
            layer.combat_action_layer.fill(KEY_GREEN)
            character.player_attack_displayer()
            character.display_enemy1()
            character.display_enemy2()
            character.display_enemy3()
            character.display_enemy4()
            update_game_screen()
        layer.combat_action_layer.fill(KEY_GREEN)
        character.player_idle_displayer()
    
    def player_heal_animation(self):
        character.player_heal_displayer()
        while character.player_heal_sprite.current_frame > 0:
            layer.combat_layer.fill(KEY_GREEN)
            layer.combat_action_layer.fill(KEY_GREEN)
            character.player_heal_displayer()
            character.display_enemy1()
            character.display_enemy2()
            character.display_enemy3()
            character.display_enemy4()
            update_game_screen()
        layer.combat_action_layer.fill(KEY_GREEN)
        character.player_idle_displayer()
    
    def spell_display_animation(self, spell_pos):
        spell.spell_animation.display_sprite(spell_animations.current_spell_color, spell_pos)
        while spell.spell_animation.current_frame > 0:
            layer.spell_layer.fill(KEY_YELLOW)
            layer.combat_layer.fill(KEY_GREEN)
            spell.spell_animation.display_sprite(spell_animations.current_spell_color, spell_pos)
            character.player_idle_displayer()
            character.display_enemy1()
            character.display_enemy2()
            character.display_enemy3()
            character.display_enemy4()
            update_game_screen()
        layer.spell_layer.fill(KEY_YELLOW)

typing_area_height = 50
typing_area_y = 480

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
    game_window.blit(layer.combat_action_layer,(0,0))
    game_window.blit(layer.spell_layer,(0,0))
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
enemy_actions = Enemy_Actions()
player_action = Player_Actions()
timer = Timer()
player_inventory = Player_Inventory()

# Game loop
def initalize_battle():
    timer.timer_duration = 30
    timer.start_ticks = pygame.time.get_ticks()
    character.battle_state = None
    timer.is_player_turn = True
    layer.combat_action_layer.fill(KEY_GREEN)
    layer.combat_action_layer.set_colorkey(KEY_GREEN)
    layer.spell_layer.fill(KEY_YELLOW)
    layer.spell_layer.set_colorkey(KEY_YELLOW)
    layer.interface_layer.fill(KEY_PURPLE)
    layer.interface_layer.set_colorkey(KEY_PURPLE)
    layer.popup_layer.fill(KEY_PURPLE)
    layer.popup_layer.set_colorkey(KEY_PURPLE)
    character.enemy_initalizer(random.randint(2,4))
    damage.chain_word_damage_multipler = 1
    battle_data.max_character_count = 20
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

