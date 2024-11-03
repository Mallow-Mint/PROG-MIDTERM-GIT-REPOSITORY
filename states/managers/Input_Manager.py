import pygame
import random
import time
from states.managers.Battle_Manager import *

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
            character.do_damage_single_target(self.damage_dealt, 1)
            spell.reset_damage()

        elif character.enemy_2_selector.is_clicked(self.current_click) == True and character.current_enemies_alive_hp[1] !=0:
            character.do_damage_single_target(self.damage_dealt, 2)
            spell.reset_damage()

        elif character.enemy_3_selector.is_clicked(self.current_click) == True and character.current_enemies_alive_hp[2] !=0:
            character.do_damage_single_target(self.damage_dealt, 3)
            spell.reset_damage()
            
        elif character.enemy_4_selector.is_clicked(self.current_click) == True and character.current_enemies_alive_hp[3] !=0:
            character.do_damage_single_target(self.damage_dealt, 4)
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
        self.damage_dealt = 0
        self.damage_healed = 0

    def reset_damage(self):
        self.enemy_selection_state = False
        self.damage_dealt = 0
        self.damage_healed = 0

    def spellcast(self, spell_used):
        self.current_spell = spell_used
        damage.word_chain(self.previous_spell, self.current_spell)
        match self.current_spell:
#Single Target Spells - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            case 'fire':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(4)) 

            case 'air':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(2))

            case 'water':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(5))

            case 'wind':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(3))

            case 'earth':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(5))

            case 'ice':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(2))

            case 'arrow':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(4))

            case 'punch':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(4))

            case 'magma':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(5))

            case 'light':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(4))

            case 'dark':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(4))

#Aoe Spells - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
            case 'lightning':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(4))
                damage.AOE_spell(self.damage_dealt)

#Life Steal Spells - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            case 'bite':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(4))

#Healing Spells - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            case 'heal':
                self.damage_healed = random.randint(6,10)
                damage.heal_spell(self.damage_healed)

            case 'recover':
                self.damage_healed = random.randint(15,20)
                damage.heal_spell(self.damage_healed)

#Test words - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            case 'test':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(99))

        self.previous_spell = spell.current_spell


spell = Spell()
damage = Damage()