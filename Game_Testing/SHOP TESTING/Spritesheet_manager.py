import pygame
import time

PURPLE = (255, 0 , 255)
run = True
clock = pygame.time.Clock()

animation_list_1 = []
animations_steps_1 = [15]
last_update_1 = pygame.times.get_ticks()
actions_1 = 0
frame_1 = 0
step_counter_1 = 0
animations_cooldown = 75


def get_image(img:str, scale):
    image = pygame.image.load(img).convert_alpha()
    image = pygame.transform.scale_by(image, scale)
    return image

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image
    
    def get_potion_sprites(self):
        self.potions_display_positions = [(900, 450)]
    def shop_potion_sprite(self, WIDTH=1600, HEIGHT=900):
        self.potion_sprite = pygame.Surface((WIDTH,HEIGHT)).convert_alpha()
        self.potion_sprite.fill(PURPLE)
    def rolling_action():
        for animation_1 in animations_steps_1:
            temp_img_list_1
    def frame_rolling():
    

while run:
    current_time_1 = pygame.time.get_ticks()
    if current_time_1 - last_update_1 >= animations_cooldown:
        frame_1 += 1
        last_update_1 = current_time_1
        if frame_1 >= len(animation_list_1[actions_1]):
            frame_1 = 0