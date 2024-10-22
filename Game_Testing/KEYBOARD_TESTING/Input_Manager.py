import pygame
import random
from Character_Manager import *

class Damage():
    def __init__(self):
        pass
    def damage_range_calculator(self, base_damage):
        self.damage_dealt = round(base_damage * random.uniform(0.8, 1.6), 0)
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
        spell.reset_keyboard()
        print(character.player_hp_health_bar.current_hp)

class Spell:
    def __init__(self):
        #Get Valid Words from Text File
        self.shared_dictionary = open('Game_Testing/KEYBOARD_TESTING/SpellBook.txt', "r")
        self.valid_words = self.shared_dictionary.read() 
        self.valid_words = self.valid_words.split("\n")
        self.shared_dictionary.close()
        self.enemy_selection_state = False
        self.damage_dealt = 0
        self.damage_healed = 0

    def reset_keyboard(self):
        self.enemy_selection_state = False
        self.damage_dealt = 0
        self.damage_healed = 0

    def spellcast(self, spell_used):
        self.current_spell = spell_used
        match self.current_spell:
            case 'fire':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(5))
            case 'heal':
                self.damage_healed = random.randint(8,12)
                damage.heal_spell(self.damage_healed)

    def targeted_enemy(self, mouse_pos):
        self.current_click = mouse_pos

        if character.enemy_1_selector.check_for_input(self.current_click):
            character.do_damage_single_target(self.damage_dealt, 1)

        elif character.enemy_2_selector.check_for_input(self.current_click):
            character.do_damage_single_target(self.damage_dealt, 2)

        elif character.enemy_3_selector.check_for_input(self.current_click):
            character.do_damage_single_target(self.damage_dealt, 3)
            
        elif character.enemy_4_selector.check_for_input(self.current_click):
            character.do_damage_single_target(self.damage_dealt, 4)
                

        spell.reset_keyboard()
        print(character.current_enemies_alive_hp)


spell = Spell()
damage = Damage()