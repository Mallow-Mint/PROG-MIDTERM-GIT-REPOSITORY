import pygame

class Music:
    def __init__(self):
        pass

    def Battle_BGM_1(self):
        fight_bg_music_1 = pygame.mixer.Sound('Assets/fight_music.mp3')
        fight_bg_music_1.set_volume(0.05)
        fight_bg_music_1.play(-1,0,1000)

class SoundEffects:
    def __init__(self):
        pass

    def keyboard_press_sound(self):
        keyboard_press_sfx = pygame.mixer.Sound('Assets/keyboard_press.mp3')
        keyboard_press_sfx.set_volume(0.1)
        keyboard_press_sfx.play()

music = Music()
sfx =  SoundEffects()