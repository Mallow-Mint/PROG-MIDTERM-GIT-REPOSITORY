import pygame
from pygame_functions import *

# Initialize the screen
screenSize(600, 600)
setBackgroundColour("pink")

# Load the sprite
testSprite = makeSprite("C:\\Users\\litch\\Downloads\\Spell-Break\\assets\\links.gif", 32)  # links.gif contains 32 separate frames of animation.
moveSprite(testSprite, 300, 300, True)
showSprite(testSprite)

# Set up frame variables
nextFrame = clock()
frame = 0

# Main game loop
while True:
    if clock() > nextFrame:  # We only animate our character every 80ms.
        frame = (frame + 1) % 8  # There are 8 frames of animation in each direction
        nextFrame += 80  # so the modulus 8 allows it to loop

    # Get key states using pygame key handling
    keys = pygame.key.get_pressed()

    # Handling movement and sprite animation based on key presses
    if keys[pygame.K_d]:  # Right arrow (keypad 6)
        changeSpriteImage(testSprite, 0 * 8 + frame)  # 0*8 because right animations are the 0th set in the sprite sheet

    elif keys[pygame.K_s]:  # Down arrow (keypad 2)
        changeSpriteImage(testSprite, 1 * 8 + frame)  # down facing animations are the 1st set

    elif keys[pygame.K_a]:  # Left arrow (keypad 4)
        changeSpriteImage(testSprite, 2 * 8 + frame)  # left facing animations

    elif keys[pygame.K_w]:  # Up arrow (keypad 8)
        changeSpriteImage(testSprite, 3 * 8 + frame)  # up facing animations

    else:
        changeSpriteImage(testSprite, 1 * 8 + 5)  # the static facing front look

    tick(120)

endWait()
