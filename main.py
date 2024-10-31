import pygame
import time

class Game():
    def __init__(self):
        pygame.init()
        self.GAME_WIDTH = 1600
        self.GAME_HEIGHT = 900
        self.GAME_DISPLAY = pygame.Surface((self.GAME_WIDTH, self.GAME_HEIGHT))
        self.GAME_SCREEN = pygame.display.set_mode((self.GAME_WIDTH, self.GAME_HEIGHT))
        self.RUNNING = True
        self.PLAYING = True
        self.DELTA_TIME = 0
        self.PREVIOUS_TIME = 0
        self.STATE_STACK = []

    def close_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.PLAYING = False
                self.RUNNING = False
    
    def game_loop(self):
        while self.PLAYING:
            self.update

    def update(self):
        pass

    def render(self):
        pygame.display.flip()
    
    def get_delta_time(self):
        current_time = time.time()
        self.DELTA_TIME = current_time - self.PREVIOUS_TIME
        self.PREVIOUS_TIME = current_time

if __name__ == "__main__":
    game = Game()
    while game.RUNNING:
        game.game_loop()