import pygame
# START PYGAME WOOOOO pygame
pygame.init()

# Create Display Window For Game
screen_width = 1600
screen_height = 900
game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Keyboard Battle")

# Set Colors used for Textures
background_layer = pygame.Surface((screen_width, screen_height))
interface_layer = pygame.Surface((screen_width, screen_height))

# Set Colors used for Textures
white = (255, 255, 255)
black = (0, 0, 0)
gray = (130, 130, 130)

# Set fonts Used for Text
font = pygame.font.Font(None, 36)

# Define the Functions for keyboard updates
class Valid_Dictionary:
    def __init__(self):
        self.shared_dictionary = open('TESTS/SpellBook.txt', "r")
        self.valid_words = self.shared_dictionary.read() 
        self.valid_word_list = self.valid_words.split("\n")
        self.shared_dictionary.close()
    
    def validWordChecker(self, current_typed_word:str):
        if current_typed_word in self.valid_word_list:
            return True
        else:
            return False

class Keyboard:
    def __init__(self):
        self.typed_text = ""
        self.cursor_position = 0
        self.max_character_count = 20
        self.valid_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
        
        self.no_letter_left = font.render("You Have None of this Character Left!", True, white)
        self.no_character_left = font.render("You Have No Characters Left!", True, white)
        self.not_in_dictionary = font.render("Word Not in your Dictionary", True, white)

    def keyboard_position(self):
        self.Key_Position = {}

        self.Letter_Positions_File = open('TESTS/Letter Positions.txt' , "r")
        self.Letter_Positions_File_Lines = self.Letter_Positions_File.readlines()

        for line in self.Letter_Positions_File_Lines:
            self.letter_pos = line[0]
            if line[7] == ",":
                self.position_x = int(line[4:7])
                self.position_y = int(line[9:12])
            else: 
                self.position_x = int(line[4:8])
                self.position_y = int(line[10:13])
            self.Key_Position[self.letter_pos] = (self.position_x, self.position_y)
        self.Letter_Positions_File.close()

    def key_amounts(self):
        self.Key_Count_Remaining = {}

        self.Letter_Amounts_File = open('TESTS/Letter_Amount.txt' , "r")
        self.Letter_Amounts_File_Lines = self.Letter_Amounts_File.readlines()

        for line in self.Letter_Amounts_File_Lines:
            self.letter_count = line[0]
            self.letter_amount = line[2]
            self.Key_Count_Remaining[self.letter_count] = int(self.letter_amount)
        self.Letter_Amounts_File.close

    def key_press_action(self, key:str,):
        self.pressed_key = key
        match self.pressed_key:
            case self.pressed_key if self.pressed_key in self.valid_letters and self.max_character_count > 0:
                if self.Key_Count_Remaining[self.pressed_key] > 0:
                    interface_layer.fill(black)
                    self.typed_text = self.typed_text[:self.cursor_position] + self.pressed_key + self.typed_text[self.cursor_position:]
                    self.cursor_position += 1
                    self.Key_Count_Remaining[self.pressed_key] -= 1
                    self.max_character_count -=1
                else:
                    interface_layer.fill(black)
                    interface_layer.blit(self.no_letter_left, (420, 200))

            case self.pressed_key if self.pressed_key in self.valid_letters and self.max_character_count == 0:
                interface_layer.fill(black)
                interface_layer.blit(self.no_character_left, (460, 200))

            case self.pressed_key if self.pressed_key == 'backspace' and self.cursor_position > 0:
                interface_layer.fill(black)
                self.deleted_key = self.typed_text[self.cursor_position - 1]  # Store the deleted key
                self.typed_text = self.typed_text[:self.cursor_position - 1] + self.typed_text[self.cursor_position:]
                self.cursor_position -= 1
                self.max_character_count += 1
                if self.deleted_key in self.valid_letters:
                    self.Key_Count_Remaining[self.deleted_key] += 1  # Add 1 to the count of the deleted key

    
            case self.pressed_key if self.pressed_key == 'return':
                if dictionary.validWordChecker(self.typed_text) == True:
                # Update Max Character Count and Display enterd word at top of Screen
                    interface_layer.fill(black)
                    self.displayed_text = font.render(self.typed_text, True, white) 
                    interface_layer.blit(self.displayed_text, ((screen_width/2 - (len(self.typed_text)*5)), 50))
                    self.typed_text = ""
                    self.cursor_position = 0
                else:
                    interface_layer.fill(black)
                    interface_layer.blit(self.not_in_dictionary, (480, 200))

def update_game_screen():
    '''
    Updates Game Window and associated Layers in order
    '''
    game_window.fill(black)
    game_window.blit(background_layer, (0,0))
    game_window.blit(interface_layer, (0,0))
    pygame.display.update()

# Intalize Variable for Typing Area
typing_area_height = 50
typing_area_y = 280

# Initalizes Variables from Classes

keyboard = Keyboard()
dictionary = Valid_Dictionary()

# Game loop
def battle_interface():
    character_counter = font.render(str(keyboard.max_character_count), True, white)
    interface_layer.blit(character_counter, (1050, 50))
    running = True
    keyboard.key_amounts()
    keyboard.keyboard_position()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                keyboard.key_press_action(key)
                character_counter = font.render(str(keyboard.max_character_count), True, white)
                interface_layer.blit(character_counter, (1050, 50))

    # Printing Graphics Areaaaaaaaaaaa

        # Black Background
        background_layer.fill(black)

        # Make Typing Area Grey Rectangle
        pygame.draw.rect(interface_layer, white, (380, typing_area_y, 520, typing_area_height))

        # Draw typed text and cursor
        typed_text_surface = font.render(keyboard.typed_text, True, black)
        interface_layer.blit(typed_text_surface, (400, typing_area_y + 12))

        # Draw keyboard and key counts
        for key, pos in keyboard.Key_Position.items():
            pygame.draw.rect(interface_layer, white, (pos[0], pos[1], 80, 100))
            key_text = font.render(key, True, black)
            count_text = font.render(str(keyboard.Key_Count_Remaining[key]), True, black)
            interface_layer.blit(key_text, (pos[0] + 30, pos[1] + 20))
            interface_layer.blit(count_text, (pos[0] + 30, pos[1] + 70))

        # Update display
        update_game_screen()

battle_interface()