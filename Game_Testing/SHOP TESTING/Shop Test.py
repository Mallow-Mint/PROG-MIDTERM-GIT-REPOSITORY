import pygame

pygame.init()

# Set up the display window 1600 x 900
win = pygame.display.set_mode((1600, 900))
# Background for the shop
BG = pygame.image.load("Game_Testing/SHOP TESTING/Assets/wooden shop bg.png")

background_layer = pygame.Surface((1600, 900))
shop_layer = pygame.Surface((1600, 900))
inventory_layer = pygame.Surface((1600, 900))

# Make Surfaces Transparent With Purple Color Key
PURPLE_COLOR_KEY = (255, 0, 255)
shop_layer.fill(PURPLE_COLOR_KEY)
shop_layer.set_colorkey((255, 0, 255))
inventory_layer.fill(PURPLE_COLOR_KEY)
inventory_layer.set_colorkey((255, 0, 255))

# Make Dictionary of Letters and Cost
Letter_Cost_File = open('Game_Testing/SHOP TESTING/Assets/Letter Costs.txt', "r")
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

# Function to load and return the custom font
def get_font(size):
    return pygame.font.Font("Game_Testing/SHOP TESTING/Assets/Shop Font.ttf", size)

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
class Shop:
    def __init__(self):
        self.categories = ["Potions", "Letters"]
        self.active_category = "Potions"
        self.shop_type = self.active_category

        # Define renamed potions and letters
        self.potions = [ShopItem("Healing Potion S", 20, "Potion"), 
                        ShopItem("Healing Potion XL", 50, "Potion"), 
                        ShopItem("Letter Potion", 25, "Potion"), 
                        ShopItem("All Letter Potion", 50, "Potion")]
        self.letters = [ShopItem(letter, price, "Letter") for letter, price in Letter_Cost_Dictionary.items()]
        
        self.selected_item = None

    def display_shop(self, shop_layer):
        # Display category tabs
        for i, category in enumerate(self.categories):
            color = LIGHT_GREY if category == self.active_category else WHITE
            pygame.draw.rect(shop_layer, color, (80 + i * 160, 50, 180, 60))  # Adjusted for new window size
            draw_text(shop_layer, category, 30, 100 + i * 160, 60, BLACK)

        # Display items from the active category
        if self.active_category == "Potions":
            self.display_potions(shop_layer)
            inventory.display_inventory(inventory_layer)
        elif self.active_category == "Letters":
            self.display_letters(shop_layer)

    def display_potions(self, shop_layer):
        draw_text(shop_layer, "Potions", 30, 130, 150)
        for i, potion in enumerate(self.potions):
            # Adjust box size and spacing for potions
            potion.display(shop_layer, 130 + i * 250, 200, 220, 90)

    def display_letters(self, shop_layer):
        draw_text(shop_layer, "Letters", 30, 130, 150)
        for i, letter in enumerate(self.letters):
            x_offset = (i % 7) * 100  # Horizontal spacing between boxes
            y_offset = (i // 7) * 80   # Vertical spacing between rows
            letter.display(shop_layer, 130 + x_offset, 200 + y_offset, 90, 50)

    def get_clicked_item(self, mx, my):
        if self.active_category == "Potions":
            for i, potion in enumerate(self.potions):
                # Align the hitbox with the visual potion boxes
                if pygame.Rect(130 + i * 250, 200, 220, 90).collidepoint(mx, my):
                    return potion
        elif self.active_category == "Letters":
            for i, letter in enumerate(self.letters):
                x_offset = (i % 7) * 100  # Match horizontal spacing
                y_offset = (i // 7) * 80   # Match vertical spacing
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
        # Inventory placed in the middle of the screen in a 2x3 grid
        inv_x_start = (1600 - (2 * 175)) // 2  # Adjusted to center based on new window size
        inv_y_start = 520  # Adjusted starting y position for inventory

        draw_text(inventory_layer, "Inventory", 20, inv_x_start, inv_y_start - 30)

        for i in range(len(self.slots)):
            row = i // 3  # Calculate row (2 rows: 0 or 1)
            col = i % 3   # Calculate column (3 columns: 0, 1, 2)
            x_pos = inv_x_start + col * 400  # Adjusted horizontal position with spacing
            y_pos = inv_y_start + row * 100  # Adjusted vertical position with spacing

            pygame.draw.rect(inventory_layer, YELLOW, (x_pos, y_pos, 265, 70), 5)  # Adjusted slot size

            if self.slots[i] is not None:
                draw_text(inventory_layer, self.slots[i].name, 15, x_pos + 5, y_pos + 20)

# Function to display the player's currency
def display_currency(inventory_layer, currency):
    draw_text(inventory_layer, f"Currency: ${currency}", 30, 1300, 80)

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
reset_button = Button(1420, 640, 150, 50, "Reset", RED)  # Adjusted button position for new resolution

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            # Check if the category tab was clicked
            shop.switch_category(mx, my)

            # Check if an item was clicked in the active category
            clicked_item = shop.get_clicked_item(mx, my)
            if clicked_item is not None:
                player_currency = purchase_item(clicked_item, inventory, player_currency, shop.shop_type)

            # Check if reset button was clicked
            if reset_button.is_clicked(mx, my):
                shop_layer.fill(PURPLE_COLOR_KEY)
                inventory_layer.fill(PURPLE_COLOR_KEY)
                player_currency = default_currency
                inventory.clear_inventory()

    shop.display_shop(shop_layer)
    display_currency(inventory_layer, player_currency)

    # Draw the reset button
    reset_button.draw(shop_layer)
    screen_updater()
    clock.tick(30)

pygame.quit()
