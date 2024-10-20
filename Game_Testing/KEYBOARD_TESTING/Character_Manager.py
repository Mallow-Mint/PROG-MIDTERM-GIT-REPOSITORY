import pygame
import random

RED = (255, 0, 0)
BLUE = (0, 0, 145)
WHITE = (255, 255, 255)
DARK_GREEN = (0, 102, 17)
DARK_RED = (100, 0, 5)
KEY_GREEN = (30, 255, 0)

class Character:
    def __init__(self):
        self.mobs_list = ['skeleton', 'zombie', 'orc', 'goblin']
        self.enemy_layer = pygame.Surface((1600,900))
        self.enemy_position = 0

        
    def enemy_initalizer(self, enemy_count):
        match enemy_count:
            case 1:
                self.enemy_1 = self.mobs_list[random.randint(0,3)]
            case 2:
                self.enemy_1 = self.mobs_list[random.randint(0,3)]
                self.enemy_2 = self.mobs_list[random.randint(0,3)]
            case 3:
                self.enemy_1 = self.mobs_list[random.randint(0,3)]
                self.enemy_2 = self.mobs_list[random.randint(0,3)]
                self.enemy_3 = self.mobs_list[random.randint(0,3)]
            case 4:
                self.enemy_1 = self.mobs_list[random.randint(0,3)]
                self.enemy_2 = self.mobs_list[random.randint(0,3)]
                self.enemy_3 = self.mobs_list[random.randint(0,3)]
                self.enemy_4 = self.mobs_list[random.randint(0,3)]
        
        while enemy_count > 0:
            if enemy_count % 2 == 0:
                pygame.draw.rect(self.enemy_layer, RED, (900 + (150*self.enemy_position), 200, 100, 200))
            else:
                pygame.draw.rect(self.enemy_layer, RED, (900 + (150*self.enemy_position), 150, 100, 200))
            enemy_count -=1
            self.enemy_position +=1
        self.enemy_position = 0
            
character = Character()

