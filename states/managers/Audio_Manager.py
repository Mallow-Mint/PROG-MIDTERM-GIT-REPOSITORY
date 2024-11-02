import pygame

class Music:
    def __init__(self):
        pass

    def Battle_BGM_1(self):
        self.fight_bg_music_1 = pygame.mixer.Sound('Assets/fight_music.mp3')
        self.fight_bg_music_1.set_volume(0.05)
        self.fight_bg_music_1.play(-1,0,1000)
    
    def Battle_BGM_1_stop(self):
        self.fight_bg_music_1.stop()
    
    def shop_bg_music(self):
        shop_music = pygame.mixer.Sound('Game_Testing/SHOP TESTING/Assets/Stardew Valley OST.mp3')
        shop_music.play(-1)

    def buy_music(self):
        buy_sound = pygame.mixer.Sound('Game_Testing/SHOP TESTING/Assets/buying sfx.mp3')
        buy_sound.play()

class SoundEffects:
    def __init__(self):
        pass

    def keyboard_press_sound(self):
        keyboard_press_sfx = pygame.mixer.Sound('Assets/keyboard_press.mp3')
        keyboard_press_sfx.set_volume(0.1)
        keyboard_press_sfx.play()

music = Music()
sfx =  SoundEffects()