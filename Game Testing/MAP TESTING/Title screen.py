import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Spell Book")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# Load font
def get_font(size):
    return pygame.font.Font(None, size)

# Button class
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

# Main function
def main_menu():
    while True:
        SCREEN.fill(BLACK)

        # Get mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Title text
        title_text = get_font(75).render("SPELL BOOK", True, WHITE)
        title_rect = title_text.get_rect(center=(400, 100))
        SCREEN.blit(title_text, title_rect)

        # Create buttons
        start_button = Button((400, 300), "NEW GAME", get_font(50), WHITE, GRAY)
        tutorial_button = Button((400, 350), "TUTORIALS", get_font(50), WHITE, GRAY)
        scores_button = Button((400, 400), "SCORES", get_font(50), WHITE, GRAY)
        settings_button = Button((400, 450), "SETTINGS", get_font(50), WHITE, GRAY)
    

        # Change button color based on mouse position
        start_button.change_color(mouse_pos)
        tutorial_button.change_color(mouse_pos)
        scores_button.change_color(mouse_pos)
        settings_button.change_color(mouse_pos)


        # Draw buttons
        start_button.draw(SCREEN)
        tutorial_button.draw(SCREEN)
        scores_button.draw(SCREEN)
        settings_button.draw(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.check_for_input(mouse_pos):
                    print("Start the game!")  # Replace with your game starting function
                if tutorial_button.check_for_input(mouse_pos):
                    print("Start the tutorial")
                if scores_button.check_for_input(mouse_pos):
                    print("Show the scores")
                if settings_button.check_for_input(mouse_pos):
                    print("Show the settings")
                

        pygame.display.update()

# Run the main menu
main_menu()