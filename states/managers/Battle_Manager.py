import pygame
import random
import time
from states.state_manager import *
from states.managers.Audio_Manager import *
from states.managers.Sprite_Manager import *
from states.battle_data.battle_data import *

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
        self.selection_sprites.get_frames()

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

class Character:
    def __init__(self):
        self.mobs_list_color = {'skeleton': 'Assets/Monsters/4 direction monsters/Skeleton/Idle.png', 
                                'zombie': 'Assets/Monsters/4 direction monsters/Mushroom/Idle.png',
                                'orc': 'Assets/Monsters/Golem_IdleB.png' ,
                                'goblin': 'Assets/Monsters/4 direction monsters/Goblin/Idle.png'}
        
        self.mobs_list_hp = {'skeleton': 15, 'zombie': 10, 'orc': 20 , 'goblin': 10}
        self.combat_layer = pygame.Surface((1600,900))
        self.selection_layer = pygame.Surface((1600,900))
        self.selected_enemy = 0
        self.current_enemies_alive_hp = [0,0,0,0]
        self.current_enemy_type = []
        self.battle_state = None

    def random_enemy_type(self):
        self.mob_list_type = list(self.mobs_list_color.keys())
        return self.mob_list_type[random.randint(0,3)]
    
    def enemy_color(self, enemy_type):
        enemy_sprite = self.mobs_list_color[enemy_type]
        print(enemy_sprite)
        return enemy_sprite
    
    def get_enemy_sprite(self, enemy_type, enemy_type_png):
        current_enemy_sprite_img = enemy_type_png

        match enemy_type:
            case 'skeleton':
                current_enemy_sprite_image = get_image(current_enemy_sprite_img, 3)
                current_enemy_sprite = General_Spritesheet(current_enemy_sprite_image, 600, 150, 4, 3, 125, self.combat_layer)
            case 'zombie':
                current_enemy_sprite_image = get_image(current_enemy_sprite_img, 3)
                current_enemy_sprite = General_Spritesheet(current_enemy_sprite_image, 600, 150, 4, 3, 125, self.combat_layer)
            case 'orc':
                current_enemy_sprite_image = get_image(current_enemy_sprite_img, 5)
                current_enemy_sprite = General_Spritesheet(current_enemy_sprite_image, 256, 64, 4, 5, 125, self.combat_layer)
            case 'goblin':
                current_enemy_sprite_image = get_image(current_enemy_sprite_img, 3)
                current_enemy_sprite = General_Spritesheet(current_enemy_sprite_image, 600, 150, 4, 3, 125, self.combat_layer)

        return current_enemy_sprite

    
    def enemy_initalizer(self, enemy_count:int):
        for x in range(enemy_count):
            if x == 0:
                self.enemy1 = character.random_enemy_type()
                self.enemy1_max_hp = self.mobs_list_hp[self.enemy1]
                self.current_enemy_type.append(self.enemy1)
                self.current_enemies_alive_hp[0] = self.enemy1_max_hp

                self.enemy_1_sprite_img = character.enemy_color(self.enemy1)
                self.enemy_1_sprite = self.get_enemy_sprite(self.enemy1, self.enemy_1_sprite_img)
                self.enemy_1_sprite.get_frames()
                self.enemy_1_hp_bar = HealthBar(880, 160, 140, 20, self.enemy1_max_hp)

            elif x == 1:
                self.enemy2 = character.random_enemy_type()
                self.enemy2_max_hp = self.mobs_list_hp[self.enemy2]
                self.current_enemy_type.append(self.enemy2)
                self.current_enemies_alive_hp[1] = self.enemy2_max_hp

                self.enemy_2_sprite_img = character.enemy_color(self.enemy2)
                self.enemy_2_sprite = self.get_enemy_sprite(self.enemy2, self.enemy_2_sprite_img)
                self.enemy_2_sprite.get_frames()
                self.enemy_2_hp_bar = HealthBar(1030, 110, 140, 20, self.enemy2_max_hp)

            elif x == 2:
                self.enemy3 = character.random_enemy_type()
                self.enemy3_max_hp = self.mobs_list_hp[self.enemy3]
                self.current_enemy_type.append(self.enemy3)
                self.current_enemies_alive_hp[2] = self.enemy3_max_hp

                self.enemy_3_sprite_img = character.enemy_color(self.enemy3)
                self.enemy_3_sprite = self.get_enemy_sprite(self.enemy3, self.enemy_3_sprite_img)
                self.enemy_3_sprite.get_frames()
                self.enemy_3_hp_bar = HealthBar(1180, 160, 140, 20, self.enemy3_max_hp)

            elif x == 3:                
                self.enemy4 = character.random_enemy_type()
                self.enemy4_max_hp = self.mobs_list_hp[self.enemy4]
                self.current_enemy_type.append(self.enemy4)
                self.current_enemies_alive_hp[3] = self.enemy4_max_hp

                self.enemy_4_sprite_img = character.enemy_color(self.enemy4)
                self.enemy_4_sprite = self.get_enemy_sprite(self.enemy4, self.enemy_4_sprite_img)
                self.enemy_4_sprite.get_frames()
                self.enemy_4_hp_bar = HealthBar(1330, 110, 140, 20, self.enemy4_max_hp)
        
        for x in range(4 - enemy_count):
            if x == 0:
                self.enemy_4_hp_bar = HealthBar(1330, 110, 140, 20, 0)
            elif x == 1:
                self.enemy_3_hp_bar = HealthBar(1180, 160, 140, 20, 0)
            elif x == 2:
                self.enemy_2_hp_bar = HealthBar(1030, 110, 140, 20, 0)

        self.amount_of_enemies = enemy_count
    
    def check_enemy_type_offset(self, enemy_type):
        match enemy_type:
            case 'skeleton':
                self.x_offset = 180
                self.y_offset = 150
            case 'zombie':
                self.x_offset = 180
                self.y_offset = 180
            case 'orc':
                self.x_offset = 100
                self.y_offset = 100
            case 'goblin':
                self.x_offset = 180
                self.y_offset = 160

    def display_enemy(self):
        self.combat_layer.fill(KEY_GREEN)
        self.selection_layer.fill(KEY_GREEN)

        for enemy in range(self.amount_of_enemies):
            if enemy == 0 and self.current_enemies_alive_hp[enemy] > 0:
                pygame.draw.rect(self.combat_layer, (0,0,0), (875, 155, 150, 30))
                self.enemy_1_hp_bar.draw(self.combat_layer)
                self.check_enemy_type_offset(self.enemy1)
                self.enemy_1_sprite.display_sprite(900-self.x_offset, 200-self.y_offset)

            elif enemy == 1 and self.current_enemies_alive_hp[enemy] > 0:
                pygame.draw.rect(self.combat_layer, (0,0,0), (1025, 105, 150, 30))
                self.enemy_2_hp_bar.draw(self.combat_layer)
                self.check_enemy_type_offset(self.enemy2)
                self.enemy_2_sprite.display_sprite(1050-self.x_offset, 150-self.y_offset)

            elif enemy == 2 and self.current_enemies_alive_hp[enemy] > 0:
                pygame.draw.rect(self.combat_layer, (0,0,0), (1175, 155, 150, 30))
                self.enemy_3_hp_bar.draw(self.combat_layer)
                self.check_enemy_type_offset(self.enemy3)
                self.enemy_3_sprite.display_sprite(1200-self.x_offset, 200-self.y_offset)

            elif enemy == 3 and self.current_enemies_alive_hp[enemy] > 0:
                pygame.draw.rect(self.combat_layer, (0,0,0), (1325, 105, 150, 30))
                self.enemy_4_hp_bar.draw(self.combat_layer)
                self.check_enemy_type_offset(self.enemy4)
                self.enemy_4_sprite.display_sprite(1350-self.x_offset, 150-self.y_offset)
        
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
                self.enemy_1_hp_bar.current_hp -= damage_dealt
                self.current_enemies_alive_hp[0] = self.enemy_1_hp_bar.current_hp
                character.enemy_status(0)
            case 2:
                self.enemy_2_hp_bar.current_hp -= damage_dealt
                self.current_enemies_alive_hp[1] = self.enemy_2_hp_bar.current_hp
                character.enemy_status(1)
            case 3:
                self.enemy_3_hp_bar.current_hp -= damage_dealt
                self.current_enemies_alive_hp[2] = self.enemy_3_hp_bar.current_hp
                character.enemy_status(2)
            case 4:
                self.enemy_4_hp_bar.current_hp -= damage_dealt
                self.current_enemies_alive_hp[3] = self.enemy_4_hp_bar.current_hp
                character.enemy_status(3)
    
    def do_damage_AOE(self, damage_dealt):
        self.enemy_1_hp_bar.current_hp -= damage_dealt
        self.current_enemies_alive_hp[0] = self.enemy_1_hp_bar.current_hp
        character.enemy_status(0)

        self.enemy_2_hp_bar.current_hp -= damage_dealt
        self.current_enemies_alive_hp[1] = self.enemy_2_hp_bar.current_hp
        character.enemy_status(1)

        self.enemy_3_hp_bar.current_hp -= damage_dealt
        self.current_enemies_alive_hp[2] = self.enemy_3_hp_bar.current_hp
        character.enemy_status(2)

        self.enemy_4_hp_bar.current_hp -= damage_dealt
        self.current_enemies_alive_hp[3] = self.enemy_4_hp_bar.current_hp
        character.enemy_status(3)

    def enemy_turn(self):
        for current_enemy_attacking in range(self.amount_of_enemies):
            if self.current_enemy_type[current_enemy_attacking] in enemy.enemy_types:
                if self.current_enemies_alive_hp[current_enemy_attacking] != 0:
                    enemy.enemy_actions(self.current_enemy_type[current_enemy_attacking])
                time.sleep(1)
        character.battle_win()

