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

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.rect)  # Fill the rect with the color
        else:
            pygame.draw.rect(screen, self.button_color, self.rect)  # Fill the rect with the color

    def is_clicked(self, mouse_pos):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            return True
        return False


class Character:
    def __init__(self):
        self.mobs_list_color = {'skeleton': WHITE, 'zombie': DARK_GREEN, 'orc':DARK_RED , 'goblin': RED}
        self.mobs_list_hp = {'skeleton': 15, 'zombie': 10, 'orc': 20 , 'goblin': 10}
        self.combat_layer = pygame.Surface((1600,900))
        self.selection_layer = pygame.Surface((1600,900))
        self.selected_enemy = 0
        self.current_enemies_alive_hp = [0,0,0,0]
        self.current_enemy_type = []
        self.player_current_health = battle_data.current_health
        self.battle_state = None

    def random_enemy_type(self):
        self.mob_list_type = list(self.mobs_list_color.keys())
        return self.mob_list_type[random.randint(0,3)]
    
    def enemy_color(self, enemy_type):
        self.enemy_clr = enemy_type
        return self.enemy_clr
    
    def enemy_hp(self, enemy_hp):
        self.current_enemy_hp = enemy_hp
        return self.current_enemy_hp
    
    def is_alive(self, enemy_hp):
        if enemy_hp > 0:
            return True
        else:
            return False
    
    def enemy_initalizer(self, enemy_count:int):
        for x in range(enemy_count):
            if x == 0:
                self.enemy1 = character.random_enemy_type()
                self.enemy1_max_hp = self.mobs_list_hp[character.enemy_color(self.enemy1)]
                self.current_enemy_type.append(self.enemy1)
                self.current_enemies_alive_hp[0] = self.enemy1_max_hp
                self.enemy_1_hp_bar = HealthBar(880, 160, 140, 20, self.enemy1_max_hp)

            elif x == 1:
                self.enemy2 = character.random_enemy_type()
                self.enemy2_max_hp = self.mobs_list_hp[character.enemy_color(self.enemy2)]
                self.current_enemy_type.append(self.enemy2)
                self.current_enemies_alive_hp[1] = self.enemy2_max_hp
                self.enemy_2_hp_bar = HealthBar(1030, 110, 140, 20, self.enemy2_max_hp)

            elif x == 2:
                self.enemy3 = character.random_enemy_type()
                self.enemy3_max_hp = self.mobs_list_hp[character.enemy_color(self.enemy3)]
                self.current_enemy_type.append(self.enemy3)
                self.current_enemies_alive_hp[2] = self.enemy3_max_hp
                self.enemy_3_hp_bar = HealthBar(1180, 160, 140, 20, self.enemy3_max_hp)

            elif x == 3:                
                self.enemy4 = character.random_enemy_type()
                self.enemy4_max_hp = self.mobs_list_hp[character.enemy_color(self.enemy4)]
                self.current_enemy_type.append(self.enemy4)
                self.current_enemies_alive_hp[3] = self.enemy4_max_hp
                self.enemy_4_hp_bar = HealthBar(1330, 110, 140, 20, self.enemy4_max_hp)
        
        for x in range(4 - enemy_count):
            if x == 0:
                self.enemy_4_hp_bar = HealthBar(1330, 110, 140, 20, 0)
            elif x == 1:
                self.enemy_3_hp_bar = HealthBar(1180, 160, 140, 20, 0)
            elif x == 2:
                self.enemy_2_hp_bar = HealthBar(1030, 110, 140, 20, 0)

        self.amount_of_enemies = enemy_count

    def display_enemy(self):
        self.combat_layer.fill(KEY_GREEN)
        self.selection_layer.fill(KEY_GREEN)

        for enemy in range(self.amount_of_enemies):
            if enemy == 0 and self.current_enemies_alive_hp[enemy] > 0:
                pygame.draw.rect(self.combat_layer, (0,0,0), (875, 155, 150, 30))
                self.enemy_1_hp_bar.draw(self.combat_layer)
                pygame.draw.rect(self.combat_layer, self.mobs_list_color[character.enemy_color(self.enemy1)], (900, 200, 100, 200))

            elif enemy == 1 and self.current_enemies_alive_hp[enemy] > 0:
                pygame.draw.rect(self.combat_layer, (0,0,0), (1025, 105, 150, 30))
                self.enemy_2_hp_bar.draw(self.combat_layer)
                pygame.draw.rect(self.combat_layer, self.mobs_list_color[character.enemy_color(self.enemy2)], (1050, 150, 100, 200))

            elif enemy == 2 and self.current_enemies_alive_hp[enemy] > 0:
                pygame.draw.rect(self.combat_layer, (0,0,0), (1175, 155, 150, 30))
                self.enemy_3_hp_bar.draw(self.combat_layer)
                pygame.draw.rect(self.combat_layer, self.mobs_list_color[character.enemy_color(self.enemy3)], (1200, 200, 100, 200))

            elif enemy == 3 and self.current_enemies_alive_hp[enemy] > 0:
                pygame.draw.rect(self.combat_layer, (0,0,0), (1325, 105, 150, 30))
                self.enemy_4_hp_bar.draw(self.combat_layer)
                pygame.draw.rect(self.combat_layer, self.mobs_list_color[character.enemy_color(self.enemy4)], (1350, 150, 100, 200))
        
        #Draw Buttons for Enemies
        self.enemy_1_selector = Button(900, 200, 100, 200, KEY_GREEN, YELLOW)
        self.enemy_1_selector.draw(self.selection_layer)

        self.enemy_2_selector = Button(1050, 150, 100, 200, KEY_GREEN, YELLOW)
        self.enemy_2_selector.draw(self.selection_layer)

        self.enemy_3_selector = Button(1200, 200, 100, 200, KEY_GREEN, YELLOW)
        self.enemy_3_selector.draw(self.selection_layer)

        self.enemy_4_selector = Button(1350, 150, 100, 200, KEY_GREEN, YELLOW)
        self.enemy_4_selector.draw(self.selection_layer)

    def enemy_status(self, current_enemy_status:int):
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
        character.battle_loss()

