import pygame
import random
import time
from states.managers.Battle_Manager import *
from states.managers.Audio_Manager import *
from states.battle_data.battle_data import *

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

        elif character.enemy_2_selector.is_clicked(self.current_click) == True and character.current_enemies_alive_hp[1] !=0:
            character.do_damage_single_target(spell.damage_dealt, 2)
            if spell.lifesteal == True:
                self.heal_spell(int(self.damage_dealt/2))

        elif character.enemy_3_selector.is_clicked(self.current_click) == True and character.current_enemies_alive_hp[2] !=0:
            character.do_damage_single_target(spell.damage_dealt, 3)
            if spell.lifesteal == True:
                self.heal_spell(int(self.damage_dealt/2))
            
        elif character.enemy_4_selector.is_clicked(self.current_click) == True and character.current_enemies_alive_hp[3] !=0:
            character.do_damage_single_target(spell.damage_dealt, 4)
            if spell.lifesteal == True:
                self.heal_spell(int(self.damage_dealt/2))
        
        else:
            return None
        #spell.spell_sound()
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
            case self.current_spell if self.current_spell in dictionary.single_target_words_damage.keys():
                self.enemy_selection_state = True
                base_damage = dictionary.single_target_words_damage[self.current_spell]
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(base_damage))
                #self.spell_sound = spell_sfx[self.current_spell

#Life Steal Spells - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            case self.current_spell if self.current_spell in dictionary.life_steal_damage.keys():
                self.enemy_selection_state = True
                self.lifesteal = True
                base_damage = dictionary.life_steal_damage[self.current_spell]
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(base_damage))

#Aoe Spells - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
            case self.current_spell if self.current_spell in dictionary.multi_target_word_damage.keys():
                base_damage = dictionary.multi_target_word_damage[self.current_spell]
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(base_damage))
                damage.AOE_spell(self.damage_dealt)

#Healing Spells - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            case self.current_spell if self.current_spell in dictionary.healing_spell_ranges.keys():
                heal_range = [dictionary.healing_spell_ranges[self.current_spell][0], dictionary.healing_spell_ranges[self.current_spell][1]]
                damage.heal_spell(random.randint(heal_range[0], heal_range[1]))

#Test words - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            case 'test':
                self.enemy_selection_state = True
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(99))
            case 'tonefaker':
                self.damage_dealt = damage.critical_checker(damage.damage_range_calculator(99))
                for key, count in battle_data.Keys_Remaining.items():
                    battle_data.Keys_Remaining[key] = 5
                sfx.FAKER()
                time.sleep(4)
                damage.AOE_spell(self.damage_dealt)

        self.previous_spell = spell.current_spell


spell = Spell()
damage = Damage()