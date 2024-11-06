import random
import pygame
pygame.init
def initialize_key_amounts():
    shared_dictionary = open('states/battle_data/SpellBook.txt', "r")
    valid_words = shared_dictionary.read() 
    valid_word_list = valid_words.split("\n")
    shared_dictionary.close()
    for x in range(len(valid_word_list)):
        current_word = valid_word_list[x]
        new_word = current_word.lower()
        valid_word_list[x] = new_word
        print(current_word)
    print(valid_word_list)

l = ['cat', 'dog', 'cow']

print(l)

def remove_from_list(list, word):
    working_list = list
    removed_word_index = working_list.index(word)
    working_list.pop(removed_word_index)
    return working_list

l = remove_from_list(l, 'dog')
l = remove_from_list(l, 'cat')
l = remove_from_list(l, 'cow')

print(l)

for x in range(1):
    print(x)
words = ['acid', 'air', 'airslice', 'airstrike', 'arrow', 'ashes', 'avalanche', 'axe',
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
          'zap', 'zephyr']

letter_counts = {}
for word in words:
    for letter in set(word):  # Use set to get unique letters in each word
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

# Print the results
print("Letter counts in words:")
for letter, count in letter_counts.items():
    print(f"{letter}: {count}")