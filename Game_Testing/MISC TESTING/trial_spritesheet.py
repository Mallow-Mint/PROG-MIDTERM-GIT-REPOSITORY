import pygame
import spritesheet

pygame.init()

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

sprite_sheet_image = pygame.image.load('Game_Testing\MISC TESTING\Link gif\XL healing potion 14.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

BG = (50, 50, 50)
BLACK = (0, 0, 0)

#Creating animation list
animation_list = []
animation_steps = [15]  # Example: two animations with 7 frames each
last_update = pygame.time.get_ticks()
action = 0
animation_cooldown = 100  # Time in milliseconds between frames
frame = 0
step_counter = 0

# Populate the animation_list based on the frames in animation_steps
for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(sprite_sheet.get_image(step_counter, 57, 114, 1, BLACK))  # Adjust frame size as needed
        step_counter += 1
    animation_list.append(temp_img_list)

run = True
while run:

    # Update background
    screen.fill(BG)

    # Update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame = 0
            
    # Show frame image
    screen.blit(animation_list[action][frame], (0, 0))

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
