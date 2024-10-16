import pygame
import os
os.chdir('/Users/Tina Miranda/Documents/AIM/PROG/MIDTERMS/TESTS')
# START PYGAME WOOOOO pygame
pygame.init()

# Create Display Window For Game
screen_width = 1280
screen_height = 800
display_width = 1280
display_height = 720
game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Keyboard Battle")

# Set Colors used for Textures
background_layer = pygame.Surface((display_width, display_height))
interface_layer = pygame.Surface((display_width, display_height))

# Set Colors used for Textures
white = (255, 255, 255)
black = (0, 0, 0)
gray = (130, 130, 130)

# Set fonts Used for Text
font = pygame.font.Font(None, 36)

# Read Positions of Letters in Text File
Key_Updater = {}

Letter_Positions_File = open('Keyboard Tests/Letter Positions.txt' , "r")
Letter_Positions_File_Lines = Letter_Positions_File.readlines()

for line in Letter_Positions_File_Lines:
    letter = line[0]
    if line[7] == ",":
        position_x = int(line[4:7])
        position_y = int(line[9:12])
    else: 
        position_x = int(line[4:8])
        position_y = int(line[10:13])
    Key_Updater[letter] = (position_x, position_y)

# Read Valid Words in Dictonary
shared_dictionary = open('Keyboard Tests/SpellBook.txt', "r")
valid_words = shared_dictionary.read() 
valid_word_list = valid_words.split("\n")
shared_dictionary.close()

def update_game_screen():
    '''
    Updates Game Window and associated Layers in order
    '''
    game_window.fill(black)
    game_window.blit(background_layer, (0,0))
    game_window.blit(interface_layer, (0,0))
    pygame.display.update()

def validWordChecker(current_typed_word:str):
    global valid_word_list
    if current_typed_word in valid_word_list:
        return True
    else:
        return False

# Keyboard layout


# Key press counts
key_press_counts = {key: 5 for key in Key_Updater.keys()}

# Typing area variables
# Intalize Variable for Printing 
typing_area_height = 50
typing_area_y = 280
typed_text = ""
cursor_position = 0
max_character_count = 20

# Game loop
character_counter = font.render(str(max_character_count), True, white)
interface_layer.blit(character_counter, (1050, 50))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            if max_character_count > 0:
                if key in Key_Updater:
                    if key_press_counts[key] == 0:
                        interface_layer.fill(black)
                        no_letter_left = font.render("You Have None of this Character Left!", True, white)
                        interface_layer.blit(no_letter_left, (420, 200))
                    if key_press_counts[key] > 0:
                        interface_layer.fill(black)
                        typed_text = typed_text[:cursor_position] + key + typed_text[cursor_position:]
                        cursor_position += 1
                        key_press_counts[key] -= 1
                        max_character_count -=1
                elif key == 'backspace':
                    if cursor_position > 0:
                        interface_layer.fill(black)
                        deleted_key = typed_text[cursor_position - 1]  # Store the deleted key
                        typed_text = typed_text[:cursor_position - 1] + typed_text[cursor_position:]
                        cursor_position -= 1
                        max_character_count += 1
                        if deleted_key in Key_Updater:
                            key_press_counts[deleted_key] += 1  # Add 1 to the count of the deleted key
                elif key == 'return':
                    if validWordChecker(typed_text) == True:
                    # Update Max Character Count and Display enterd word at top of Screen
                        interface_layer.fill(black)
                        displayed_text = font.render(typed_text, True, white) 
                        interface_layer.blit(displayed_text, ((screen_width/2 - (len(typed_text)*5)), 50))
                        typed_text = ""
                        cursor_position = 0
                    else:
                        interface_layer.fill(black)
                        invalid_word_popup = font.render("Word Not in your Dictionary", True, white) 
                        interface_layer.blit(invalid_word_popup, (480, 200))
            elif max_character_count == 0:
                if key == 'backspace':
                    interface_layer.fill(black)
                    deleted_key = typed_text[cursor_position - 1]  # Store the deleted key
                    typed_text = typed_text[:cursor_position - 1] + typed_text[cursor_position:]
                    cursor_position -= 1
                    max_character_count += 1
                    if deleted_key in Key_Updater:
                        key_press_counts[deleted_key] += 1  # Add 1 to the count of the deleted key
                if key == 'return':
                    if validWordChecker(typed_text) == True:
                    # Update Max Character Count and Display enterd word at top of Screen
                        interface_layer.fill(black)
                        displayed_text = font.render(typed_text, True, white) 
                        interface_layer.blit(displayed_text, ((screen_width/2 - (len(typed_text)*5)), 50))
                        typed_text = ""
                        cursor_position = 0
                    else:
                        interface_layer.fill(black)
                        invalid_word_popup = font.render("Word Not in your Dictionary", True, white) 
                        interface_layer.blit(invalid_word_popup, (480, 200))
                if key in Key_Updater:
                    interface_layer.fill(black)
                    no_characters_left_warning = font.render("You Have No Characters Left!", True, white)
                    interface_layer.blit(no_characters_left_warning, (460, 200))
            character_counter = font.render(str(max_character_count), True, white)
            interface_layer.blit(character_counter, (1050, 50))
# Printing Graphics Areaaaaaaaaaaa

    # Black Background
    background_layer.fill(black)

    # Make Typing Area Grey Rectangle
    pygame.draw.rect(interface_layer, white, (380, typing_area_y, 520, typing_area_height))

    # Draw typed text and cursor
    typed_text_surface = font.render(typed_text, True, black)
    interface_layer.blit(typed_text_surface, (400, typing_area_y + 12))

    # Draw keyboard and key counts
    for key, pos in Key_Updater.items():
        pygame.draw.rect(interface_layer, white, (pos[0], pos[1], 80, 100))
        key_text = font.render(key, True, black)
        count_text = font.render(str(key_press_counts[key]), True, black)
        interface_layer.blit(key_text, (pos[0] + 30, pos[1] + 20))
        interface_layer.blit(count_text, (pos[0] + 30, pos[1] + 70))

    # Update display
    update_game_screen()

# Quit pygame
pygame.quit()