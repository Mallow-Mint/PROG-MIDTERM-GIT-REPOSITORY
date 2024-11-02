import pygame
import time
from states.title import *

class Game():
    def __init__(self):
        pygame.init()
        self.GAME_WIDTH = 1600
        self.GAME_HEIGHT = 900
        self.GAME_DISPLAY = pygame.Surface((self.GAME_WIDTH, self.GAME_HEIGHT))
        self.TRANSITION_DISPLAY = pygame.Surface((self.GAME_WIDTH, self.GAME_HEIGHT))
        self.GAME_SCREEN = pygame.display.set_mode((self.GAME_WIDTH, self.GAME_HEIGHT))
        pygame.display.set_caption("Spell Book")
        self.RUNNING = True
        self.PLAYING = True
        self.DELTA_TIME = 0 
        self.PREVIOUS_TIME = 0
        self.STATE_STACK = []
        self.load_states()

    def game_loop(self):
        while self.PLAYING:
            self.get_delta_time()
            self.update()
            self.render()

    def update(self):
        self.STATE_STACK[-1].update()

    def render(self):
        self.STATE_STACK[-1].render(self.GAME_DISPLAY)
        self.GAME_SCREEN.blit(self.GAME_DISPLAY, (0,0))
        pygame.display.flip()

    def get_delta_time(self):
        current_time = time.time()
        self.DELTA_TIME = current_time - self.PREVIOUS_TIME
        self.PREVIOUS_TIME = current_time

    def load_states(self):
        self.title_screen = Title(self)
        self.STATE_STACK.append(self.title_screen)

if __name__ == "__main__":
    game = Game()
    while game.RUNNING:
        game.game_loop()
