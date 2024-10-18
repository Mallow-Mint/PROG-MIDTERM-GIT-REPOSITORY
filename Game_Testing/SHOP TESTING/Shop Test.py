import pygame
from pygame_functions_shop import *
pygame.init()

# Set up the display window 1600 x 900
win = pygame.display.set_mode((1600, 900))
# Background for the shop
BG = pygame.image.load("Assets/wooden shop bg.png")

background_layer = pygame.Surface((1600, 900))
shop_layer = pygame.Surface((1600, 900))
inventory_layer = pygame.Surface((1600, 900))

nextFrame = clock()
frame = 0
potion_XL_SS = 'Assets/XL healing potion 14 MS.png'
test_sprite_1 = makeSprite(potion_XL_SS, 24)

# Make Surfaces Transparent With Purple Color Key
PURPLE_COLOR_KEY = (255, 0, 255)
shop_layer.fill(PURPLE_COLOR_KEY)
shop_layer.set_colorkey((255, 0, 255))
inventory_layer.fill(PURPLE_COLOR_KEY)
inventory_layer.set_colorkey((255, 0, 255))

# Make Dictionary of Letters and Cost
Letter_Cost_File = open('Assets/Letter Costs.txt', "r")
Letter_Cost_File_Lines = Letter_Cost_File.readlines()
Letter_Cost_Dictionary = {}

# Make Dictionary of Letter and Letter Amounts
for line in Letter_Cost_File_Lines:
    letter, cost = line.strip().split(":")
    Letter_Cost_Dictionary[letter.strip()] = int(cost.strip())
Letter_Cost_File.close()

def screen_updater():
    win.fill(BLACK)
    background_layer.blit(BG, (0, 0))
    win.blit(background_layer, (0, 0))
    win.blit(shop_layer, (0, 0))
    win.blit(inventory_layer, (0, 0))

    pygame.display.update()

# Initialize the player's currency and inventory
default_currency = 200
player_currency = default_currency
inventory_slots = 6
inventory = [None] * inventory_slots

# Define colors
WHITE = (255, 255, 255)
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

# Function to load and return the custom font
def get_font(size):
    return pygame.font.Font("Assets/Shop Font.ttf", size)

# Function to draw text using the custom font
def draw_text(shop_layer, text, font_size, x, y, color=WHITE):
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

        self.potions = [
            ShopItem("Healing Potion S", 20, "Potion"),
            ShopItem("Healing Potion XL", 50, "Potion"),
            ShopItem("Letter Potion", 25, "Potion"),
            ShopItem("All Letter Potion", 50, "Potion")
        ]
        self.letters = [ShopItem(letter, price, "Letter") for letter, price in Letter_Cost_Dictionary.items()]

    def display_shop(self, shop_layer):
        for i, category in enumerate(self.categories):
            color = LIGHT_GREY if category == self.active_category else WHITE
            pygame.draw.rect(shop_layer, color, (160 + i * 160, 50, 180, 60))
            draw_text(shop_layer, category, 20, 174 + i * 160, 70, BLACK)

        if self.active_category == "Potions":
            self.display_potions(shop_layer)
            inventory.display_inventory(inventory_layer)
        elif self.active_category == "Letters":
            self.display_letters(shop_layer)

    def display_potions(self, shop_layer):
        draw_text(shop_layer, "Potions", 20, 300, 150)

        potion_box_width = 150
        potion_box_height = 150
        grid_start_x = 270
        grid_start_y = 220
        spacing = 250

        for i, potion in enumerate(self.potions):
            row = i // 2
            col = i % 2
            x = grid_start_x + col * spacing
            y = grid_start_y + row * spacing

            pygame.draw.rect(shop_layer, PURPLE_COLOR_KEY, (x, y, potion_box_width, potion_box_height))
            draw_text(shop_layer, potion.name, 15, x, y - 25, BLACK)

            buy_box_x = x
            buy_box_y = y + potion_box_height + 10

            if potion.name == "Healing Potion S":
                changeSpriteImage(test_sprite_1, 0 * 14 + frame)
                moveSprite(test_sprite_1, buy_box_x, buy_box_y, True)
                showSprite(test_sprite_1)

            draw_text(shop_layer, f"Buy for ${potion.price}", 13, buy_box_x + 5, buy_box_y + 10, GREY)

    def display_letters(self, shop_layer):
        draw_text(shop_layer, "Letters", 30, 130, 150)
        for i, letter in enumerate(self.letters):
            x_offset = (i % 7) * 100
            y_offset = (i // 7) * 80
            letter.display(shop_layer, 130 + x_offset, 200 + y_offset, 90, 50)

    def get_clicked_item(self, mx, my):
        if self.active_category == "Potions":
            for i, potion in enumerate(self.potions):
                row = i // 2
                col = i % 2
                x = 130 + col * 200
                y = 220 + row * 200
                if pygame.Rect(x, y, 150, 150).collidepoint(mx, my):
                    return potion
        elif self.active_category == "Letters":
            for i, letter in enumerate(self.letters):
                x_offset = (i % 7) * 100
                y_offset = (i // 7) * 80
                if pygame.Rect(130 + x_offset, 200 + y_offset, 90, 50).collidepoint(mx, my):
                    return letter
        return None

    def switch_category(self, mx, my):
        if pygame.Rect(80, 50, 160, 50).collidepoint(mx, my):
            shop_layer.fill(PURPLE_COLOR_KEY)
            self.active_category = "Potions"
            self.shop_type = self.active_category
        elif pygame.Rect(240, 50, 160, 50).collidepoint(mx, my):
            shop_layer.fill(PURPLE_COLOR_KEY)
            inventory_layer.fill(PURPLE_COLOR_KEY)
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
        inv_x_start = 1000  # Starting x position (near the right side of the screen)
        inv_y_start = 190  # Starting y position (upper part of the screen)

        # Draw the inventory label
        draw_text(inventory_layer, "Inventory", 20, inv_x_start, inv_y_start - 30)

        # Iterate over each inventory slot and position it in a 2x3 grid
        for i in range(len(self.slots)):
            row = i // 2  # There are 2 columns, so the row is calculated based on index // 2
            col = i % 2   # Column is either 0 (left) or 1 (right)

            # Adjust positions for the 2x3 layout
            x_pos = inv_x_start + col * 175  # 175 px spacing between columns
            y_pos = inv_y_start + row * 100  # 100 px spacing between rows

            # Draw a slot (adjusted size for better fit)
            pygame.draw.rect(inventory_layer, YELLOW, (x_pos, y_pos, 150, 80), 5)

            # If an item exists in this slot, display its name
            if self.slots[i] is not None:
                draw_text(inventory_layer, self.slots[i].name, 15, x_pos + 5, y_pos + 30)



# Function to display the player's currency
def display_currency(inventory_layer, currency):
    draw_text(inventory_layer, f"Currency: ${currency}", 20, 350, 750)

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
running = True
# Create reset button
reset_button = Button(1420, 640, 150, 50, "Reset", RED)  # Adjusted button position for new resolution

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
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

    if clock() > nextFrame:  # To animate the sprite
        frame = (frame + 1) % 24  # Update the frame for animation
        nextFrame += 80  # Timing for the animation
                
        shop.display_shop(shop_layer)
        display_currency(inventory_layer, player_currency)

        # Draw the reset button
        reset_button.draw(shop_layer)

        # Call to display the inventory
        inventory.display_inventory(inventory_layer)

        screen_updater()
        clock.tick(30)

    pygame.quit()
