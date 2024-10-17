import pygame
import sys

class Animation:
    def __init__(self, frames):
        self.frames = frames

    ###class Animation:
    ###def __init__(self, spritesheet):
    ###    self.spritesheet = spritesheet
    ###def playanim(self):
    ###     pygame.spritemethod(self.spritesheet)

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 1600, 900
screen = pygame.display.set_mode((screen_width, screen_height))

# Set a clock for controlling the frame rate
clock = pygame.time.Clock()

# Load the sprite animation frames into a list
sprite_frames = [
    pygame.image.load('Game Testing\ENEMY TESTING\pump_king_attack\pumpking_attack_1.png'),
    pygame.image.load('Game Testing\ENEMY TESTING\pump_king_attack\pumpking_attack_2.png'),
    pygame.image.load('Game Testing\ENEMY TESTING\pump_king_attack\pumpking_attack_3.png'),
    pygame.image.load('Game Testing\ENEMY TESTING\pump_king_attack\pumpking_attack_4.png'),
    pygame.image.load('Game Testing\ENEMY TESTING\pump_king_attack\pumpking_attack_5.png'),
    pygame.image.load('Game Testing\ENEMY TESTING\pump_king_attack\pumpking_attack_6.png')
]

pump = Animation(sprite_frames)

# Set the initial frame index and animation speed
current_frame = 0
frame_duration = 100  # Milliseconds per frame
last_frame_time = pygame.time.get_ticks()

# Create a rect object for positioning
sprite_rect = pump.frames[0].get_rect()

# Set the initial position of the sprite
sprite_rect.topleft = (screen_width // 2,screen_height // 2)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the current time
    current_time = pygame.time.get_ticks()

    # Check if it's time to update the frame
    if current_time - last_frame_time > frame_duration:
        current_frame = (current_frame + 1) % len(sprite_frames)
        last_frame_time = current_time

    # Fill the screen with a background color (optional)
    screen.fill((0, 0, 0))

    # Draw the current frame of the animated sprite
    screen.blit(sprite_frames[current_frame], sprite_rect)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)  # Limit to 60 frames per second
