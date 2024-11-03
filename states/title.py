import pygame
import sys
from states.state_manager import *
from states.map_state import *
from states.battle_state import *
from states.shop_state import *
from states.battle_data.battle_data import *
from states.managers.Audio_Manager import *

music.title_screen_music()
class Title(State):
    def __init__(self, game):
        State.__init__(self, game)

    def update(self):
        if menu.start_tutorial:
            music.title_screen_music_stop()
            initalize_battle()
            new_state = Battle(self.game)
            new_state.enter_state()
            menu.start_tutorial = False
<<<<<<< HEAD
        if menu.start_game:
            music.title_screen_music_stop()
            new_state = Map(self.game)
            new_state.enter_state()
            menu.start_game = False
        if menu.open_shop:
            music.title_screen_music_stop()
=======
        
        if menu.start_game == True:
            new_state = Map(self.game)
            print(battle_data.inventory_slots)
            new_state.enter_state() 
            menu.start_game = False

        if menu.open_shop == True:
            shop_initializer()
>>>>>>> 9f0290db912832fba2f2fe106c6008fec8a517c5
            new_state = Shop_State(self.game)
            new_state.enter_state()
            menu.open_shop = False

    def render(self, display):
        main_menu()
        display.blit(MENU_SCREEN, (0, 0))

class Menu:
    def __init__(self):
        self.start_game = False
        self.start_tutorial = False
        self.open_shop = False

pygame.init()

Title_BG = pygame.image.load('Assets/Background/bg_15/bg_15.png')
Title_BG = pygame.transform.scale(Title_BG, (1600, 900))

MENU_SCREEN = pygame.display.set_mode((1600, 900))
BLACK = (0, 0, 0)

def get_font(size):
    return pygame.font.Font('Assets/Fonts/timetwist/Timetwist-Bold.otf', size)

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
def intro_fade(screen):
    overlay = pygame.Surface((1600, 900))
    overlay.fill(BLACK)
    
    message = "Shadow engulfed lightness...\n" \
              "evil monsters disturbed peace...\n" \
              "we need to eradicate them all!\n" \
              "Will you be our hero...?"
    font = get_font(30)
    
    start_time = pygame.time.get_ticks()
    fade_in_duration = 13000  
    fade_out_duration = 3000  

    revealed_text = ""
    char_index = 0
    text_duration = fade_in_duration // len(message.replace(" ", ""))  
    
    while True:
        elapsed_time = pygame.time.get_ticks() - start_time

        if elapsed_time < fade_in_duration:
            if elapsed_time >= char_index * text_duration and char_index < len(message):
                revealed_text += message[char_index]
                char_index += 1

            screen.fill(BLACK)
            render_text_centered(screen, revealed_text, font, (255, 255, 255), (800, 450))
            overlay.set_alpha(255)  

        elif elapsed_time < fade_in_duration + fade_out_duration:

            fade_out_time = elapsed_time - fade_in_duration
            alpha = max(0, 255 - (fade_out_time / fade_out_duration) * 255)
            overlay.set_alpha(int(alpha))
            screen.fill((0, 0, 0))
            screen.blit(Title_BG, (0, 0))
            screen.blit(overlay, (0, 0))
        else:
            break  

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def render_text_centered(screen, text, font, color, position):
    lines = text.splitlines()
    y_offset = font.get_linesize() * len(lines) // 2 
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect(center=(position[0], position[1] - y_offset + i * font.get_linesize()))
        screen.blit(text_surface, text_rect)

def main_menu():
    MENU_SCREEN.blit(Title_BG, (0, 0))
    mouse_pos = pygame.mouse.get_pos()

    title_text = pygame.image.load('Assets/Background/bg_1/bg_title.png')
    title_rect = title_text.get_rect(center=(800, 150))
    MENU_SCREEN.blit(title_text, title_rect)

    start_button = Button((800, 250), "NEW GAME", get_font(22), BLACK, (200, 200, 200))
    tutorial_button = Button((800, 300), "TUTORIALS", get_font(22), BLACK, (200, 200, 200))
    scores_button = Button((800, 350), "SCORES", get_font(22), BLACK, (200, 200, 200))
    quit_button = Button((800, 400), "QUIT", get_font(22), BLACK, (200, 200, 200))

    start_button.change_color(mouse_pos)
    tutorial_button.change_color(mouse_pos)
    scores_button.change_color(mouse_pos)
    quit_button.change_color(mouse_pos)

    start_button.draw(MENU_SCREEN)
    tutorial_button.draw(MENU_SCREEN)
    scores_button.draw(MENU_SCREEN)
    quit_button.draw(MENU_SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.check_for_input(mouse_pos):
                menu.start_game = True
            if tutorial_button.check_for_input(mouse_pos):
                menu.start_tutorial = True
            if scores_button.check_for_input(mouse_pos):
                menu.open_shop = True
            if quit_button.check_for_input(mouse_pos):
                pygame.quit()
                sys.exit()

intro_fade(MENU_SCREEN)
