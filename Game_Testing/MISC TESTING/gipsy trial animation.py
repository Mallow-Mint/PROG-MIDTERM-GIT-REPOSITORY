import pygame
from pygame_functions import *

# Initialize the screen
screenSize(600, 600)
setBackgroundColour("cyan")

# Load the sprite
link_gif_game = 'Link gif/gipsy spritesheet 24 2x.png'
test_sprite = makeSprite(link_gif_game, 24)  # links.gif contains 32 separate frames of animation.
moveSprite(test_sprite, 300, 300, True)
showSprite(test_sprite)

# Set up frame variables
nextFrame = clock()
frame = 0
rolling_mode = 0 + 2
# Main game loop
while True:
    if clock() > nextFrame:  # We only animate our character every 80ms.
        frame = (frame + 1) % 24  # There are 8 frames of animation in each direction
        nextFrame += 80  # so the modulus 8 allows it to loop

    # Handling movement and sprite animation based on key presses
    if rolling_mode == 2:  # Right arrow (keypad 6)
        changeSpriteImage(test_sprite, 0 * 24 + frame)  # 0*8 because right animations are the 0th set in the sprite sheet

    tick(24)

endWait()