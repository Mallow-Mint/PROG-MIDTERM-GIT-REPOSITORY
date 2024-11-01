import pygame
import time

#Colors 
GREEN = (30, 255, 0)

def get_image(img:str, scale):
    image = pygame.image.load(img)
    image = pygame.transform.scale_by(image, scale)
    return image

class Keyboard:
    def __init__(self) -> None:
        self.valid_letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 
                              'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                              'z', 'x', 'c', 'v', 'b', 'n', 'm' ]
class KeyboardSprites():
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

        for key in keyboard.valid_letters:
            self.keyboard_default_key_sprite.append((0 + (204*self.qwerty_number), 0 , 102, 96))
            self.keyboard_pressed_key_sprite.append((102 + (204*self.qwerty_number), 0 , 102, 96))
            self.qwerty_number += 1
        
    def keyboard_default_sprite(self, WIDTH=1600, HEIGHT=900):
        self.sprite_mover = 0
        self.keyboard_sprites = pygame.Surface((WIDTH,HEIGHT))
        self.keyboard_sprites.fill(GREEN)
        for key in keyboard.valid_letters:
            self.keyboard_sprites.blit(self.sheet, self.sprite_display_positions[0+self.sprite_mover], 
                                          self.keyboard_default_key_sprite[0+self.sprite_mover])
            self.sprite_mover += 1
        return self.keyboard_sprites
    
    def pressed_key_animation(self, key, WIDTH=1600, HEIGHT=900):
        self.keyboard_sprites = pygame.Surface((WIDTH,HEIGHT))
        self.keyboard_sprites.fill(GREEN)
        self.pressed_key_index = keyboard.valid_letters.index(key)
        self.sprite_mover = 0

        for key in keyboard.valid_letters:
            self.keyboard_sprites.blit(self.sheet, self.sprite_display_positions[0+self.sprite_mover], 
                                          self.keyboard_default_key_sprite[0+self.sprite_mover])
            self.sprite_mover += 1

        self.keyboard_sprites.blit(self.sheet, self.sprite_display_positions[self.pressed_key_index], 
                                   self.keyboard_pressed_key_sprite[self.pressed_key_index])
        
        return self.keyboard_sprites

keyboard = Keyboard()
