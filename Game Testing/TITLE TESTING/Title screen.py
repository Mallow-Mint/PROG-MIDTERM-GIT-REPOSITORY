import pygame
import sys

# Initialize Pygame
pygame.init()

Title_BG = pygame.image.load('Assets/Background/bg_15/bg_15.png')
# Set up display
SCREEN = pygame.display.set_mode((1300, 650))
pygame.display.set_caption("Spell Book")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# Load font
def get_font(size):
    return pygame.font.Font('Assets/Fonts/minercraftory/Minercraftory.ttf', size)

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
        SCREEN.blit(Title_BG, (-100, 0))
        # Get mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Title text
        title_text = get_font(100).render("SPELL BOOK", True, BLACK)
        title_rect = title_text.get_rect(center=(650, 200))
        SCREEN.blit(title_text, title_rect)

        # Create buttons
        start_button = Button((650, 300), "NEW GAME", get_font(32), BLACK, GRAY)
        tutorial_button = Button((650, 350), "TUTORIALS", get_font(32), BLACK, GRAY)
        scores_button = Button((650, 400), "SCORES", get_font(32), BLACK, GRAY)
        quit_button = Button((650, 450), "QUIT", get_font(32), BLACK, GRAY)
    

        # Change button color based on mouse position
        start_button.change_color(mouse_pos)
        tutorial_button.change_color(mouse_pos)
        scores_button.change_color(mouse_pos)
        quit_button.change_color(mouse_pos)


        # Draw buttons
        start_button.draw(SCREEN)
        tutorial_button.draw(SCREEN)
        scores_button.draw(SCREEN)
        quit_button.draw(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.check_for_input(mouse_pos):
                    print("Start the game")  # Replace with your game starting function
                if tutorial_button.check_for_input(mouse_pos):
                    print("Start the tutorial")
                if scores_button.check_for_input(mouse_pos):
                    print("Show scores")
                if quit_button.check_for_input(mouse_pos):
                    pygame.quit()
                    sys.exit()
                

        pygame.display.update()

# Run the main menu
main_menu()