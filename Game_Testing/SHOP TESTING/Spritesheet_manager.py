import pygame
import time

PURPLE = (255, 0 , 255)
run = True
clock = pygame.time.Clock()
animations_cooldown = 100
potion_layer_test = pygame.Surface((1600, 900))


def get_image(img, scale):
    image = pygame.image.load(img)
    image = pygame.transform.scale_by(image, scale)
    return image

class Spritesheet():
    def __init__(self, image, width, height, frame_count, scale):
        self.sheet = image
        self.width = width
        self.height = height
        self.scale = scale
        self.frames = frame_count
        self.frame_1 = 0
        self.current_time_1 = 0
        self.last_update_1 = pygame.time.get_ticks()

    def get_potion_frames(self):
        scaled_width = self.width * self.scale
        scaled_height = self.height * self.scale
        self.potion_1_frame_coordinates = []
        for frame in range(self.frames):
            current_frame = (scaled_width * frame, 0, scaled_width, scaled_height)
            self.potion_1_frame_coordinates.append(current_frame)
    
    def get_single_frame(self):
        potion_layer_test.blit(self.sheet, (0,0), self.potion_1_frame_coordinates[self.frame_1])

    def get_potion_sprites_1(self):
        if self.current_time_1 - self.last_update_1 >= animations_cooldown:
            self.frame_1 += 1
            self.last_update_1 = self.current_time_1
            if self.frame_1 >= self.frames:
                self.frame_1 = 0
    
    def display_potion(self):
        self.current_time_1 = pygame.time.get_ticks()
        self.get_potion_sprites_1()
        self.get_single_frame()
