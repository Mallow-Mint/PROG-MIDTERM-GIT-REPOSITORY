import pygame
import sys
from states.state_manager import *
from states.map_state import *
from states.battle_state import *
from states.shop_state import *
from states.battle_data.battle_data import *
from states.managers.Audio_Manager import *

pygame.init()

Game_Over_Screen = pygame.display.set_mode((1600, 900))
BLACK = (0, 0, 0)

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

def get_font(size):
    return pygame.font.Font('Assets/Fonts/timetwist/Timetwist-Bold.otf', size)

def intro_fade(screen):
    overlay = pygame.Surface((1600, 900))
    overlay.fill(BLACK)
    
    message = "Shadow engulfed lightness...\n" \
              "withered peace...\n" \
              "eradicate them all!\n" \
              "Will you be our hero..?"
    font = get_font(30)
    
    start_time = pygame.time.get_ticks()
    fade_in_duration = 13000  
    fade_out_duration = 3000  

    revealed_text = ""
    char_index = 0
    text_duration = 11500 // len(message.replace(" ", ""))  
    
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
            if event.type == pygame.KEYDOWN:
                fade_in_duration = 0
                fade_out_duration = 0
                
def render_text_centered(screen, text, font, color, position):
    lines = text.splitlines()
    y_offset = font.get_linesize() * len(lines) // 2 
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect(center=(position[0], position[1] - y_offset + i * font.get_linesize()))
        screen.blit(text_surface, text_rect)