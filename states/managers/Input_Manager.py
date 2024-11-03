import pygame
import random
import time
from states.managers.Battle_Manager import *
from states.managers.Audio_Manager import *

class Damage():
    def __init__(self):
        self.chain_word_damage_multipler = 1

    def damage_range_calculator(self, base_damage):
        self.damage_dealt = round(base_damage * random.uniform(0.8, 1.6), 0)
        self.damage_dealt = round(self.damage_dealt * self.chain_word_damage_multipler, 0)
        return int(self.damage_dealt)

    def critical_checker(self, damage_dealt):
        critical_test = random.randint(1,16)
        if critical_test == 16:
            damage_dealt = damage_dealt*2
        else:
            pass
        return damage_dealt
    
    def heal_spell(self, hp_healed):
        character.player_heal(hp_healed)
        spell.reset_damage()
        print(character.player_hp_health_bar.current_hp)

    def AOE_spell(self, damage_dealt):
        character.do_damage_AOE(damage_dealt)
        spell.reset_damage()
        print(character.current_enemies_alive_hp)

    
    def word_chain(self, previous_spell, current_spell):
        if previous_spell[-1] == current_spell[0]:
            self.chain_word_damage_multipler += 0.5
        else:
            self.chain_word_damage_multipler = 1
            spell.previous_spell = ' '

    def targeted_enemy(self, mouse_pos):
        self.current_click = mouse_pos

        if character.enemy_1_selector.is_clicked(self.current_click) == True and character.current_enemies_alive_hp[0] !=0:
            character.do_damage_single_target(spell.damage_dealt, 1)
            if spell.lifesteal == True:
                self.heal_spell(int(self.damage_dealt/2))
            spell.reset_damage()

        elif character.enemy_2_selector.is_clicked(self.current_click) == True and character.current_enemies_alive_hp[1] !=0:
            character.do_damage_single_target(spell.damage_dealt, 2)
            spell.reset_damage()

        elif character.enemy_3_selector.is_clicked(self.current_click) == True and character.current_enemies_alive_hp[2] !=0:
            character.do_damage_single_target(spell.damage_dealt, 3)
            spell.reset_damage()
            
        elif character.enemy_4_selector.is_clicked(self.current_click) == True and character.current_enemies_alive_hp[3] !=0:
            character.do_damage_single_target(spell.damage_dealt, 4)
            spell.reset_damage()

        print(character.current_enemies_alive_hp)
        character.battle_win()

class Spell:
    def __init__(self):
        #Get Valid Words from Text File
        self.shared_dictionary = open('states/battle_data/SpellBook.txt', "r")
        self.valid_words = self.shared_dictionary.read() 
        self.valid_words = self.valid_words.split("\n")
        self.shared_dictionary.close()
        self.previous_spell = ' '
        self.enemy_selection_state = False
        self.lifesteal = False
        self.damage_dealt = 0
        self.damage_healed = 0

    def reset_damage(self):
        self.enemy_selection_state = False
        self.lifesteal = False
        self.damage_dealt = 0
        self.damage_healed = 0

    def spellcast(self, spell_used):
        self.current_spell = spell_used
        damage.word_chain(self.previous_spell, self.current_spell)
        match self.current_spell:
#Single Target Spells - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            case 'acid':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(4))
                self.spell_sound = sfx.acid_spell_sound
            case 'air':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(2))
            case 'airslice':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(8))
            case 'arrow':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(4))
            case 'ashes':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(4))
            case 'axe':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(2))
            
            case 'bane':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(4))
            case 'bash':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(3))
            case 'blight':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(5))
            case 'bolt':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(4))
            case 'burn':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(4))
                self.spell_sound = sfx.fire_spell_sound

            case 'crusade':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(6))
            case 'curse':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(5))

            case 'dark':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(3))
            case 'drown':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(5))
            case 'destroy':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(7))

            case 'earth':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(5))
            case 'execute':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(7))
            case 'exile':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(5))

            case 'fire':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(4))
                self.spell_sound = sfx.fire_spell_sound
            case 'firebolt':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(7))
                self.spell_sound = sfx.fire_spell_sound
            case 'freeze':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(7))

            case 'gale':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(4))

            case 'hail':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(4))
            case 'heat':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(4))
            case 'hot':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(4))
            case 'howl':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(4))
            
            case 'ice':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(2))
                self.spell_sound = sfx.ice_spell_sound
            case 'icewall':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(6))
                self.spell_sound = sfx.ice_spell_sound
            
            case 'kick':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(4))
            
            case 'lava':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(4))
            case 'light':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(4))
            case 'lightbeam':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(8))
            
            case 'magma':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(5))
            
            case 'punch':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(4))
            
            case 'rumble':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(6))

            case 'scorch':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(5))
                self.spell_sound = sfx.fire_spell_sound
            case 'smite':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(5))
            case 'snare':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(5))
            case 'snowball':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(7))
            case 'strike':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(6))
            case 'suffocate':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(7))

            case 'thunder':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(7))
            case 'torpedo':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(7))
            
            case 'umbral':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(6))

            case 'wind':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(4))
            case 'water':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(5))
                self.spell_sound = sfx.water_spell_sound
            case 'wet':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(3))
                self.spell_sound = sfx.water_spell_sound
            case 'wind':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(4))
            case 'windslash':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(8))
            
            case 'zap':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(4))

