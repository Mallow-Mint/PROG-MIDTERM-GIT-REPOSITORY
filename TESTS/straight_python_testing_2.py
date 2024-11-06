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

running = True
skeleton_attcking = False


def play_attack(sprite, attacking_sprite, x_pos, y_pos):
    sprite.layer.fill(BLACK)
    sprite.display_sprite(0,0)
    while sprite.current_frame > 0:
        sprite.layer.fill(BLACK)
        sprite.display_sprite(0,0)
        play_non_attacking(attacking_sprite, x_pos, y_pos)
        window.blit(display, (0,0))
        pygame.display.flip()

def play_non_attacking(sprite, x_pos, y_pos):
    sprite.display_sprite(x_pos,y_pos)
    

while running:
    display.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            if key == 'return':
                running = False
            elif key == 'left':
                play_attack(skeleton_attack_sprite, zombie_sprite, 300, 0)
            elif key == 'right':
                play_attack(zombie_attack_sprite, skeleton_sprite, 0, 0)


    skeleton_sprite.display_sprite(0,0)
    zombie_sprite.display_sprite(300,0)
    window.blit(display, (0,0))
    pygame.display.flip()
    