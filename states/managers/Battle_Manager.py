import pygame
import random
import time
from states.state_manager import *
from states.managers.Audio_Manager import *
from states.managers.Sprite_Manager import *
from states.battle_data.battle_data import *
from states.battle_data.enemy_data import *
from main_spellbook import *

RED = (255, 0, 0)
WHITE = (255, 255, 255)
DARK_GREEN = (0, 102, 17)
DARK_RED = (100, 0, 5)
BLUE = (0, 0, 145)
YELLOW = (255, 255, 0)
KEY_GREEN = (30, 255, 0)

class HealthBar:
  def __init__(self, x, y, w, h, max_hp):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.current_hp = max_hp
    self.max_hp = max_hp

  def draw(self, surface):
    #calculate health ratio
    ratio = self.current_hp / self.max_hp
    pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
    pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))

import pygame

class Button:
    def __init__(self, x, y, width, height, button_color, hover_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.button_color = button_color
        self.hover_color = hover_color
        self.rect = pygame.Rect(x, y, width, height)
        self.selection_sprite_img = get_image('Assets/Interface/selection_sprites.png')
        self.selection_sprites = General_Spritesheet(self.selection_sprite_img, 105, 27, 4, 1, 0, character.selection_layer)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.draw_hover()

    def is_clicked(self, mouse_pos):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            return True
        return False
    
    def draw_hover(self):
        self.selection_sprites.get_single_frame(0, self.x-5, self.y-5)
        self.selection_sprites.get_single_frame(1, self.x+self.width-20, self.y-5)
        self.selection_sprites.get_single_frame(2, self.x-5, self.y+self.height-20)
        self.selection_sprites.get_single_frame(3, self.x+self.width-20, self.y+self.height-20)

class Enemy:
    def __init__(self, enemy_type, enemy_number):
        self.enemy = enemy_type
        self.enemy_max_hp = mobs_list_hp[enemy_type]
        character.current_enemy_type.append(self.enemy)
        character.current_enemies_alive_hp[enemy_number] = self.enemy_max_hp
        self.enemy_sprite = character.get_enemy_idle_sprite(self.enemy)

class Character:
    def __init__(self):
        self.combat_layer = pygame.Surface((1600,900))
        self.combat_action_layer = pygame.Surface((1600,900))
        self.selection_layer = pygame.Surface((1600,900))
        self.selected_enemy = 0
        self.current_enemies_alive_hp = [0,0,0,0]
        self.current_enemy_type = []
        self.battle_state = None

    def random_enemy_type(self):
        return mobs_list_type[random.randint(0,3)]
    
    def get_enemy_idle_sprite(self, enemy_type):
        match enemy_type:
            case 'skeleton':
                current_enemy_sprite = General_Spritesheet(skeleton_idle_img, 600, 150, 4, 3, random.randint(100,175), self.combat_layer)
            case 'zombie':
                current_enemy_sprite = General_Spritesheet(zombie_idle_img, 600, 150, 4, 3, random.randint(100,175), self.combat_layer)
            case 'orc':
                current_enemy_sprite = General_Spritesheet(orc_idle_img, 256, 64, 4, 5, random.randint(100,175), self.combat_layer)
            case 'goblin':
                current_enemy_sprite = General_Spritesheet(goblin_idle_img, 600, 150, 4, 3, random.randint(100,175), self.combat_layer)

        return current_enemy_sprite
    

    def enemy_initalizer(self, enemy_count:int):
        for x in range(enemy_count):
            random_enemy = self.random_enemy_type()
            if x == 0:
                self.enemy1 = Enemy('skeleton', x)
                self.enemy1_hp_bar = HealthBar(880, 160, 140, 20, self.enemy1.enemy_max_hp)

            elif x == 1:
                self.enemy2 = Enemy(random_enemy, x)
                self.enemy2_hp_bar = HealthBar(1030, 110, 140, 20, self.enemy2.enemy_max_hp)

            elif x == 2:
                self.enemy3 = Enemy(random_enemy, x)
                self.enemy3_hp_bar = HealthBar(1180, 160, 140, 20, self.enemy3.enemy_max_hp)

            elif x == 3:                
                self.enemy4 = Enemy(random_enemy, x)
                self.enemy4_hp_bar = HealthBar(1330, 110, 140, 20, self.enemy4.enemy_max_hp)
        
        for x in range(4 - enemy_count):
            if x == 0:
                self.enemy4_hp_bar = HealthBar(1330, 110, 140, 20, 0)
            elif x == 1:
                self.enemy3_hp_bar = HealthBar(1180, 160, 140, 20, 0)
            elif x == 2:
                self.enemy2_hp_bar = HealthBar(1030, 110, 140, 20, 0)

        self.amount_of_enemies = enemy_count
    
    def check_enemy_type_offset(self, enemy_type):
        match enemy_type:
            case enemy_type if enemy_type in mobs_list_type:
                self.x_offset = mobs_list_offset[enemy_type][0]
                self.y_offset = mobs_list_offset[enemy_type][1]

    def display_idle_enemy(self):
        self.combat_layer.fill(KEY_GREEN)
        self.combat_action_layer.fill(KEY_GREEN)
        self.selection_layer.fill(KEY_GREEN)

        for enemy in range(self.amount_of_enemies):
            if enemy == 0 and self.current_enemies_alive_hp[enemy] > 0:
                pygame.draw.rect(self.combat_layer, (0,0,0), (875, 155, 150, 30))
                self.enemy1_hp_bar.draw(self.combat_layer)
                self.check_enemy_type_offset(self.enemy1.enemy)
                self.enemy1.enemy_sprite.display_sprite(900-self.x_offset, 200-self.y_offset)

            elif enemy == 1 and self.current_enemies_alive_hp[enemy] > 0:
                pygame.draw.rect(self.combat_layer, (0,0,0), (1025, 105, 150, 30))
                self.enemy2_hp_bar.draw(self.combat_layer)
                self.check_enemy_type_offset(self.enemy2.enemy)
                self.enemy2.enemy_sprite.display_sprite(1050-self.x_offset, 150-self.y_offset)

            elif enemy == 2 and self.current_enemies_alive_hp[enemy] > 0:
                pygame.draw.rect(self.combat_layer, (0,0,0), (1175, 155, 150, 30))
                self.enemy3_hp_bar.draw(self.combat_layer)
                self.check_enemy_type_offset(self.enemy3.enemy)
                self.enemy3.enemy_sprite.display_sprite(1200-self.x_offset, 200-self.y_offset)

            elif enemy == 3 and self.current_enemies_alive_hp[enemy] > 0:
                pygame.draw.rect(self.combat_layer, (0,0,0), (1325, 105, 150, 30))
                self.enemy4_hp_bar.draw(self.combat_layer)
                self.check_enemy_type_offset(self.enemy4.enemy)
                self.enemy4.enemy_sprite.display_sprite(1350-self.x_offset, 150-self.y_offset)
        
        #Draw Buttons for Enemies
        self.enemy_1_selector = Button(900, 200, 100, 200, KEY_GREEN, YELLOW)
        if character.current_enemies_alive_hp[0] !=0:
            self.enemy_1_selector.draw(self.selection_layer)

        self.enemy_2_selector = Button(1050, 150, 100, 200, KEY_GREEN, YELLOW)
        if character.current_enemies_alive_hp[1] !=0:
            self.enemy_2_selector.draw(self.selection_layer)

        self.enemy_3_selector = Button(1200, 200, 100, 200, KEY_GREEN, YELLOW)
        if character.current_enemies_alive_hp[2] !=0:
            self.enemy_3_selector.draw(self.selection_layer)

        self.enemy_4_selector = Button(1350, 150, 100, 200, KEY_GREEN, YELLOW)
        if character.current_enemies_alive_hp[3] !=0:
            self.enemy_4_selector.draw(self.selection_layer)

    def enemy_status(self, current_enemy_status:int):
        self.current_enemies_alive_hp[current_enemy_status] = int(self.current_enemies_alive_hp[current_enemy_status]) 
        if self.current_enemies_alive_hp[current_enemy_status] <= 0:
            self.current_enemies_alive_hp[current_enemy_status] = 0

    def do_damage_single_target(self, damage_dealt, enemy_targeted):
        match enemy_targeted:
            case 1:
                self.enemy1_hp_bar.current_hp -= damage_dealt
                self.current_enemies_alive_hp[0] = self.enemy1_hp_bar.current_hp
                character.enemy_status(0)
            case 2:
                self.enemy2_hp_bar.current_hp -= damage_dealt
                self.current_enemies_alive_hp[1] = self.enemy2_hp_bar.current_hp
                character.enemy_status(1)
            case 3:
                self.enemy3_hp_bar.current_hp -= damage_dealt
                self.current_enemies_alive_hp[2] = self.enemy3_hp_bar.current_hp
                character.enemy_status(2)
            case 4:
                self.enemy4_hp_bar.current_hp -= damage_dealt
                self.current_enemies_alive_hp[3] = self.enemy4_hp_bar.current_hp
                character.enemy_status(3)
    
    def do_damage_AOE(self, damage_dealt):
        self.enemy1_hp_bar.current_hp -= damage_dealt
        self.current_enemies_alive_hp[0] = self.enemy1_hp_bar.current_hp
        character.enemy_status(0)

        self.enemy2_hp_bar.current_hp -= damage_dealt
        self.current_enemies_alive_hp[1] = self.enemy2_hp_bar.current_hp
        character.enemy_status(1)

        self.enemy3_hp_bar.current_hp -= damage_dealt
        self.current_enemies_alive_hp[2] = self.enemy3_hp_bar.current_hp
        character.enemy_status(2)

        self.enemy4_hp_bar.current_hp -= damage_dealt
        self.current_enemies_alive_hp[3] = self.enemy4_hp_bar.current_hp
        character.enemy_status(3)

# PLAYER RELATED FUNCTIONS --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

    def player_initalizer(self):
        self.player_hp_health_bar = HealthBar(280, 160, 140, 20, 50)
        self.player_hp_health_bar.current_hp = battle_data.current_health[0]
        self.player_sprite_img = get_image('Assets/Wizard Pack/Idle.png', 2)
        self.player_sprite = General_Spritesheet(self.player_sprite_img, 1386, 190, 6, 2, 200, self.selection_layer)

    def player_idle_displayer(self):
        pygame.draw.rect(self.combat_layer, (0,0,0), (275, 155, 150, 30))
        self.player_hp_health_bar.draw(self.combat_layer)
        self.player_sprite.display_sprite(140, 90)

    def player_heal(self, hp_healed, hp_change=0):
        hp_change = battle_data.current_health[0]
        hp_change += hp_healed
        battle_data.current_health[0] = int(hp_change)
        if battle_data.current_health[0] > 50:
            battle_data.current_health[0] = 50
        self.player_hp_health_bar.current_hp = battle_data.current_health[0]
        self.player_hp_health_bar.draw(self.combat_layer)
    
    def player_damage(self, hp_damage, hp_change=0):
        hp_change = battle_data.current_health[0]
        hp_change -= hp_damage
        battle_data.current_health[0] = int(hp_change)
        self.player_hp_health_bar.current_hp = battle_data.current_health[0]
        self.player_hp_health_bar.draw(self.combat_layer)
    
    def battle_win(self):
        self.total_enemy_hp = 0
        for enemy_hp in range(self.amount_of_enemies):
            self.total_enemy_hp += self.current_enemies_alive_hp[enemy_hp]
        
        if self.total_enemy_hp == 0:
            self.battle_state = 'WIN'
            battle_data.current_health = battle_data.current_health
            music.Battle_BGM_1_stop()
        
        if self.player_hp_health_bar.current_hp <= 0:
            self.battle_state = 'LOSS'
            music.Battle_BGM_1_stop()

class Potions:
    def __init__(self):
        self.inventory_slot_1 = Button(80, 570, 115, 110, KEY_GREEN, YELLOW)
        self.inventory_slot_2 = Button(80, 710, 115, 110, KEY_GREEN, YELLOW)
        self.inventory_slot_3 = Button(1400, 570, 115, 110, KEY_GREEN, YELLOW)
        self.inventory_slot_4 = Button(1400, 710, 115, 110, KEY_GREEN, YELLOW)
        self.potion_selection_state = False
    
    def display_inventory_buttons(self):
        if battle_data.inventory_slots[0] is not None:
            self.inventory_slot_1.draw(character.selection_layer)
        if battle_data.inventory_slots[1] is not None:
            self.inventory_slot_2.draw(character.selection_layer)
        if battle_data.inventory_slots[2] is not None:
            self.inventory_slot_3.draw(character.selection_layer)
        if battle_data.inventory_slots[3] is not None:
            self.inventory_slot_4.draw(character.selection_layer)

    def clicked_potion(self, mouse_pos):
        self.current_click = mouse_pos

        if self.inventory_slot_1.is_clicked(self.current_click):
            battle_data.inventory_slots[0] = None
            print('clicked on inventory_1')

        elif self.inventory_slot_2.is_clicked(self.current_click):
            battle_data.inventory_slots[1] = None
            print('clicked on inventory_2')

        elif self.inventory_slot_3.is_clicked(self.current_click):
            battle_data.inventory_slots[2]= None
            print('clicked on inventory_3')
            
        elif self.inventory_slot_4.is_clicked(self.current_click):
            battle_data.inventory_slots[3] = None
            print('clicked on inventory_4')
        
        else:
            return None


character = Character()
potions = Potions()