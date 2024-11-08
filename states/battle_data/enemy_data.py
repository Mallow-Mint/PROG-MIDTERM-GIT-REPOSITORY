from states.managers.Sprite_Manager import *

mobs_list_type = ['skeleton', 'zombie', 'bat_eye', 'goblin']
mobs_list_hp = {'skeleton': 20, 'zombie': 15, 'bat_eye': 30 , 'goblin': 15}
mobs_list_offset = {'skeleton': (160,150), 'zombie': (180,160), 'bat_eye': (170,150), 'goblin': (180,160)}

#Idle_PNG's
skeleton_idle_img = get_image('Assets/Monsters/4 direction monsters/Skeleton/Idle.png', 3)
zombie_idle_img = get_image('Assets/Monsters/4 direction monsters/Mushroom/Idle.png', 3)
bat_eye_idle_img = get_image('Assets/Monsters/4 direction monsters/Flying eye/Flight.png', 3)
goblin_idle_img = get_image('Assets/Monsters/4 direction monsters/Goblin/Idle.png', 3)

#Attack_PNG's
skeleton_attack_img = get_image('Assets/Monsters/4 direction monsters/Skeleton/Attack.png', 3)
zombie_attack_img = get_image('Assets/Monsters/4 direction monsters/Mushroom/Attack.png', 3)
bat_eye_attack_img = get_image('Assets/Monsters/4 direction monsters/Flying eye/Attack.png', 3)
goblin_attack_img = get_image('Assets/Monsters/4 direction monsters/Goblin/Attack.png', 3)


#Hit_PNG's
skeleton_hit_img = get_image('Assets/Monsters/4 direction monsters/Skeleton/Take Hit.png', 3)
zombie_hit_img = get_image('Assets/Monsters/4 direction monsters/Mushroom/Take Hit.png', 3)
bat_eye_hit_img = get_image('Assets/Monsters/4 direction monsters/Flying eye/Take Hit.png', 3)
goblin_hit_img = get_image('Assets/Monsters/4 direction monsters/Goblin/Take Hit.png', 3)

def get_enemy_idle_sprite(enemy_type, layer):
    match enemy_type:
        case 'skeleton':
            current_enemy_sprite = General_Spritesheet(skeleton_idle_img, 600, 150, 4, 3, random.randint(100,175), layer)
        case 'zombie':
            current_enemy_sprite = General_Spritesheet(zombie_idle_img, 600, 150, 4, 3, random.randint(100,175), layer)
        case 'bat_eye':
            current_enemy_sprite = General_Spritesheet(bat_eye_idle_img, 1200, 150, 8, 3, random.randint(40,50), layer)
        case 'goblin':
            current_enemy_sprite = General_Spritesheet(goblin_idle_img, 600, 150, 4, 3, random.randint(100,175), layer)

    return current_enemy_sprite

def get_enemy_attack_sprite(enemy_type, layer):
    match enemy_type:
        case 'skeleton':
            current_enemy_attack_sprite = General_Spritesheet(skeleton_attack_img, 1200, 150, 8, 3, 80, layer)
        case 'zombie':
            current_enemy_attack_sprite = General_Spritesheet(zombie_attack_img, 1200, 150, 8, 3, 80, layer)
        case 'bat_eye':
            current_enemy_attack_sprite = General_Spritesheet(bat_eye_attack_img, 1200, 150, 8, 3, 80, layer)
        case 'goblin':
            current_enemy_attack_sprite = General_Spritesheet(goblin_attack_img, 1200, 150, 8, 3, 80, layer)

    return current_enemy_attack_sprite

def get_enemy_hit_sprite(enemy_type, layer):
    match enemy_type:
        case 'skeleton':
            current_enemy_hit_sprite = General_Spritesheet(skeleton_hit_img, 600, 150, 4, 3, 100, layer)
        case 'zombie':
            current_enemy_hit_sprite = General_Spritesheet(zombie_hit_img, 600, 150, 4, 3, 100, layer)
        case 'bat_eye':
            current_enemy_hit_sprite = General_Spritesheet(bat_eye_hit_img, 600, 150, 4, 3, 100, layer)
        case 'goblin':
            current_enemy_hit_sprite = General_Spritesheet(goblin_hit_img, 600, 150, 4, 3, 100, layer)

    return current_enemy_hit_sprite