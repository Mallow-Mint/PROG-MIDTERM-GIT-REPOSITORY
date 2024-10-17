import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set a clock for controlling the frame rate
clock = pygame.time.Clock()


class Character:
    def __init__(self, name, hp, element_weakness, sprite_animations):
        #self attackcount (checks the characters attacks available)
        #self strength = computation for max hp
        #self agility = evasion or miss
        #self immunity = strong against certain elements or physical attacks()
        #self armor = extra hp but might need to make an armor bar
        self.name = name
        self.max_hp = hp
        self.current_hp = hp
        self.element_weakness = element_weakness
        self.sprite_animations = sprite_animations  # Dictionary of all animations (idle, run, attack, etc.)
        self.current_animation = "idle"  # Default animation is idle
        self.current_frame = 0
        self.frame_duration = 100  # Milliseconds per frame
        self.last_frame_time = pygame.time.get_ticks()
        self.sprite_rect = self.sprite_animations["idle"][0].get_rect()
        self.attack_pattern_count = len(sprite_animations["attack"])  # Number of attack patterns
        self.damage_ranges = {
            "attack_1": (5, 10),  # Attack 1 does 5-10 damage
            "attack_2": (10, 15),  # Attack 2 does 10-15 damage
            "attack_3": (15, 20),  # Attack 3 does 15-20 damage
        }
        
    def update_animation(self):
        # Update frame based on current animation
        current_time = pygame.time.get_ticks()
        if current_time - self.last_frame_time > self.frame_duration:
            self.current_frame = (self.current_frame + 1) % len(self.sprite_animations[self.current_animation])
            self.last_frame_time = current_time
    
    def draw(self, screen):
        # Draw the current frame of the current animation
        sprite = self.sprite_animations[self.current_animation][self.current_frame]
        screen.blit(sprite, self.sprite_rect)
        self.draw_hp_bar(screen)

    def draw_hp_bar(self, screen):
        # Draw the HP bar above the character
        bar_width = 100
        bar_height = 10
        fill_width = int(bar_width * (self.current_hp / self.max_hp))
        outline_rect = pygame.Rect(self.sprite_rect.x, self.sprite_rect.y - 20, bar_width, bar_height)
        fill_rect = pygame.Rect(self.sprite_rect.x, self.sprite_rect.y - 20, fill_width, bar_height)
        pygame.draw.rect(screen, (255, 0, 0), fill_rect)  # Red fill (HP)
        pygame.draw.rect(screen, (255, 255, 255), outline_rect, 2)  # White border
    
    def take_damage(self, damage, element=None):
        # Apply damage to the character, factoring in elemental weakness
        if element == self.element_weakness:
            damage *= 1.5  # Take 50% extra damage from weak element
        self.current_hp -= damage
        self.current_hp = max(self.current_hp, 0)  # HP cannot go below 0
        if self.current_hp > 0:
            self.current_animation = "hit"
        else:
            self.current_animation = "death"
    
    def attack(self):
        # Randomly choose an attack pattern (up to 3 attacks)
        if self.attack_pattern_count > 0:
            attack_index = random.randint(1, self.attack_pattern_count)
            attack_key = f"attack_{attack_index}"
            damage_range = self.damage_ranges.get(attack_key, (0, 0))
            damage = random.randint(*damage_range)
            self.current_animation = attack_key
            return attack_key, damage
        else:
            return None, 0

    def is_alive(self):
        return self.current_hp > 0


# Example usage

# Load example animations (you'll need to load your actual images)
# This is a dictionary where each key corresponds to an animation type
sprite_animations = {
    "idle": [pygame.image.load('idle_1.png'), pygame.image.load('idle_2.png')],
    "run": [pygame.image.load('run_1.png'), pygame.image.load('run_2.png')],
    "attack_1": [pygame.image.load('attack1_1.png'), pygame.image.load('attack1_2.png')],
    "attack_2": [pygame.image.load('attack2_1.png'), pygame.image.load('attack2_2.png')],
    "attack_3": [pygame.image.load('attack3_1.png'), pygame.image.load('attack3_2.png')],
    "hit": [pygame.image.load('hit_1.png'), pygame.image.load('hit_2.png')],
    "death": [pygame.image.load('death_1.png'), pygame.image.load('death_2.png')],
}

# Create a character
player = Character(name="Hero", hp=100, element_weakness="fire", sprite_animations=sprite_animations)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update character animation
    player.update_animation()

    # Draw everything
    screen.fill((0, 0, 0))  # Fill screen with black
    player.draw(screen)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)