# PLAYER RELATED FUNCTIONS --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

    def player_initalizer(self):
        self.player_hp_health_bar = HealthBar(280, 160, 140, 20, 50)
        self.player_hp_health_bar.current_hp = self.player_current_health[0]
        self.player_sprite_img = get_image('Assets/Wizard Pack/Idle.png', 2)
        self.player_sprite = General_Spritesheet(self.player_sprite_img, 1386, 190, 6, 2, self.selection_layer, 140, 90)
        self.player_sprite.get_frames()

    def player_displayer(self):
        pygame.draw.rect(self.combat_layer, (0,0,0), (275, 155, 150, 30))
        self.player_hp_health_bar.draw(self.combat_layer)
        self.player_sprite.display_sprite()

    def player_heal(self, hp_healed, hp_change=0):
        hp_change = self.player_current_health[0]
        hp_change += hp_healed
        self.player_current_health[0] = hp_change
        if self.player_current_health[0] > 50:
            self.player_current_health[0] = 50
        self.player_hp_health_bar.current_hp = self.player_current_health[0]
        self.player_hp_health_bar.draw(self.combat_layer)
    
    def player_damage(self, hp_damage, hp_change=0):
        hp_change = self.player_current_health[0]
        hp_change -= hp_damage
        self.player_current_health[0] = hp_change
        self.player_hp_health_bar.current_hp = self.player_current_health[0]
        self.player_hp_health_bar.draw(self.combat_layer)
    
    def battle_win(self):
        self.total_enemy_hp = 0
        for enemy_hp in range(self.amount_of_enemies):
            self.total_enemy_hp += self.current_enemies_alive_hp[enemy_hp]
        
        if self.total_enemy_hp == 0:
            self.battle_state = 'WIN'
            battle_data.current_health = self.player_current_health
            music.Battle_BGM_1_stop()
    
    def battle_loss(self):
        if self.player_current_health[0] < 0:
            print("You Died")
        else:
            print(f"You have {self.player_current_health[0]} Hp Left")

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

character = Character()
enemy = Enemy_Actions()
