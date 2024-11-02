import pygame

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
                print(f"Node at ({node.x}, {node.y}) selected!")
                node.state = "completed"  # Mark as completed
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


def main():
    pygame.init()
    screen = pygame.display.set_mode((1600, 900))
    clock = pygame.time.Clock()

    # Create the nodes with associated screen types
    node1 = Node(100, 300, 30, state="available", screen_type="battle")  # Starting node on map screen
    node2 = Node(250, 300, 30, state="locked", screen_type="shop")  # Battle screen node
    node3 = Node(400, 300, 30, state="locked", screen_type="battle")    # Shop screen node
    node4 = Node(550, 300, 30, state="locked", screen_type="shop")
    node5 = Node(700, 300, 30, state="locked", screen_type="battle")

    # Set up connections (which nodes unlock others)
    node1.connected_nodes = [node2]  # Clicking node1 unlocks node2 
    node2.connected_nodes = [node3]  # Clicking node2 unlocks node3
    node3.connected_nodes = [node4] 
    node4.connected_nodes = [node5] 


    nodes = [node1, node2, node3, node4, node5]

    # Initial screen state
    current_screen = "map"

    # Create the 'Return to Map' button
    return_button = Button(600, 500, 150, 50, "Return to Map")

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if current_screen == "map":
                # Handle mouse clicks on the map screen
                current_screen = handle_mouse(nodes, event, current_screen)

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Handle 'Return to Map' button click
                mouse_pos = event.pos
                if return_button.is_clicked(mouse_pos) and current_screen in ["battle", "shop"]:
                    current_screen = "map"

        # Draw the current screen
        if current_screen == "map":
            draw_map_screen(screen, nodes)
        elif current_screen == "battle":
            draw_battle_screen(screen, return_button)  # Pass return_button here
        elif current_screen == "shop":
            draw_shop_screen(screen, return_button)  # Pass return_button here

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

main()