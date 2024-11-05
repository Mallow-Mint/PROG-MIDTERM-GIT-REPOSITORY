import pygame
import sys
import time
import random

class Battle_Data:
    def __init__(self):
        self.current_health = [50]
        self.Keys_Remaining = { 'q': 5,
                                'w': 5,
                                'e': 5, 
                                'r': 5,
                                't': 5,
                                'y': 5,
                                'u': 5,
                                'i': 5,
                                'o': 5,
                                'p': 5,
                                'a': 5,
                                's': 5,
                                'd': 5,
                                'f': 5,
                                'g': 5,
                                'h': 5,
                                'j': 5,
                                'k': 5, 
                                'l': 5,
                                'z': 5,
                                'x': 5,
                                'c': 5,
                                'v': 5,
                                'b': 5,
                                'n': 5,
                                'm': 5}
        
        self.valid_letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 
                              'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                              'z', 'x', 'c', 'v', 'b', 'n', 'm' ]
        
        self.player_currency = 300
        self.inventory_slots = [None] * 4
        self.total_characters = 0

    def reset_battle_data(self):
        self.current_health = [50]
        self.Keys_Remaining = { 'q': 5,
                                'w': 5,
                                'e': 5, 
                                'r': 5,
                                't': 5,
                                'y': 5,
                                'u': 5,
                                'i': 5,
                                'o': 5,
                                'p': 5,
                                'a': 5,
                                's': 5,
                                'd': 5,
                                'f': 5,
                                'g': 5,
                                'h': 5,
                                'j': 5,
                                'k': 5, 
                                'l': 5,
                                'z': 5,
                                'x': 5,
                                'c': 5,
                                'v': 5,
                                'b': 5,
                                'n': 5,
                                'm': 5}
        
        self.valid_letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 
                              'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                              'z', 'x', 'c', 'v', 'b', 'n', 'm' ]
        
        self.player_currency = 300
        self.inventory_slots = [None] * 6
        self.total_characters = 0



class Valid_Dictionary:
    def __init__(self):
        self.valid_word_list = ['acid', 'air', 'airslice', 'airstrike', 'arrow', 'ashes', 'avalanche', 'axe',
                                'bane', 'bash', 'bite', 'bless', 'blight', 'bolt', 'burn',
                                'crusade', 'curse',
                                'dark', 'drown', 'destroy',
                                'earth', 'earthquake', 'eruption', 'execute', 'exile', 'explosion',
                                'fire', 'fireblast', 'firebolt', 'firestorm', 'flamethrower', 'freeze', 'frostnova',
                                'gale',
                                'hail', 'heal', 'heat', 'heatwave', 'hot', 'howl',
                                'ice', 'iceprison', 'icewall',
                                'judgement',
                                'kick',
                                'landfall', 'landslide', 'lava', 'light', 'lightbeam', 'lightning',
                                'magma', 'necromancy',
                                'obliterate',
                                'poison', 'punch', 'purify',
                                'quasar',
                                'rain', 'rainstorm', 'recover', 'rumble',
                                'sandstorm', 'scorch', 'smite', 'snare', 'snowball', 'squall', 'stonesplitter', 'strike', 'suffocate', 'sunbeam',
                                'thunder', 'thunderbolt', 'thunderclap', 'thunderstorm', 'tornado', 'torpedo', 'tsunami',
                                'umbral',
                                'volcano', 
                                'water', 'waterspout', 'waterstorm', 'wet', 'whirlpool', 'whirlwind', 'wind', 'windslash', 
                                'zap', 'zephyr', 
                                'test', 'tonefaker']
        
        self.single_target_words_damage = { 'acid': 4,
                                            'air': 2,
                                            'airslice': 8,
                                            'arrow': 4,
                                            'ashes': 4,
                                            'axe': 2,
                                            'bane': 4,
                                            'bash': 3,
                                            'blight': 5,
                                            'bolt': 4,
                                            'burn': 4,
                                            'crusade': 6,
                                            'curse': 5,
                                            'dark': 3,
                                            'drown': 5,
                                            'destroy': 7,
                                            'earth': 5,
                                            'execute': 7,
                                            'exile': 5,
                                            'fire': 4,
                                            'firebolt': 7,
                                            'freeze': 7,
                                            'gale': 4,
                                            'hail': 4,
                                            'heat': 4,
                                            'hot': 4,
                                            'howl': 4,
                                            'ice': 2,
                                            'icewall': 6,
                                            'kick': 4,
                                            'lava': 4,
                                            'light': 4,
                                            'lightbeam': 8,
                                            'magma': 5,
                                            'punch': 4,
                                            'rumble': 6,
                                            'scorch': 5,
                                            'smite': 5,
                                            'snare': 5,
                                            'snowball': 7,
                                            'strike': 6,
                                            'suffocate': 7,
                                            'thunder': 7,
                                            'torpedo': 7,
                                            'umbral': 6,
                                            'wind': 4,
                                            'water': 5,
                                            'wet': 3,
                                            'wind': 4,
                                            'windslash': 8,
                                            'zap': 4}
        
        self.life_steal_damage = {'bite': 4,
                                  'necromancy': 8}
        
        self.multi_target_word_damage = {   'airstrike': 5,
                                            'avalanche': 4,
                                            'earthquake': 5,
                                            'eruption': 4,
                                            'explosion': 4,
                                            'fireball': 4,
                                            'firestorm': 4,
                                            'flamethrower': 6,
                                            'frostnova': 4,
                                            'heatwave': 4,
                                            'iceprison': 4,
                                            'judgement': 4,
                                            'landfall': 4,
                                            'landslide': 4,
                                            'lightning': 4,
                                            'obliterate': 5,
                                            'quasar': 3,
                                            'rain': 2,
                                            'rainstorm': 4,
                                            'thunderbolt': 5,
                                            'thunderclap': 5,
                                            'thunderstorm': 6,
                                            'tornado': 3,
                                            'tsunami': 3,
                                            'sandstorm': 4,
                                            'squall': 3,
                                            'sunbeam': 3,
                                            'stonesplitter': 6,
                                            'volcano': 3,
                                            'waterspout': 5,
                                            'waterstorm': 5,
                                            'whirlpool': 4,
                                            'whirlwind': 4,
                                            'zephyr': 3 }
        
        self.healing_spell_ranges = {'bless': [8,12],
                                     'heal': [4,8],
                                     'purify': [8,12],
                                     'recover': [13,20]}
    
    def validWordChecker(self, current_typed_word:str):
        if current_typed_word in self.valid_word_list:
            return True
        else:
            return False
    
dictionary = Valid_Dictionary()
battle_data = Battle_Data()
