import pygame
from Sprite_Manager import *

# START PYGAME WOOOOO pygame
pygame.init()

# Create Display Window For Game
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

game_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Keyboard Battle")

# Set Colors used for Textures
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (130, 130, 130)
KEY_PURPLE = (255, 0, 255)
GREEN = (30, 255, 0)

#Get Sprites and sprite locations

keyboard_sprite_sheet_image = pygame.image.load('Assets/SimpleKeys/Classic/Light/Keys_Sprite_Sheet.png').convert_alpha()
keyboard_sprite_sheet = KeyboardSprites(keyboard_sprite_sheet_image)
keyboard_sprite_sheet.get_keyboard_sprites()

class Layers:
    def __init__(self):
        self.background_layer = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.keyboard_layer = keyboard_sprite_sheet.keyboard_default_sprite(6)
        self.keyboard_animation_cooldown = 200
        self.keyboard_update = pygame.time.get_ticks()

class Keyboard:
    def __init__(self):
        self.valid_letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 
                              'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                              'z', 'x', 'c', 'v', 'b', 'n', 'm' ]
        self.key_state = 1 #1 is default 0 is pressed
        
    def key_press_action(self, key:str,):
        self.pressed_key = key
        match self.pressed_key:
            case self.pressed_key if self.pressed_key in self.valid_letters:
                layer.keyboard_layer = keyboard_sprite_sheet.pressed_key_animation(self.pressed_key, 6)
                self.key_state = 0
                update_game_screen()
                while self.key_state < 1:
                    self.key_state += 1
                    layer.keyboard_layer = keyboard_sprite_sheet.keyboard_default_sprite(6)



layer = Layers()
keyboard = Keyboard()

def update_game_screen():
    '''
    Updates Game Window and associated Layers in order
    '''
    game_window.blit(layer.keyboard_layer, (0,0))
    pygame.display.flip()

def battle_interface():
    running = True
    frame_rate = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                keyboard.key_press_action(key)
        update_game_screen()
        frame_rate.tick(60)

battle_interface()