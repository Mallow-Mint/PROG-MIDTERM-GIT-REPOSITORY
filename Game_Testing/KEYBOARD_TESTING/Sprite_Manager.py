import pygame

#Color
GREEN = (30, 255, 0)

class Keyboard:
    def __init__(self) -> None:
        self.valid_letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 
                              'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                              'z', 'x', 'c', 'v', 'b', 'n', 'm' ]
        
        
class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_keyboard_sprites(self):
        self.keyboard_default_key_sprite = []
        self.keyboard_pressed_key_sprite = []
        self.sprite_display_positions = [(42,80), (60, 80), (78,80), (96, 80), (114,80), (132,80), (150,80), (168,80), (186,80), (204,80),
                                         (50,97), (68, 97), (86,97), (104,97), (122,97), (140,97), (158, 97), (176,97), (194,97),
                                         (68,114), (86,114), (104,114), (122,114), (140,114), (158,114), (176,114)]

        self.qwerty_number = 0
        self.sprite_mover = 0

        for key in keyboard.valid_letters:
            self.keyboard_default_key_sprite.append((0 + (34*self.qwerty_number), 0 , 17, 16))
            self.keyboard_pressed_key_sprite.append((17 + (34*self.qwerty_number), 0 , 17, 16))
            self.qwerty_number += 1
        
    def keyboard_default_sprite(self, scale ,WIDTH=1600, HEIGHT=900):
        self.sprite_mover = 0
        self.keyboard_sprites = pygame.Surface((WIDTH,HEIGHT)).convert_alpha()
        for key in keyboard.valid_letters:
            self.keyboard_sprites.blit(self.sheet, self.sprite_display_positions[0+self.sprite_mover], 
                                          self.keyboard_default_key_sprite[0+self.sprite_mover])
            self.sprite_mover += 1
        self.keyboard_sprites = pygame.transform.scale(self.keyboard_sprites, (WIDTH*scale, HEIGHT*scale))
        return self.keyboard_sprites
    
    def pressed_key_animation(self, key, scale, WIDTH=1600, HEIGHT=900):
        self.keyboard_sprites = pygame.Surface((WIDTH,HEIGHT)).convert_alpha()
        self.pressed_key_index = keyboard.valid_letters.index(key)
        self.sprite_mover = 0

        for key in keyboard.valid_letters:
            self.keyboard_sprites.blit(self.sheet, self.sprite_display_positions[0+self.sprite_mover], 
                                          self.keyboard_default_key_sprite[0+self.sprite_mover])
            self.sprite_mover += 1

        self.keyboard_sprites.blit(self.sheet, self.sprite_display_positions[self.pressed_key_index], 
                                   self.keyboard_pressed_key_sprite[self.pressed_key_index])
        
        self.keyboard_sprites = pygame.transform.scale(self.keyboard_sprites, (WIDTH*scale, HEIGHT*scale))
        return self.keyboard_sprites

keyboard = Keyboard()