# PLAYER RELATED FUNCTIONS --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

    def player_initalizer(self):
        self.player_hp_health_bar = HealthBar(280, 160, 140, 20, 50)
        self.player_hp_health_bar.current_hp = battle_data.current_health[0]
        self.player_sprite_img = get_image('Assets/Wizard Pack/Idle.png', 2)
        self.player_sprite = General_Spritesheet(self.player_sprite_img, 1386, 190, 6, 2, 200, self.selection_layer)
        self.player_sprite.get_frames()

    def player_displayer(self):
        pygame.draw.rect(self.combat_layer, (0,0,0), (275, 155, 150, 30))
        self.player_hp_health_bar.draw(self.combat_layer)
        self.player_sprite.display_sprite(140, 90)

    def player_heal(self, hp_healed, hp_change=0):
        hp_change = int(battle_data.current_health[0])
        hp_change += hp_healed
        battle_data.current_health[0] = hp_change
        if battle_data.current_health[0] > 50:
            battle_data.current_health[0] = 50
        self.player_hp_health_bar.current_hp = battle_data.current_health[0]
        self.player_hp_health_bar.draw(self.combat_layer)
    
    def player_damage(self, hp_damage, hp_change=0):
        hp_change = battle_data.current_health[0]
        hp_change -= hp_damage
        battle_data.current_health[0] = hp_change
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
    

