from states.managers.Sprite_Manager import *

mobs_list_type = ['skeleton', 'zombie', 'bat_eye', 'goblin']
mobs_list_hp = {'skeleton': 30, 'zombie': 20, 'bat_eye': 40 , 'goblin': 20}
mobs_list_offset = {'skeleton': (160,150), 'zombie': (180,180), 'bat_eye': (170,150), 'goblin': (180,160)}

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