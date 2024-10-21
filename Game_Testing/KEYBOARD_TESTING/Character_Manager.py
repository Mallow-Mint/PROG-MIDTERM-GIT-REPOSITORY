import pygame
import random

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


class Character:
    def __init__(self):
        self.mobs_list_color = {'skeleton': WHITE, 'zombie': DARK_GREEN, 'orc':DARK_RED , 'goblin': RED}
        self.mobs_list_hp = {'skeleton': 15, 'zombie': 10, 'orc': 20 , 'goblin': 10}
        self.combat_layer = pygame.Surface((1600,900))
        self.current_enemies_alive_hp = []

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
                self.current_enemies_alive_hp.append(self.enemy1_max_hp)
                self.enemy_1_hp_bar = HealthBar(880, 160, 140, 20, self.enemy1_max_hp)

            elif x == 1:
                self.enemy2 = character.random_enemy_type()
                self.enemy2_max_hp = self.mobs_list_hp[character.enemy_color(self.enemy2)]
                self.current_enemies_alive_hp.append(self.enemy2_max_hp)
                self.enemy_2_hp_bar = HealthBar(1030, 110, 140, 20, self.enemy1_max_hp)

            elif x == 2:
                self.enemy3 = character.random_enemy_type()
                self.enemy3_max_hp = self.mobs_list_hp[character.enemy_color(self.enemy3)]
                self.current_enemies_alive_hp.append(self.enemy3_max_hp)
                self.enemy_3_hp_bar = HealthBar(1180, 160, 140, 20, self.enemy1_max_hp)

            elif x == 3:                
                self.enemy4 = character.random_enemy_type()
                self.enemy4_max_hp = self.mobs_list_hp[character.enemy_color(self.enemy4)]
                self.current_enemies_alive_hp.append(self.enemy4_max_hp)
                self.enemy_4_hp_bar = HealthBar(1330, 110, 140, 20, self.enemy1_max_hp)
    
    def display_enemy(self):
        self.amount_of_enemies = len(self.current_enemies_alive_hp)
        for enemy in range(self.amount_of_enemies):
            if enemy == 0:
                self.enemy_1_hp_bar.draw(self.combat_layer)
                pygame.draw.rect(self.combat_layer, self.mobs_list_color[character.enemy_color(self.enemy1)], (900, 200, 100, 200))

            elif enemy == 1:
                self.enemy_2_hp_bar.draw(self.combat_layer)
                pygame.draw.rect(self.combat_layer, self.mobs_list_color[character.enemy_color(self.enemy2)], (1050, 150, 100, 200))

            elif enemy == 2:
                self.enemy_3_hp_bar.draw(self.combat_layer)
                pygame.draw.rect(self.combat_layer, self.mobs_list_color[character.enemy_color(self.enemy3)], (1200, 200, 100, 200))

            elif enemy == 3:
                self.enemy_4_hp_bar.draw(self.combat_layer)
                pygame.draw.rect(self.combat_layer, self.mobs_list_color[character.enemy_color(self.enemy4)], (1350, 150, 100, 200))

    def do_damage_single_target(self, damage_dealt, enemy_targeted):
        match enemy_targeted:
            case 1:
                self.enemy_1_hp_bar.current_hp -= damage_dealt
                self.current_enemies_alive_hp[0] = self.enemy_1_hp_bar.current_hp
            case 2:
                self.enemy_2_hp_bar.current_hp -= damage_dealt
                self.current_enemies_alive_hp[1] = self.enemy_2_hp_bar.current_hp
            case 3:
                self.enemy_3_hp_bar.current_hp -= damage_dealt
                self.current_enemies_alive_hp[2] = self.enemy_3_hp_bar.current_hp
            case 4:
                self.enemy_4_hp_bar.current_hp -= damage_dealt
                self.current_enemies_alive_hp[3] = self.enemy_4_hp_bar.current_hp

    def player_initalizer(self, hp=40):
        self.player_hp_health_bar = HealthBar(280, 160, 140, 20, hp)
        self.player_hp_health_bar.draw(self.combat_layer)
        pygame.draw.rect(self.combat_layer, BLUE, (300, 200, 100, 200))


character = Character()


