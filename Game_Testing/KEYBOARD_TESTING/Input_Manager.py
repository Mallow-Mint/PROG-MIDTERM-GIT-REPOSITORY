import pygame
import random

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

class Spell:
    def __init__(self):
        #Get Valid Words from Text File
        self.shared_dictionary = open('Game_Testing/KEYBOARD_TESTING/SpellBook.txt', "r")
        self.valid_words = self.shared_dictionary.read() 
        self.valid_words = self.valid_words.split("\n")
        self.shared_dictionary.close()
        selected_enemy = None

    def spellcast(self, spell):
        self.current_spell = spell
        match self.current_spell:
            case 'fire':
                self.fire_damage_dealt = damage.critical_checker(damage.damage_range_calculator(5))
                print("You dealt", self.fire_damage_dealt, "damage")


spell = Spell()
damage = Damage()