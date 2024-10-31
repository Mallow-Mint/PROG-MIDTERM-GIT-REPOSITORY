import pygame
import time

PURPLE = (255, 0 , 255)
run = True
clock = pygame.time.Clock()
animations_cooldown = 75

def get_image(img:str, scale):
    image = pygame.image.load(img).convert_alpha()
    image = pygame.transform.scale_by(image, scale)
    return image

class Spritesheet():
    def __init__(self, image):
        self.sheet = image
    
    def get_potion_sprites_1(self):
        self.animation_list_1 = []
        self.animations_steps_1 = [15]
        self.last_update_1 = pygame.time.get_ticks()
        self.action_1 = 0
        self.frame_1 = 0
        self.step_counter_1 = 0
        self.potion_1_cordinates = [800, 450]
    def Rollinganimation_1(self, WIDTH=1600, HEIGHT = 900):
        self.potion_1_sprites = pygame.Surface((WIDTH, HEIGHT)).convert_alpha()
        self.potion_1_sprites.fill(PURPLE)
        for animation_1 in self.animations_steps_1:
            temp_img_list_1 = []
            for _ in range(animation_1):
                img_1 = self.sheet# Adjust parameters as needed
                if img_1 is not None:  # Ensure we have a valid image
                    temp_img_list_1.append(img_1)
                self.step_counter_1 += 1
        self.animation_list_1.append(temp_img_list_1)
        while run:
            self.current_time_1 = pygame.time.get_ticks()
            if self.current_time_1 - self.last_update_1 >= animations_cooldown:
                self.frame_1 += 1
                self.last_update_1 = self.current_time_1
                if self.frame_1 >= len(self.animation_list_1[self.action_1]):
                    self.frame_1 = 0
        self.potion_1_sprites.blit(self.sheet, self.potion_1_cordinates)
        
        return self.potion_1_sprites
