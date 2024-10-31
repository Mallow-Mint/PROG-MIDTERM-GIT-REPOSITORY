import pygame
import time
from states.title import *
from states.battle_state import *

class Game():
    def __init__(self):
        pygame.init()
        self.GAME_WIDTH = 1600
        self.GAME_HEIGHT = 900
        self.GAME_DISPLAY = pygame.Surface((self.GAME_WIDTH, self.GAME_HEIGHT))
        self.GAME_SCREEN = pygame.display.set_mode((self.GAME_WIDTH, self.GAME_HEIGHT))
        pygame.display.set_caption("Spell Book")
        self.RUNNING = True
        self.PLAYING = True
        self.DELTA_TIME = 0
        self.PREVIOUS_TIME = 0
        self.STATE_STACK = []
        self.load_states()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.RUNNING = False
                self.PLAYING = False
        if timer.is_player_turn == False:
            pass
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif timer.is_player_turn == True:
                    mouse_pos = pygame.mouse.get_pos()
                    if event.type == pygame.KEYDOWN and spell.enemy_selection_state == False:
                        key = pygame.key.name(event.key)
                        keyboard.key_press_action(key)

                    elif event.type == pygame.MOUSEBUTTONDOWN and spell.enemy_selection_state == True:
                        spell.targeted_enemy(mouse_pos)

                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if keyboard.end_turn_button.is_clicked() == True:
                            timer.timer_duration = 1

    def game_loop(self):
        while self.PLAYING:
            self.get_delta_time()
            self.get_events()
            self.update()
            self.render()

    def update(self):
        pass

    def render(self):
        self.STATE_STACK[-1].render(self.GAME_DISPLAY)
        self.GAME_SCREEN.blit(self.GAME_DISPLAY, (0,0))
        pygame.display.flip()

    def get_delta_time(self):
        current_time = time.time()
        self.DELTA_TIME = current_time - self.PREVIOUS_TIME
        self.PREVIOUS_TIME = current_time

    def load_states(self):
        self.battle_screen = Battle(self)
        self.STATE_STACK.append(self.battle_screen)

if __name__ == "__main__":
    game = Game()
    while game.RUNNING:
        game.game_loop()