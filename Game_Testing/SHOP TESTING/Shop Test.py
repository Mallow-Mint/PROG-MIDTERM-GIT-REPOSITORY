import pygame
import spritesheet 
pygame.init()

# Set up the display window 1600 x 900
win = pygame.display.set_mode((1600, 900))
# Background for everything in the shop
shop_bg_normal = pygame.image.load('Game_Testing/SHOP TESTING/Assets/trial wood shop bg.png')
currency_BG_normal = pygame.image.load('Game_Testing/SHOP TESTING/Assets/currency bg.png')
item_BG_normal = pygame.image.load('Game_Testing/SHOP TESTING/Assets/items bg.png')
item_frame_normal = pygame.image.load('Game_Testing/SHOP TESTING/Assets/item frames.png')
currency_BG = pygame.transform.scale(currency_BG_normal, (600 // 2, 300 // 2))
item_BG = pygame.transform.scale(item_BG_normal, (568 , 750 ))
shop_bg = pygame.transform.scale(shop_bg_normal, (1600 , 1117 * 0.81 ))
item_frame = pygame.transform.scale(item_frame_normal, (200, 200))

#variables for the sprites
sprite_sheet_image_1 = pygame.image.load('Game_Testing/SHOP TESTING/Assets/Healing potion OG.png').convert_alpha()
sprite_sheet_image_2 = pygame.image.load('Game_Testing/SHOP TESTING/Assets/XL Healing potion OG.png').convert_alpha()
sprite_sheet_image_3 = pygame.image.load('Game_Testing/SHOP TESTING/Assets/All Leter Potion OG.png').convert_alpha()
sprite_sheet_image_4 = pygame.image.load('Game_Testing/SHOP TESTING/Assets/Letter Potion OG.png').convert_alpha()
sprite_sheet_HpS = spritesheet.SpriteSheet(sprite_sheet_image_1)
sprite_sheet_HpXL = spritesheet.SpriteSheet(sprite_sheet_image_2)
sprite_sheet_AllLp = spritesheet.SpriteSheet(sprite_sheet_image_3)
sprite_sheet_Lp = spritesheet.SpriteSheet(sprite_sheet_image_4)

background_layer = pygame.Surface((1600, 900))
shop_layer = pygame.Surface((1600, 900))
inventory_layer = pygame.Surface((1600, 900))
sprite_layer = pygame.Surface((1600,900))
misc_layer = pygame.Surface((1600,900))

# Make Surfaces Transparent With Purple Color Key
PURPLE_COLOR_KEY = (255, 0, 255)
shop_layer.fill(PURPLE_COLOR_KEY)
shop_layer.set_colorkey((255, 0, 255))
inventory_layer.fill(PURPLE_COLOR_KEY)
inventory_layer.set_colorkey((255, 0, 255))
misc_layer.fill(PURPLE_COLOR_KEY)
misc_layer.set_colorkey((255, 0, 255))

# Make Dictionary of Letters and Cost
Letter_Cost_File = open('Game_Testing/SHOP TESTING/Assets/Letter Costs.txt', 'r')
Letter_Cost_File_Lines = Letter_Cost_File.readlines()
Letter_Cost_Dictionary = {}

# Make Dictionary of Letter and Letter Amounts
for line in Letter_Cost_File_Lines:
    letter, cost = line.strip().split(":")
    Letter_Cost_Dictionary[letter.strip()] = int(cost.strip())
Letter_Cost_File.close()

def screen_updater():
    win.fill(BLACK)
    background_layer.blit(shop_bg, (0, 0))
    win.blit(background_layer, (0, 0))
    win.blit(misc_layer, (0, 0))
    win.blit(shop_layer, (0, 0))
    win.blit(inventory_layer, (0, 0))

    pygame.display.update()

# Initialize the player's currency and inventory
default_currency = 200
player_currency = default_currency
inventory_slots = 6
inventory = [None] * inventory_slots

# Define colors
PURPLE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
LIGHT_GREY = (211, 211, 211)
BROWN = (150, 75, 0)
LIGHT_BROWN = (196, 164, 132)
YELLOW = (248, 255, 33)
TRANSPARENT = (0, 0, 0,)

# Creating animation list
animation_list_1 = []
animation_list_2 = []
animation_list_3 = []
animation_list_4 = []
animation_steps_1 = [15]  # Example: adjust this number to match your frames
animation_steps_2 = [24]
animation_steps_3 = [14]
animation_steps_4 = [22]
last_update_1 = pygame.time.get_ticks()
last_update_2 = pygame.time.get_ticks()
last_update_3 = pygame.time.get_ticks()
last_update_4 = pygame.time.get_ticks()
action_1 = 0
action_2 = 0
action_3 = 0
action_4 = 0
frame_1 = 0
frame_2 = 0
frame_3 = 0
frame_4 = 0
step_counter_1 = 0
step_counter_2 = 0
step_counter_3 = 0
step_counter_4 = 0
animation_cooldown = 75  # Time in milliseconds between frames

""" DONT JUDGE ME FOR THIS SECTION, TINATAMAD AKO GUMAWA NG CLASS OKAY!!!! IT WORKSSSSSSS!!"""
button1 = Button('Click me',200,40,(200,250),5)
# Rolling for the First Sprite Image
for animation_1 in animation_steps_1:
    temp_img_list_1 = []
    for _ in range(animation_1):
        img_1 = sprite_sheet_HpS.get_image(step_counter_1, 19, 38, 2.4, BLACK)# Adjust parameters as needed
        if img_1 is not None:  # Ensure we have a valid image
            temp_img_list_1.append(img_1)
        step_counter_1 += 1
    animation_list_1.append(temp_img_list_1)
#Rolling for the Second Sprite Image
for animation_2 in animation_steps_2:
    temp_img_list_2 = []
    for _ in range(animation_2):
        img_2 = sprite_sheet_HpXL.get_image(step_counter_2, 18, 34, 2.5, BLACK)# Adjust parameters as needed
        if img_2 is not None:  # Ensure we have a valid image
            temp_img_list_2.append(img_2)
        step_counter_2 += 1
    animation_list_2.append(temp_img_list_2)
# Rolling for the Third Sprite Image
for animation_3 in animation_steps_3:
    temp_img_list_3 = []
    for _ in range(animation_3):
        img_3 = sprite_sheet_AllLp.get_image(step_counter_3, 16, 51, 2, BLACK)# Adjust parameters as needed
        if img_3 is not None:  # Ensure we have a valid image
            temp_img_list_3.append(img_3)
        step_counter_3 += 1
    animation_list_3.append(temp_img_list_3)
# Rolling for the Fourth Sprite Image
for animation_4 in animation_steps_4:
    temp_img_list_4 = []
    for _ in range(animation_4):
        img_4 = sprite_sheet_Lp.get_image(step_counter_4, 18, 35, 2.5, BLACK)# Adjust parameters as needed
        if img_4 is not None:  # Ensure we have a valid image
            temp_img_list_4.append(img_4)
        step_counter_4 += 1
    animation_list_4.append(temp_img_list_4)

# Function to load and return the custom font
def get_font(size):
    return pygame.font.Font("Game_Testing/SHOP TESTING/Assets/Shop Font.ttf", size)

# Function to draw text using the custom font
def draw_text(shop_layer, text, font_size, x, y, color=PURPLE):
    font = get_font(font_size)
    render = font.render(text, True, color)
    shop_layer.blit(render, (x, y))

# Class for a shop item
class ShopItem:
    def __init__(self, name, price, item_type):
        self.name = name
        self.price = price
        self.item_type = item_type

    def display(self, shop_layer, x, y, width, height):
        pygame.draw.rect(shop_layer, BROWN if self.item_type == "Potion" else LIGHT_BROWN, (x, y, width, height))
        draw_text(shop_layer, self.name, 15, x + 10, y + 16)
        draw_text(shop_layer, f"${self.price}", 15, x + 30, y + 65)

# Class for the shop with categories
# Modify the Shop class to display potions in a 2x2 grid with potion boxes
class Shop:
    def __init__(self):
        self.categories = ["Potions", "Letters"]
        self.active_category = "Potions"
        self.shop_type = self.active_category

        # Define renamed potions and letters
        self.potions = [
            ShopItem("Healing Potion S", 20, "Potion"),
            ShopItem("Healing Potion XL", 50, "Potion"),
            ShopItem("Letter Potion", 25, "Potion"),
            ShopItem("All Letter Potion", 50, "Potion")
        ]
        self.letters = [ShopItem(letter, price, "Letter") for letter, price in Letter_Cost_Dictionary.items()]

    def display_shop(self, shop_layer):
        # Display category tabs
        for i, category in enumerate(self.categories):
            color = LIGHT_GREY if category == self.active_category else PURPLE
            pygame.draw.rect(shop_layer, color, (160 + i * 160, 50, 180, 60))
            draw_text(shop_layer, category, 20, 174 + i * 160, 70, BLACK)

        # Display items from the active category
        if self.active_category == "Potions":
            self.display_potions(shop_layer)
            inventory.display_inventory(inventory_layer)
        elif self.active_category == "Letters":
            self.display_letters(shop_layer)

    def display_potions(self, shop_layer):
        draw_text(shop_layer, "Potions", 20, 400, 150)

        # 2x2 grid setup for potion boxes
        potion_box_width = 150
        potion_box_height = 150
        grid_start_x = 270
        grid_start_y = 220
        spacing = 250

        # Draw each potion in the 2x2 grid
        for i, potion in enumerate(self.potions):
            row = i // 2
            col = i % 2
            x = grid_start_x + col * spacing
            y = grid_start_y + row * spacing

            # Draw potion name above the box
            draw_text(shop_layer, potion.name, 13, x - 20, y - 25, BLACK)

            # Draw the "Buy for $price" rectangle below the potion box
            buy_box_x = x
            buy_box_y = y + potion_box_height + 10
            buy_box_width = potion_box_width
            buy_box_height = 30
            pygame.draw.rect(shop_layer, YELLOW, (buy_box_x, buy_box_y, buy_box_width, buy_box_height))
            draw_text(shop_layer, f"Buy for ${potion.price}", 13, buy_box_x + 5, buy_box_y + 10, GREY)

            # Draw the sprite for Healing Potion XL in the correct position
            if potion.name == "Healing Potion S":  # Check if this is the target potion
                sprite_x = x + 40  # X position for the sprite (same as potion box)
                sprite_y = y  # Y position for the sprite (same as potion box)
                shop_layer.blit(animation_list_1[0][frame_1], (sprite_x + 18, sprite_y + 18))  # Blit the sprite at the potion position
                misc_layer.blit(item_frame, (sprite_x - 63, sprite_y - 25))
                misc_layer.blit(item_frame, (sprite_x + 185, sprite_y + 223))
                misc_layer.blit(item_frame, (sprite_x - 63, sprite_y + 223))
                misc_layer.blit(item_frame, (sprite_x + 185, sprite_y - 25))
            if potion.name == "Healing Potion XL":  # Check if this is the target potion
                sprite_x = x + 40  # X position for the sprite (same as potion box)
                sprite_y = y  # Y position for the sprite (same as potion box)
                shop_layer.blit(animation_list_2[0][frame_2], (sprite_x + 15, sprite_y + 23))  # Blit the sprite at the potion position
            if potion.name == "All Letter Potion":  # Check if this is the target potion
                sprite_x = x + 40  # X position for the sprite (same as potion box)
                sprite_y = y  # Y position for the sprite (same as potion box)
                shop_layer.blit(animation_list_3[0][frame_3], (sprite_x + 21, sprite_y + 8))  # Blit the sprite at the potion position
            if potion.name == "Letter Potion":  # Check if this is the target potion
                sprite_x = x + 40  # X position for the sprite (same as potion box)
                sprite_y = y  # Y position for the sprite (same as potion box)
                shop_layer.blit(animation_list_4[0][frame_4], (sprite_x + 15, sprite_y + 20))  # Blit the sprite at the potion position



    def display_letters(self, shop_layer):
        draw_text(shop_layer, "Letters", 20, 400, 150)
        for i, letter in enumerate(self.letters):
            x_offset = (i % 5) * 120  # Horizontal spacing between boxes
            y_offset = (i // 5) * 80   # Vertical spacing between rows
            letter.display(shop_layer, 200 + x_offset, 220 + y_offset, 90, 50)

    def get_clicked_item(self, mx, my):
        if self.active_category == "Potions":
            for i, potion in enumerate(self.potions):
                row = i // 2
                col = i % 2
                x = 270 + col * 250  # Adjusted to match the x position of the potion boxes
                y = 220 + row * 250 + 150 + 10  # Adjusted to the "Buy" box position (below the potion box)
                if pygame.Rect(x, y, 150, 30).collidepoint(mx, my):
                    return potion
        elif self.active_category == "Letters":
            for i, letter in enumerate(self.letters):
                x_offset = (i % 5) * 120  # Horizontal spacing between boxes
                y_offset = (i // 5) * 80   # Vertical spacing between rows
                if pygame.Rect(200 + x_offset, 220 + y_offset, 90, 50).collidepoint(mx, my):
                    return letter
        return None


    def switch_category(self, mx, my):
        # Adjust the x and y positions of the category tabs to match the positions in the shop
        potions_tab_rect = pygame.Rect(160, 50, 180, 60)  # Coordinates for the "Potions" tab
        letters_tab_rect = pygame.Rect(320, 50, 180, 60)  # Coordinates for the "Letters" tab

        # Check if the user clicked on the "Potions" tab
        if potions_tab_rect.collidepoint(mx, my):
            shop_layer.fill(PURPLE_COLOR_KEY)
            self.active_category = "Potions"
            self.shop_type = self.active_category

        # Check if the user clicked on the "Letters" tab
        elif letters_tab_rect.collidepoint(mx, my):
            shop_layer.fill(PURPLE_COLOR_KEY)
            inventory_layer.fill(PURPLE_COLOR_KEY)
            misc_layer.fill(PURPLE_COLOR_KEY)
            self.active_category = "Letters"
            self.shop_type = self.active_category

# Class for inventory
class Inventory:
    def __init__(self, slots):
        self.slots = [None] * slots

    def add_to_inventory(self, item, shop_type):
        if shop.shop_type == "Potions":
            for i in range(len(self.slots)):
                if self.slots[i] is None:
                    self.slots[i] = item
                    return True
            return False
        else:
            return False

    def clear_inventory(self):
        self.slots = [None] * len(self.slots)

    def display_inventory(self, inventory_layer):
        # Place the inventory in the top right corner in a 2x3 grid
        inv_x = 1000  # Starting x position (near the right side of the screen)
        inv_y = 190  # Starting y position (upper part of the screen)
        inventory_layer.blit(item_BG, (881, -20))

        # Draw the inventory label
        draw_text(inventory_layer, "Inventory", 20, inv_x + 75, inv_y - 87)

        # Iterate over each inventory slot and position it in a 2x3 grid
        for i in range(len(self.slots)):
            row = i // 2  # There are 2 columns, so the row is calculated based on index // 2
            col = i % 2   # Column is either 0 (left) or 1 (right)

            # Adjust positions for the 2x3 layout
            x_pos = inv_x + col * 175  # 175 px spacing between columns
            y_pos = inv_y + row * 130  # 100 px spacing between rows

            # Draw a slot (adjusted size for better fit)
            pygame.draw.rect(inventory_layer, YELLOW, (x_pos, y_pos, 150, 80), 5)

            # If an item exists in this slot, display its name
            if self.slots[i] is not None:
                draw_text(inventory_layer, self.slots[i].name, 15, x_pos + 5, y_pos + 30)
                

# Function to display the player's currency with background
def display_currency(inventory_layer, currency):
    # Coordinates where you want to display the currency background and the currency text
    currency_bg_x = 310
    currency_bg_y = 730  # Adjust the Y position to place it slightly above the edge
    text_x = currency_bg_x + 48  # Add a small padding to position the text nicely within the background
    text_y = currency_bg_y + 67  # Adjust the Y position to center the text within the background

    # First, blit the currency background
    inventory_layer.blit(currency_BG, (currency_bg_x, currency_bg_y))

    # Then, draw the player's currency text on top of the background
    draw_text(inventory_layer, f"Currency: ${currency}", 15, text_x, text_y,)

# Function to handle item purchase
def purchase_item(item, inventory, currency, shop_type):
    if currency >= item.price:
        if inventory.add_to_inventory(item, shop_type):
            inventory_layer.fill(PURPLE_COLOR_KEY)
            currency -= item.price
    return currency

# Button class for creating buttons
class Button:
    def __init__(self, x, y, w, h, text, color):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = color

    def draw(self, shop_layer):
        pygame.draw.rect(shop_layer, self.color, self.rect)
        draw_text(shop_layer, self.text, 20, self.rect.x + 10, self.rect.y + 10, BLACK)

    def is_clicked(self, mx, my):
        return self.rect.collidepoint(mx, my)

# Main loop
run = True
clock = pygame.time.Clock()

# Initialize the shop and inventory
shop = Shop()
inventory = Inventory(inventory_slots)

# Create reset button
reset_button = Button(1200, 700, 150, 50, "Reset", RED)  # Adjusted button position for new resolution

while run:
    current_time_1 = pygame.time.get_ticks()
    current_time_2 = pygame.time.get_ticks()
    current_time_3 = pygame.time.get_ticks()
    current_time_4 = pygame.time.get_ticks()
    if current_time_1 - last_update_1 >= animation_cooldown:
        frame_1 += 1
        last_update_1 = current_time_1
        if frame_1 >= len(animation_list_1[action_1]):
            frame_1 = 0
    if current_time_2 - last_update_2 >= animation_cooldown:
        frame_2 += 1
        last_update_2 = current_time_2
        if frame_2 >= len(animation_list_2[action_2]):
            frame_2 = 0
    if current_time_3 - last_update_3 >= animation_cooldown:
        frame_3 += 1
        last_update_3 = current_time_3
        if frame_3 >= len(animation_list_3[action_3]):
            frame_3 = 0 
    if current_time_4 - last_update_4 >= animation_cooldown:
        frame_4 += 1
        last_update_4 = current_time_4
        if frame_4 >= len(animation_list_4[action_4]):
            frame_4 = 0    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            shop.switch_category(mx, my)

            clicked_item = shop.get_clicked_item(mx, my)
            if clicked_item is not None:
                player_currency = purchase_item(clicked_item, inventory, player_currency, shop.shop_type)

            if reset_button.is_clicked(mx, my):
                shop_layer.fill(PURPLE_COLOR_KEY)
                inventory_layer.fill(PURPLE_COLOR_KEY)
                player_currency = default_currency
                inventory.clear_inventory()

    shop.display_shop(shop_layer)
    display_currency(inventory_layer, player_currency)

    # Draw the reset button
    reset_button.draw(shop_layer)

    # Call to display the inventory
    inventory.display_inventory(inventory_layer)

    screen_updater()
    clock.tick(30)

pygame.quit()