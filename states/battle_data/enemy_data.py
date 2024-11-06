from states.managers.Sprite_Manager import *

mobs_list_type = ['skeleton', 'zombie', 'orc', 'goblin']
mobs_list_hp = {'skeleton': 30, 'zombie': 20, 'orc': 40 , 'goblin': 20}
mobs_list_offset = {'skeleton': (160,150), 'zombie': (180,180), 'orc': (100,100), 'goblin': (180,160)}


skeleton_idle_img = get_image('Assets/Monsters/4 direction monsters/Skeleton/Idle.png', 3)
zombie_idle_img = get_image('Assets/Monsters/4 direction monsters/Mushroom/Idle.png', 3)
orc_idle_img = get_image('Assets/Monsters/Golem_IdleB.png', 5)
goblin_idle_img = get_image('Assets/Monsters/4 direction monsters/Goblin/Idle.png', 3)