import pygame

class Music():
    def __init__(self):
        pass
    def shop_bg_music(self):
        shop_music = pygame.mixer.Sound('Game_Testing/SHOP TESTING/Assets/Stardew Valley OST.mp3')
        shop_music.play(-1)

    def buy_music(self):
        buy_sound = pygame.mixer.Sound('Game_Testing/SHOP TESTING/Assets/buying sfx.mp3')
        buy_sound.play()

    def shop_bg_music(self):
        shop_music = pygame.mixer.Sound('Game_Testing/SHOP TESTING/Assets/Stardew Valley OST.mp3')
        shop_music.play(-1)

    def buy_music(self):
        buy_sound = pygame.mixer.Sound('Game_Testing/SHOP TESTING/Assets/buying sfx.mp3')
        buy_sound.play()
        
music = Music()