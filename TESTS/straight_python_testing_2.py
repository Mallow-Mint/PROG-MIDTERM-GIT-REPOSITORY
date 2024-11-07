import pygame
import random
from Sprite_Manager import *
from enemy_data import *
pygame.init()
BLACK = (0,0,0)
window = pygame.display.set_mode((800,800))
display = pygame.Surface((800,800))
skeleton_sprite = General_Spritesheet(skeleton_idle_img, 600, 150, 4, 3, 125, display)
skeleton_attack_img = get_image('Assets/Monsters/4 direction monsters/Skeleton/Attack.png', 3)
skeleton_attack_sprite = General_Spritesheet(skeleton_attack_img, 1200, 150, 8, 3, 100, display)

zombie_sprite = General_Spritesheet(zombie_idle_img, 600, 150, 4, 3, 125, display)
zombie_attack_img = get_image('Assets/Monsters/4 direction monsters/Mushroom/Attack.png', 3)
zombie_attack_sprite = General_Spritesheet(zombie_attack_img, 1200, 150, 8, 3, 100, display)

test_spell_img = get_image('Assets/Attack Effects/Free/Part 14/672.png', 4)
test_spell_sprite = Spell_Spritesheet(test_spell_img, 896, 576, 14, 9, 4, 100, display)
    

running = True
sprite_changer = 0
while running:
    display.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            if key == 'return':
                running = False
            if key == 'right':
                if sprite_changer < test_spell_sprite.amount_of_rows - 1:
                    sprite_changer += 1
                else:
                    sprite_changer = 0
            if key == 'left':
                if sprite_changer > 0:
                    sprite_changer -= 1
                else:
                    sprite_changer = test_spell_sprite.amount_of_rows - 1

    test_spell_sprite.display_sprite(sprite_changer, 0, 0)
    window.blit(display, (0,0))
    pygame.display.flip()
    