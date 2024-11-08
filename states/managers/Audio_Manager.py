import pygame

class Music:
    def __init__(self):
        pass

    def Battle_BGM_1(self):
        self.fight_bg_music_1 = pygame.mixer.Sound('Assets/fight_music.mp3')
        self.fight_bg_music_1.set_volume(0.1)
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
        self.menu_music.set_volume(0.5)
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
    
    def air_spell_sound(self):
        air_spell_sfx = pygame.mixer.Sound('Assets/Sound Effects/sfx air slash.mp3')
        air_spell_sfx.set_volume(1)
        air_spell_sfx.play()
    
    def fire_AOE_spell_sound(self):
        fire_AOE = pygame.mixer.Sound('Assets/Sound Effects/Fireball sound effect.mp3')
        fire_AOE.set_volume(1)
        fire_AOE.play()
    
    def fireball_spell_sound(self):
        fireball_sfx = pygame.mixer.Sound('Assets/Sound Effects/fireball sfx.mp3')
        fireball_sfx.set_volume(1)
        fireball_sfx.play()

    def snow_spell_sound(self):
        snow_sfx = pygame.mixer.Sound('Assets/Sound Effects/Ice Spell Sound.mp3')
        snow_sfx.set_volume(1)
        snow_sfx.play()

    def freeze_spell_sound(self):
        freeze_sfx = pygame.mixer.Sound('Assets/Sound Effects/freeze.mp3')
        freeze_sfx.set_volume(1)
        freeze_sfx.play()
    
    def light_beam_sound(self):
        light_beam_sfx = pygame.mixer.Sound('Assets/Sound Effects/laser sound.mp3')
        light_beam_sfx.set_volume(1)
        light_beam_sfx.play()

    def quasar_sound(self):
        quasar_sfx = pygame.mixer.Sound('Assets/Sound Effects/quasar_sfx.mp3')
        quasar_sfx.set_volume(1)
        quasar_sfx.play()

    def heal_sound(self):
        heal_sfx = pygame.mixer.Sound('Assets/Sound Effects/heal_sfx.mp3')
        heal_sfx.set_volume(1)
        heal_sfx.play()

    def FAKER(self):
        water_spell_sfx = pygame.mixer.Sound('Assets/Sound Effects/SHOCKWAVE.mp3')
        water_spell_sfx.set_volume(1)
        water_spell_sfx.play()


music = Music()
sfx =  SoundEffects()
#Single Target Spells SFX - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

water_spell_single_target_sfx = sfx.water_spell_sound
air_spell_single_target_sfx = sfx.air_spell_sound
fireball_single_target_sfx = sfx.fireball_spell_sound
snow_single_target_sfx = sfx.snow_spell_sound
freeze_single_target_sfx = sfx.freeze_spell_sound
light_beam_single_target_sfx = sfx.light_beam_sound


spell_sfx_single_target = {"water": water_spell_single_target_sfx,
                           "wet": water_spell_single_target_sfx,
                           "acid": water_spell_single_target_sfx,
                           "air": air_spell_single_target_sfx, 
                           "airslice": air_spell_single_target_sfx,
                           "airstrike": air_spell_single_target_sfx,
                           "fireball": fireball_single_target_sfx,
                           "firebolt": fireball_single_target_sfx,
                           "icewall": snow_single_target_sfx,
                           "ice": snow_single_target_sfx,
                           "freeze": freeze_single_target_sfx,
                           "burn": fireball_single_target_sfx,
                           "fire": fireball_single_target_sfx,
                           "hot": fireball_single_target_sfx,
                           "lava": fireball_single_target_sfx,
                           "lightbeam": light_beam_single_target_sfx,
                           "light": light_beam_single_target_sfx,
                           

                           }

#Aoe Spells - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

firestorm_spell_AOE_targe_sfx = sfx.fire_AOE_spell_sound
quasar_spell_AOE_target_sfx = sfx.quasar_sound

spell_sfx_AOE_target = {"firestorm": firestorm_spell_AOE_targe_sfx,
                        "heatwave": firestorm_spell_AOE_targe_sfx,
                        "explosion": firestorm_spell_AOE_targe_sfx,
                        "quasar": quasar_spell_AOE_target_sfx

                        }

heal_spell_Heal_sfx = sfx.heal_sound

spell_sfx_Heal = {"heal": heal_spell_Heal_sfx}

