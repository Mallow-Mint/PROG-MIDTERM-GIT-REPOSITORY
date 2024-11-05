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
    
    def validWordChecker(self, current_typed_word:str):
        if current_typed_word in self.valid_word_list:
            return True
        else:
            return False
    
dictionary = Valid_Dictionary()
battle_data = Battle_Data()
