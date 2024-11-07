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

l.pop()
print(l)