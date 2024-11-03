import pygame
import time
import sys
from states.state_manager import *
from states.map_state import *
from states.battle_state import *
from states.shop_state import *
from states.battle_data.battle_data import *
from states.managers.Audio_Manager import *

class Title(State):
    def __init__(self, game):
        State.__init__(self, game)

    def update(self):
        if menu.start_tutorial == True:
            initalize_battle()
            new_state = Battle(self.game)
            new_state.enter_state() 
            menu.start_tutorial = False
        
        if menu.start_game == True:
            new_state = Map(self.game)
            print(battle_data.inventory_slots)
            new_state.enter_state() 
            menu.start_game = False

        if menu.open_shop == True:
            music.title_screen_music_stop()
            shop_initializer()
            new_state = Shop_State(self.game)
            new_state.enter_state() 
            menu.open_shop = False

    def render(self, display):
        main_menu()
        display.blit(MENU_SCREEN, (0,0))

class Menu:
    def __init__(self):
        self.start_game = False
        self.start_tutorial = False
        self.open_shop = False


# Initialize Pygame
pygame.init()

Title_BG = pygame.image.load('Assets/Background/bg_15/bg_15.png')
Title_BG = pygame.transform.scale(Title_BG, (1600,900))
# Set up display
MENU_SCREEN = pygame.display.set_mode((1600, 900))

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# Load font
def get_font(size):
    return pygame.font.Font('Assets/Fonts/timetwist/Timetwist-Bold.otf', size)

# Button class
class Button:
    def __init__(self, pos, text, font, base_color, hover_color):
        self.image = None
        self.pos = pos
        self.font = font
        self.text = text
        self.base_color = base_color
        self.hover_color = hover_color
        self.rect = None
        self.create_button()

    def create_button(self):
        text_surface = self.font.render(self.text, True, self.base_color)
        self.rect = text_surface.get_rect(center=self.pos)
        self.image = text_surface

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def change_color(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.image = self.font.render(self.text, True, self.hover_color)
        else:
            self.image = self.font.render(self.text, True, self.base_color)

    def check_for_input(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    
menu = Menu()
# Main function
def main_menu():
    MENU_SCREEN.blit(Title_BG, (0,0))
    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Title text
    title_text = pygame.image.load('Assets/Background/bg_1/bg_title.png')
    title_rect = title_text.get_rect(center=(800, 150))
    MENU_SCREEN.blit(title_text, title_rect)

    # Create buttons
    start_button = Button((800, 250), "NEW GAME", get_font(22), BLACK, GRAY)
    tutorial_button = Button((800, 300), "TUTORIALS", get_font(22), BLACK, GRAY)
    scores_button = Button((800, 350), "SCORES", get_font(22), BLACK, GRAY)
    quit_button = Button((800, 400), "QUIT", get_font(22), BLACK, GRAY)


    # Change button color based on mouse position
    start_button.change_color(mouse_pos)
    tutorial_button.change_color(mouse_pos)
    scores_button.change_color(mouse_pos)
    quit_button.change_color(mouse_pos)

    # Draw buttons
    start_button.draw(MENU_SCREEN)
    tutorial_button.draw(MENU_SCREEN)
    scores_button.draw(MENU_SCREEN)
    quit_button.draw(MENU_SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.check_for_input(mouse_pos):
                menu.start_game = True  # Replace with your game starting function
            if tutorial_button.check_for_input(mouse_pos):
                menu.start_tutorial = True
            if scores_button.check_for_input(mouse_pos):
                print("Show scores")
                menu.open_shop = True
            if quit_button.check_for_input(mouse_pos):
                pygame.quit()
                sys.exit()

# Run the main menu
