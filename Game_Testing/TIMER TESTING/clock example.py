import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 1600, 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Clock Example - Top Left")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Font and size
font = pygame.font.Font(None, 74)

# Clock object to manage time
clock = pygame.time.Clock()

# Timer setup (in seconds)
timer_duration = 60  # 30 second countdown
start_ticks = pygame.time.get_ticks()  # Record start time

# Circular clock settings
center_x, center_y = 200, 50  # Position the center of the circle near the top-left corner
radius = 40  # Radius of the clock
line_thickness = 10  # Thickness of the clock hand

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen with white
    screen.fill(BLACK)

    # Calculate the time remaining (since get_ticks gives time in milliseconds)
    seconds_passed = (pygame.time.get_ticks() - start_ticks) / 1000
    time_left = max(0, timer_duration - int(seconds_passed))

    # Render the timer text (position it near the top left)
    timer_text = font.render(f"{time_left:02d}", True, WHITE)
    screen.blit(timer_text, (50, 50))  # Position text at (50, 50) near top-left

    # Calculate the angle of the clock hand based on time remaining
    angle = (time_left / timer_duration) * 2 * math.pi  # Convert to radians

    # Calculate the end position of the clock hand
    hand_x = center_x + radius * math.cos(-angle + math.pi / 2)
    hand_y = center_y + radius * math.sin(-angle + math.pi / 2)

    # Draw the clock circle (positioned at top left)
    pygame.draw.circle(screen, WHITE, (center_x, center_y), radius, line_thickness)

    # Draw the clock hand (line from center to calculated hand position)
    pygame.draw.line(screen, RED, (center_x, center_y), (hand_x, hand_y), line_thickness)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 frames per second
    clock.tick(60)  # Limit to 60 FPS

# Quit Pygame
pygame.quit()
sys.exit()



