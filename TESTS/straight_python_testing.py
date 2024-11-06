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
