import pygame
from Game_Testing.TITLE_TESTING.Title_screen import *
from Game_Testing.KEYBOARD_TESTING.Keyboard_ver_4 import *

running = True
while running:
    main_menu.main_menu_display()
    print(main_menu.new_game_conditon)
    if main_menu.self.new_game_condition == True:
        battle_interface()