import pygame

class Spell:
    def __init__(self):
        #Get Valid Words from Text File
        self.shared_dictionary = open('Game_Testing/KEYBOARD_TESTING/SpellBook.txt', "r")
        self.valid_words = self.shared_dictionary.read() 
        self.valid_words = self.valid_words.split("\n")
        self.shared_dictionary.close()

    def spellcast(self, spell):
        self.current_spell = spell
        if spell in self.valid_words:
            print("You Cast", self.current_spell)

spell = Spell()