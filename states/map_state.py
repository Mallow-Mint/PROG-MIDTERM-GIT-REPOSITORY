import pygame
import sys
from states.state_manager import *
from states.battle_state import *
from states.shop_state import *

# State Class of
class Map(State):
    def __init__(self, game):
        State.__init__(self, game)
    
    def update(self):
        if room.enter_battle:
            initalize_battle()
            new_state = Battle(self.game)
            new_state.enter_state()
            room.enter_battle = False
            map.current_screen = "map"
        
        if room.enter_shop:
            shop_initializer()
            new_state = Shop_State(self.game)
            new_state.enter_state()
            room.enter_shop = False
            map.current_screen = "map"

        if map.node8.state == "completed" and character.battle_state == 'WIN':
            self.exit_state()
            map.reset_map()
            character.battle_state = None

    def render(self, display):
        main_map()
        display.blit(screen, (0,0))

class Map_Room:
    def __init__(self):
        self.enter_battle = False
        self.enter_shop = False

class Map_Menu:
    def __init__(self):
        self.current_screen = "map"
        # Create the nodes with associated screen types
        self.node1 = Node(270, 420, 30, state="available", screen_type="battle")  # Starting node on map screen
        self.node2 = Node(420, 420, 30, state="locked", screen_type="battle")  # Battle screen node
        self.node3 = Node(570, 420, 30, state="locked", screen_type="shop")    # Shop screen node
        self.node4 = Node(720, 420, 30, state="locked", screen_type="battle")
        self.node5 = Node(870, 420, 30, state="locked", screen_type="battle")
        self.node6 = Node(1020, 420, 30, state="locked", screen_type="battle")
        self.node7 = Node(1170, 420, 30, state="locked", screen_type="shop")
        self.node8 = Node(1320, 420, 30, state="locked", screen_type="battle")


        # Set up connections (which nodes unlock others)
        self.node1.connected_nodes = [self.node2]  # Clicking node1 unlocks node2 
        self.node2.connected_nodes = [self.node3]  # Clicking node2 unlocks node3
        self.node3.connected_nodes = [self.node4] 
        self.node4.connected_nodes = [self.node5]
        self.node5.connected_nodes = [self.node6] 
        self.node6.connected_nodes = [self.node7] 
        self.node7.connected_nodes = [self.node8] 


        self.nodes = [self.node1, self.node2, self.node3, self.node4, self.node5, self.node6, self.node7, self.node8]

        # Create the 'Return to Map' button
        self.return_button = Button(600, 500, 150, 50, "Return to Map")
    
    def reset_map(self):
        self.node1.state = "available"
        self.node2.state = "locked"
        self.node3.state = "locked"
        self.node4.state = "locked"
        self.node5.state = "locked"
        self.node6.state = "locked"
        self.node7.state = "locked"
        self.node8.state = "locked"


pygame.init()
screen = pygame.display.set_mode((1600, 900))
clock = pygame.time.Clock()

# Node class definition with unlocked connections from earlier
class Node:
    def __init__(self, x, y, radius, state="locked", screen_type=None):
        self.x = x 
        self.y = y
        self.radius = radius
        self.state = state
        self.connected_nodes = []  # Nodes connected to this node
        self.screen_type = screen_type  # The screen type this node will transition to (e.g., 'battle', 'shop')

    def draw(self, screen):
        # Define colors for each state
        color = {
            "available": (0, 255, 0),  # Green: Available
            "completed": (0, 0, 255),  # Blue: Completed
            "locked": (100, 100, 100)  # Gray: Locked
        }[self.state]
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)

    def is_hovered(self, mouse_pos):
        # Check if mouse is hovering over the node
        return (self.x - mouse_pos[0])**2 + (self.y - mouse_pos[1])**2 <= self.radius**2

    def unlock_connections(self):
        # Unlock all connected nodes that are locked
        for node in self.connected_nodes:
            if node.state == "locked":
                node.state = "available"  # Unlock connected nodes

def draw_connection(screen, node1, node2):
    pygame.draw.line(screen, (255, 255, 255), (node1.x, node1.y), (node2.x, node2.y), 5)

def handle_mouse(nodes, event, current_screen):
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = event.pos
        for node in nodes:
            # Only allow selection if the node is in the "available" state
            if node.is_hovered(mouse_pos) and node.state == "available":
                node.state = "completed"
                node.unlock_connections()  # Unlock connected nodes
                return node.screen_type  # Return the type of screen to transition to
    return current_screen  # If no change, keep the current screen

# Button class to create and manage buttons (like 'Return to Map')
class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
        label = self.font.render(self.text, True, (0, 0, 0))
        screen.blit(label, (self.rect.x + 10, self.rect.y + 10))

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


def draw_map_screen(screen, nodes):
    screen.fill((0, 0, 0))

    # Draw connections between nodes
    for i in range(len(nodes)):
        for connected_node in nodes[i].connected_nodes:
            draw_connection(screen, nodes[i], connected_node)

    # Draw the nodes
    for node in nodes:
        node.draw(screen)


def draw_battle_screen(screen, return_button):
    screen.fill((100, 0, 0))
    font = pygame.font.Font(None, 74)
    text = font.render("Battle Screen!", True, (255, 255, 255))
    screen.blit(text, (200, 250))
    return_button.draw(screen)  # Draw the 'Return to Map' button


def draw_shop_screen(screen, return_button):
    screen.fill((0, 100, 0))
    font = pygame.font.Font(None, 74)
    text = font.render("Shop Screen!", True, (255, 255, 255))
    screen.blit(text, (200, 250))
    return_button.draw(screen)

def draw_boss_screen(screen, return_button):
    screen.fill((0, 0, 100))
    font = pygame.font.Font(None, 74)
    text = font.render("Boss Screen!", True, (255, 255, 255))
    screen.blit(text, (200, 250))
    return_button.draw(screen)

room = Map_Room()
map = Map_Menu()

def main_map():
    # Main loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if map.current_screen == "map":
            # Handle mouse clicks on the map screen
            map.current_screen = handle_mouse(map.nodes, event, map.current_screen)

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Handle 'Return to Map' button click
            mouse_pos = event.pos
            if map.return_button.is_clicked(mouse_pos) and map.current_screen in ["battle", "shop", "boss"]:
                map.current_screen = "map"

    # Draw the current screen
    if map.current_screen == "map":
        draw_map_screen(screen, map.nodes)

    elif map.current_screen == "battle":
        room.enter_battle = True  # Pass return_button here
        
    elif map.current_screen == "shop":
        room.enter_shop = True  # Pass return_button here

    elif map.current_screen == "boss":
        draw_boss_screen(screen, map.return_button)  # Pass return_button here

    pygame.display.flip()
    clock.tick(60)