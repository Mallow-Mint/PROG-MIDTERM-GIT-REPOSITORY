import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 1600, 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Character Animation Demo")

# Set a clock for controlling the frame rate
clock = pygame.time.Clock()

def load_sprites():
    try:
        # Create a dictionary to hold the sprite animations
        sprite_animations = {
            "idle": [
                pygame.image.load('Assets/Medieval_Characters/Medieval_Characters_For_Demo/Medieval_Normal_King/normal_king_idle_1.png').convert_alpha(),
                pygame.image.load('Assets/Medieval_Characters/Medieval_Characters_For_Demo/Medieval_Normal_King/normal_king_idle_2.png').convert_alpha(),
                pygame.image.load('Assets/Medieval_Characters/Medieval_Characters_For_Demo/Medieval_Normal_King/normal_king_idle_3.png').convert_alpha()
            ],
            "attack_1": [
                pygame.image.load('Assets/Medieval_Characters/Medieval_Characters_For_Demo/Medieval_Normal_King/normal_king_normal_attack_2.png.').convert_alpha(),
                pygame.image.load('Assets/Medieval_Characters/Medieval_Characters_For_Demo/Medieval_Normal_King/normal_king_normal_attack_3.png').convert_alpha(),
                pygame.image.load('Assets/Medieval_Characters/Medieval_Characters_For_Demo/Medieval_Normal_King/normal_king_normal_attack_4.png').convert_alpha(),
                pygame.image.load('Assets/Medieval_Characters/Medieval_Characters_For_Demo/Medieval_Normal_King/normal_king_normal_attack_5.png').convert_alpha()
            ],
            "attack_2": [
                pygame.image.load('Assets/Medieval_Characters/Medieval_Characters_For_Demo/Medieval_Normal_King/normal_king_special_attack_2.png.').convert_alpha(),
                pygame.image.load('Assets/Medieval_Characters/Medieval_Characters_For_Demo/Medieval_Normal_King/normal_king_special_attack_3.png.').convert_alpha(),
                pygame.image.load('Assets/Medieval_Characters/Medieval_Characters_For_Demo/Medieval_Normal_King/normal_king_special_attack_4.png.').convert_alpha(),
                pygame.image.load('Assets/Medieval_Characters/Medieval_Characters_For_Demo/Medieval_Normal_King/normal_king_special_attack_5.png.').convert_alpha()
            ],
            "hit": [
                pygame.image.load('Assets/Medieval_Characters/Medieval_Characters_For_Demo/Medieval_Normal_King/normal_king_hit_1.png').convert_alpha(),
                pygame.image.load('Assets/Medieval_Characters/Medieval_Characters_For_Demo/Medieval_Normal_King/normal_king_hit_2.png').convert_alpha(),
                pygame.image.load('Assets/Medieval_Characters/Medieval_Characters_For_Demo/Medieval_Normal_King/normal_king_hit_3.png').convert_alpha()
            ],
            "death": [
                
                pygame.image.load('Assets/Medieval_Characters/Medieval_Characters_For_Demo/Medieval_Normal_King/normal_king_death_1.png').convert_alpha(),
                pygame.image.load('Assets/Medieval_Characters/Medieval_Characters_For_Demo/Medieval_Normal_King/normal_king_death_2.png').convert_alpha(),
                pygame.image.load('Assets/Medieval_Characters/Medieval_Characters_For_Demo/Medieval_Normal_King/normal_king_death_3.png').convert_alpha(),
                pygame.image.load('Assets/Medieval_Characters/Medieval_Characters_For_Demo/Medieval_Normal_King/normal_king_death_4.png').convert_alpha(),
                pygame.image.load('Assets/Medieval_Characters/Medieval_Characters_For_Demo/Medieval_Normal_King/normal_king_death_5.png').convert_alpha(),
                pygame.image.load('Assets/Medieval_Characters/Medieval_Characters_For_Demo/Medieval_Normal_King/normal_king_death_6.png').convert_alpha(),
                pygame.image.load('Assets/Medieval_Characters/Medieval_Characters_For_Demo/Medieval_Normal_King/normal_king_death_7.png').convert_alpha(),
                pygame.image.load('Assets/Medieval_Characters/Medieval_Characters_For_Demo/Medieval_Normal_King/normal_king_death_8.png').convert_alpha(),
                pygame.image.load('Assets/Medieval_Characters/Medieval_Characters_For_Demo/Medieval_Normal_King/normal_king_death_9.png').convert_alpha(),
                pygame.image.load('Assets/Medieval_Characters/Medieval_Characters_For_Demo/Medieval_Normal_King/normal_king_death_10.png').convert_alpha(),
                pygame.image.load('Assets/Medieval_Characters/Medieval_Characters_For_Demo/Medieval_Normal_King/normal_king_death_11.png').convert_alpha(),
            ],
        }
    except pygame.error as e:
        print(f"Error loading images: {e}")
        sys.exit()
    
    return sprite_animations

