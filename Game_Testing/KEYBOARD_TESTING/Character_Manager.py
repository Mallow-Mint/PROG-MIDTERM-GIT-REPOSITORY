import pygame
import random

RED = (255, 0, 0)
WHITE = (255, 255, 255)
DARK_GREEN = (0, 102, 17)
DARK_RED = (100, 0, 5)
BLUE = (0, 0, 145)
KEY_GREEN = (30, 255, 0)

class Character:
    def __init__(self):
        self.mobs_list = {'skeleton': WHITE, 'zombie': DARK_GREEN, 'orc':DARK_RED , 'goblin': RED}
        self.combat_layer = pygame.Surface((1600,900))

    def random_enemy_type(self):
        self.mob_list_type = list(self.mobs_list.keys())
        return self.mob_list_type[random.randint(0,3)]
    
    def enemy_color(self, enemy_type):
        self.enemy_clr = enemy_type
        return self.enemy_clr
    
    def enemy_initalizer(self, enemy_count:int):
        for x in range(enemy_count):
            if x == 0:
                self.enemy_1 = character.random_enemy_type()
                pygame.draw.rect(self.combat_layer, self.mobs_list[character.enemy_color(self.enemy_1)], (900, 200, 100, 200))
            elif x == 1:
                self.enemy_2 = character.random_enemy_type()
                pygame.draw.rect(self.combat_layer, self.mobs_list[character.enemy_color(self.enemy_2)], (1050, 150, 100, 200))
            elif x == 2:
                self.enemy_3 = character.random_enemy_type()
                pygame.draw.rect(self.combat_layer, self.mobs_list[character.enemy_color(self.enemy_3)], (1200, 200, 100, 200))
            elif x == 3:                
                self.enemy_4 = character.random_enemy_type()
                pygame.draw.rect(self.combat_layer, self.mobs_list[character.enemy_color(self.enemy_4)], (1350, 150, 100, 200))

    def player_initalizer(self):
        pygame.draw.rect(self.combat_layer, BLUE, (300, 200, 100, 200))

                
character = Character()


