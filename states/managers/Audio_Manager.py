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
        self.shop_music = pygame.mixer.Sound('Assets/Shop_Assets/Stardew Valley OST.mp3')
        self.shop_music.play(-1)

    def shop_bg_music_stop(self):
        self.shop_music.stop()

    def buy_music(self):
        buy_sound = pygame.mixer.Sound('Assets/Shop_Assets/buying sfx.mp3')
        buy_sound.play()
        
    def title_screen_music(self):
        self.menu_music = pygame.mixer.Sound('Assets/Background Music/title screen music.mp3')
        self.menu_music.set_volume(0.1)
        self.menu_music.play(-1, 0, 1000)
    def title_screen_music_stop(self):
        self.menu_music.stop()

class SoundEffects:
    def __init__(self):
        pass

    def keyboard_press_sound(self):
        keyboard_press_sfx = pygame.mixer.Sound('Assets/keyboard_press.mp3')
        keyboard_press_sfx.set_volume(0.1)
        keyboard_press_sfx.play()
    def fire_spell_sound(self):
        fire_spell_sfx = pygame.mixer.Sound('Assets/Sound Effects/Fireball sound effect.mp3')
        fire_spell_sfx.set_volume(1)
        fire_spell_sfx.play()

    def ice_spell_sound(self):
        ice_spell_sfx = pygame.mixer.Sound('Assets/Sound Effects/ice sound effect.mp3')
        ice_spell_sfx.set_volume(1)
        ice_spell_sfx.play()
    
    def acid_spell_sound(self):
        acid_spell_sfx = pygame.mixer.Sound('Assets/Sound Effects/acid sound effect.mp3')
        acid_spell_sfx.set_volume(1)
        acid_spell_sfx.play()
    
    def water_spell_sound(self):
        water_spell_sfx = pygame.mixer.Sound('Assets/Sound Effects/water sound effect.mp3')
        water_spell_sfx.set_volume(1)
        water_spell_sfx.play()
music = Music()
sfx =  SoundEffects()