import pygame
import time
from states.battle_data.battle_data import *

pygame.init()
#Colors 
GREEN = (30, 255, 0)
KEY_PURPLE = (255, 0, 255)

potion_layer = pygame.Surface((1600,900))
background_layer = pygame.Surface((1600,900))


def get_image(img:str, scale=1):
    if scale == 1:
        image = pygame.image.load(img)
        return image
    else:
        image = pygame.image.load(img)
        image = pygame.transform.scale_by(image, scale)
        return image
        
class KeyboardSprites:
    def __init__(self, image):  
        self.sheet = image

    def get_keyboard_sprites(self):
        self.keyboard_default_key_sprite = []
        self.keyboard_pressed_key_sprite = []
        self.sprite_display_positions = [(252,540), (360, 540), (468,540), (576, 540), (684, 540), (792,540), (900,540), (1008,540), (1116,540), (1224,540),
                                         (300,642), (408, 642), (516,642), (624,642), (732,642), (840,642), (948, 642), (1056,642), (1164,642),
                                         (408,744), (516,744), (624,744), (732,744), (840,744), (948,744), (1056,744)]
        self.qwerty_number = 0
        self.sprite_mover = 0

        for key in battle_data.valid_letters:
            self.keyboard_default_key_sprite.append((0 + (204*self.qwerty_number), 0 , 102, 96))
            self.keyboard_pressed_key_sprite.append((102 + (204*self.qwerty_number), 0 , 102, 96))
            self.qwerty_number += 1
        
    def keyboard_default_sprite(self, WIDTH=1600, HEIGHT=900):
        self.keyboard_sprites = pygame.Surface((WIDTH,HEIGHT))
        self.keyboard_sprites.fill(GREEN)
        for key, amount in battle_data.Keys_Remaining.items():
            if amount > 0:
                key_index = battle_data.valid_letters.index(key)
                self.keyboard_sprites.blit(self.sheet, self.sprite_display_positions[0+key_index], 
                                            self.keyboard_default_key_sprite[0+key_index])
        return self.keyboard_sprites
    
    def pressed_key_animation(self, key, WIDTH=1600, HEIGHT=900):
        self.keyboard_sprites = pygame.Surface((WIDTH,HEIGHT))
        self.keyboard_sprites.fill(GREEN)
        self.pressed_key_index = battle_data.valid_letters.index(key)

        for key, amount in battle_data.Keys_Remaining.items():
            if amount > 0:
                key_index = battle_data.valid_letters.index(key)
                self.keyboard_sprites.blit(self.sheet, self.sprite_display_positions[0+key_index], 
                                            self.keyboard_default_key_sprite[0+key_index])

        self.keyboard_sprites.blit(self.sheet, self.sprite_display_positions[self.pressed_key_index], 
                                   self.keyboard_pressed_key_sprite[self.pressed_key_index])
        
        return self.keyboard_sprites

class General_Spritesheet:
    def __init__(self, image, width, height, frame_count, scale, cooldown, layer):
        self.sheet = image
        self.width = width
        self.height = height
        self.scale = scale
        self.frames = frame_count
        self.layer = layer
        self.current_frame = 0
        self.current_time_1 = 0
        self.animation_cooldown = cooldown
        self.last_update_1 = pygame.time.get_ticks()
        self.get_frames()

    def get_frames(self):
        scaled_width = self.width * self.scale
        scaled_height = self.height * self.scale
        self.frame_coordinates = []
        for animation_frame in range(self.frames):
            current_frame = ((scaled_width/self.frames) * animation_frame, 0, (scaled_width/self.frames) , scaled_height)
            self.frame_coordinates.append(current_frame)
    
    def get_single_frame(self, frame, x_pos, y_pos):
        self.layer.blit(self.sheet, (x_pos, y_pos), self.frame_coordinates[frame])

    def get_current_sprite(self):
        if self.current_time_1 - self.last_update_1 >= self.animation_cooldown:
            self.current_frame += 1
            self.last_update_1 = self.current_time_1
            if self.current_frame >= self.frames:
                self.current_frame = 0
    
    def display_sprite(self, x_pos, y_pos):
        self.current_time_1 = pygame.time.get_ticks()
        self.get_current_sprite()
        self.get_single_frame(self.current_frame, x_pos, y_pos)

class Spell_Spritesheet:
    def __init__(self, image, width, height, frame_count_per_row, amount_of_rows, scale, cooldown, layer):
        self.sheet = image
        self.width = width
        self.height = height
        self.scale = scale
        self.frames_per_row = frame_count_per_row
        self.amount_of_rows = amount_of_rows
        self.layer = layer
        self.current_frame = 0
        self.current_time_1 = 0
        self.animation_cooldown = cooldown
        self.last_update_1 = pygame.time.get_ticks()
        self.get_frames()

    def get_frames(self):
        scaled_width = self.width * self.scale
        scaled_height = self.height * self.scale
        self.frame_coordinates = []
        for row in range(self.amount_of_rows):
            for animation_frame in range(self.frames_per_row):
                current_frame = ((scaled_width/self.frames_per_row) * animation_frame, (scaled_height/self.amount_of_rows) * row, (scaled_width/self.frames_per_row) , scaled_height/self.amount_of_rows)
                self.frame_coordinates.append(current_frame)
    
    def get_single_frame(self, row , frame_on_row, pos):
        self.layer.blit(self.sheet, pos, self.frame_coordinates[(self.frames_per_row * row) + frame_on_row])

    def get_current_sprite(self):
        if self.current_time_1 - self.last_update_1 >= self.animation_cooldown:
            self.current_frame += 1
            self.last_update_1 = self.current_time_1
            if self.current_frame >= self.frames_per_row:
                self.current_frame = 0
    
    def display_sprite(self, color , pos):
        '''
        COLOR CODE
        0 = Orange
        1 = Purple
        2 = Light Blue
        3 = Green
        4 = Brown
        5 = White
        6 = Light Purple
        7 = Red
        8 = Dark Blue
        '''
        self.current_time_1 = pygame.time.get_ticks()
        self.get_current_sprite()
        self.get_single_frame(color, self.current_frame, pos)