sprite_animations = load_sprites()  # Load the sprite animations

class Character:
    def __init__(self, name, hp, sprite_animations, element_weakness=None):
        #HP hp bar
        #spawn randomizer
        #attack count
        #level?
        self.name = name
        self.max_hp = hp
        self.current_hp = hp
        self.sprite_animations = sprite_animations
        self.current_animation = "idle"
        self.current_frame = 0
        self.frame_duration = 100  # Milliseconds per frame
        self.last_frame_time = pygame.time.get_ticks()
        self.sprite_rect = self.sprite_animations["idle"][0].get_rect(center=(screen_width // 2, screen_height // 2))
        self.attack_pattern_count = 2  # Number of attack patterns
        self.damage_ranges = {
            "attack_1": (5, 10),
            "attack_2": (10, 15),
        }
        self.element_weakness = element_weakness  # Elemental weakness (if any)

    def update_animation(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_frame_time > self.frame_duration:
            self.current_frame = (self.current_frame + 1) % len(self.sprite_animations[self.current_animation])
            self.last_frame_time = current_time

    def change_animation(self, animation):
        if animation in self.sprite_animations:
            self.current_animation = animation
            self.current_frame = 0

    def draw(self, screen):
        sprite = self.sprite_animations[self.current_animation][self.current_frame]
        screen.blit(sprite, self.sprite_rect)
        self.draw_hp_bar(screen)

    def draw_hp_bar(self, screen):
        bar_width = 100
        bar_height = 10
        fill_width = int(bar_width * (self.current_hp / self.max_hp))
        outline_rect = pygame.Rect(self.sprite_rect.x, self.sprite_rect.y - 20, bar_width, bar_height)
        fill_rect = pygame.Rect(self.sprite_rect.x, self.sprite_rect.y - 20, fill_width, bar_height)
        pygame.draw.rect(screen, (255, 0, 0), fill_rect)  # Red fill (HP)
        pygame.draw.rect(screen, (255, 255, 255), outline_rect, 2)  # White border

    def take_damage(self, damage, element=None):
        if element == self.element_weakness:
            damage *= 1.5
        self.current_hp -= damage
        self.current_hp = max(self.current_hp, 0)
        if self.current_hp > 0:
            self.current_animation = "hit"
        else:
            self.current_animation = "death"

    def attack(self):
        attack_index = random.randint(1, self.attack_pattern_count)
        attack_key = f"attack_{attack_index}"
        damage_range = self.damage_ranges.get(attack_key, (0, 0))
        damage = random.randint(*damage_range)
        self.current_animation = attack_key
        return attack_key, damage

    def is_alive(self):
        return self.current_hp > 0

player = Character(name="Medieval_Normal_King", hp=100, sprite_animations=sprite_animations)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Detect key presses for numbers 1 to 6 to trigger animations
    keys = pygame.key.get_pressed()

    if keys[pygame.K_1]:
        player.change_animation("idle")
    elif keys[pygame.K_2]:
        player.change_animation("attack_1")
    elif keys[pygame.K_3]:
        player.change_animation("attack_2")
    elif keys[pygame.K_4]:
        player.change_animation("attack_3")
    elif keys[pygame.K_5]:
        player.change_animation("hit")
    elif keys[pygame.K_6]:
        player.change_animation("death")

    # Update character animation
    player.update_animation()

    # Draw everything
    screen.fill((0, 0, 0))  # Fill screen with black
    player.draw(screen)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)