#Aoe Spells - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
            case 'airstrike':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(5))
                damage.AOE_spell(self.damage_dealt)
            case 'avalanche':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(5))
                damage.AOE_spell(self.damage_dealt)

            case 'earthquake':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(5))
                damage.AOE_spell(self.damage_dealt)
            case 'eruption':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(4))
                damage.AOE_spell(self.damage_dealt)
            case 'explosion':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(6))
                damage.AOE_spell(self.damage_dealt)

            case 'fireblast':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(5))
                damage.AOE_spell(self.damage_dealt)
            case 'firestorm':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(6))
                damage.AOE_spell(self.damage_dealt)
            case 'flamethrower':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(8))
                damage.AOE_spell(self.damage_dealt)
            case 'frostnova':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(5))
                damage.AOE_spell(self.damage_dealt)

            case 'heatwave':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(5))
                damage.AOE_spell(self.damage_dealt)
            
            case 'iceprison':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(5))
                damage.AOE_spell(self.damage_dealt)
            
            case 'judgement':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(6))
                damage.AOE_spell(self.damage_dealt)

            case 'landfall':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(4))
                damage.AOE_spell(self.damage_dealt)
            case 'landslide':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(5))
                damage.AOE_spell(self.damage_dealt)
            case 'lightning':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(5))
                damage.AOE_spell(self.damage_dealt)

            case 'obliterate':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(7))
                damage.AOE_spell(self.damage_dealt)

            case 'quasar':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(3))
                damage.AOE_spell(self.damage_dealt)
            
            case 'rain':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(3))
                damage.AOE_spell(self.damage_dealt)
            case 'rainstorm':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(5))
                damage.AOE_spell(self.damage_dealt)
            
            case 'thunderbolt':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(5))
                damage.AOE_spell(self.damage_dealt)
            case 'thunderclap':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(6))
                damage.AOE_spell(self.damage_dealt)
            case 'thunderstorm':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(7))
                damage.AOE_spell(self.damage_dealt)
            case 'tornado':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(5))
                damage.AOE_spell(self.damage_dealt)
            case 'tsunami':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(5))
                damage.AOE_spell(self.damage_dealt)
                self.spell_sound = sfx.water_spell_sound
            
            case 'sandstorm':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(6))
                damage.AOE_spell(self.damage_dealt)
            case 'squall':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(4))
                damage.AOE_spell(self.damage_dealt)
            case 'sunbeam':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(5))
                damage.AOE_spell(self.damage_dealt)
            case 'stonesplitter':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(8))
                damage.AOE_spell(self.damage_dealt)
            
            case 'volcano':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(6))
                damage.AOE_spell(self.damage_dealt)

            case 'waterspout':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(6))
                damage.AOE_spell(self.damage_dealt)
            case 'waterstorm':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(6))
                damage.AOE_spell(self.damage_dealt)
            case 'whirlpool':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(6))
                damage.AOE_spell(self.damage_dealt)
            case 'whirlwind':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(6))
                damage.AOE_spell(self.damage_dealt)

            case 'zephyr':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(5))
                damage.AOE_spell(self.damage_dealt)
            

#Life Steal Spells - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            case 'bite':
                self.enemy_selection_state = True
                self.lifesteal = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(4))

            case 'necromancy':
                self.enemy_selection_state = True
                self.lifesteal = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(6))

#Healing Spells - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            case 'bless':
                self.damage_healed = random.randint(8,12)
                damage.heal_spell(self.damage_healed)

            case 'heal':
                self.damage_healed = random.randint(4,8)
                damage.heal_spell(self.damage_healed)
            
            case 'purify':
                self.damage_healed = random.randint(8,12)
                damage.heal_spell(self.damage_healed)

            case 'recover':
                self.damage_healed = random.randint(15,20)
                damage.heal_spell(self.damage_healed)

#Test words - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            case 'test':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(99))
            case 'tonefaker':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(99))
                for key, count in battle_data.Keys_Remaining.items():
                    battle_data.Keys_Remaining[key] = 5
                damage.AOE_spell(self.damage_dealt)


        self.previous_spell = spell.current_spell


spell = Spell()
damage = Damage()