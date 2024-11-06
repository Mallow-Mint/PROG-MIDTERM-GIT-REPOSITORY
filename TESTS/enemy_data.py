from Sprite_Manager import *

mobs_list_type = ['skeleton', 'zombie', 'orc', 'goblin']

mobs_list_sprites = {'skeleton': 'Assets/Monsters/4 direction monsters/Skeleton/Idle.png', 
                                'zombie': 'Assets/Monsters/4 direction monsters/Mushroom/Idle.png',
                                'orc': 'Assets/Monsters/Golem_IdleB.png' ,
                                'goblin': 'Assets/Monsters/4 direction monsters/Goblin/Idle.png'}
        
mobs_list_hp = {'skeleton': 15, 'zombie': 10, 'orc': 20 , 'goblin': 10}


skeleton_idle_img = get_image('Assets/Monsters/4 direction monsters/Skeleton/Idle.png', 3)
zombie_idle_img = get_image('Assets/Monsters/4 direction monsters/Mushroom/Idle.png', 3)
orc_idle_img = get_image('Assets/Monsters/Golem_IdleB.png', 5)
goblin_idle_img = get_image('Assets/Monsters/4 direction monsters/Goblin/Idle.png', 3)