class Enemy_Actions:
    def __init__ (self):
        self.enemy_types = ['skeleton', 'zombie', 'orc', 'goblin']
    
    def enemy_actions(self, enemy_doing_action):
        match enemy_doing_action:
            case 'skeleton':
                skeleton_attack = random.randint(1,100)
                if skeleton_attack <= 67:
                    self.current_enemy_damage = random.randint(2,3)
                else: 
                    self.current_enemy_damage = random.randint(4,6)
                character.player_damage(self.current_enemy_damage)
                print(f"sekelton did {self.current_enemy_damage} damage")

            case 'zombie':
                self.current_enemy_damage = random.randint(2,4)
                character.player_damage(self.current_enemy_damage)
                print(f"zombie did {self.current_enemy_damage} damage")

            case 'orc':
                self.current_enemy_damage = random.randint(4,8)
                character.player_damage(self.current_enemy_damage)
                print(f"orc did {self.current_enemy_damage} damage")

            case 'goblin':
                self.current_enemy_damage = random.randint(1,3)
                character.player_damage(self.current_enemy_damage)
                print(f"goblin did {self.current_enemy_damage} damage")

        print(character.mob_list_type)

class Potions:
    def __init__(self):
        self.inventory_slot_1 = Button(80, 570, 115, 110, KEY_GREEN, YELLOW)
        self.inventory_slot_2 = Button(80, 710, 115, 110, KEY_GREEN, YELLOW)
        self.inventory_slot_3 = Button(1400, 570, 115, 110, KEY_GREEN, YELLOW)
        self.inventory_slot_4 = Button(1400, 710, 115, 110, KEY_GREEN, YELLOW)
    
    def display_inventory_buttons(self):
        if battle_data.inventory_slots[0] is not None:
            self.inventory_slot_1.draw(character.selection_layer)
        if battle_data.inventory_slots[1] is not None:
            self.inventory_slot_2.draw(character.selection_layer)
        if battle_data.inventory_slots[2] is not None:
            self.inventory_slot_3.draw(character.selection_layer)
        if battle_data.inventory_slots[3] is not None:
            self.inventory_slot_4.draw(character.selection_layer)

character = Character()
enemy = Enemy_Actions()
potions = Potions()