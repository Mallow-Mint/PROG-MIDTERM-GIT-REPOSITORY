from states.managers.Sprite_Manager import *

class Spell_Dict:
    def __init__(self):
        self.single_target_words_damage = { 'acid': 4,
                                            'air': 2,
                                            'airslice': 8,
                                            'arrow': 4,
                                            'ashes': 4,
                                            'axe': 2,
                                            'bane': 4,
                                            'bash': 3,
                                            'blight': 5,
                                            'bolt': 4,
                                            'burn': 4,
                                            'crusade': 6,
                                            'curse': 5,
                                            'dark': 3,
                                            'drown': 5,
                                            'destroy': 7,
                                            'earth': 5,
                                            'execute': 7,
                                            'exile': 5,
                                            'fire': 4,
                                            'firebolt': 7,
                                            'freeze': 7,
                                            'gale': 4,
                                            'hail': 4,
                                            'heat': 4,
                                            'hot': 4,
                                            'howl': 4,
                                            'ice': 2,
                                            'icewall': 6,
                                            'kick': 4,
                                            'lava': 4,
                                            'light': 4,
                                            'lightbeam': 8,
                                            'magma': 5,
                                            'punch': 4,
                                            'rumble': 6,
                                            'scorch': 5,
                                            'smite': 5,
                                            'snare': 5,
                                            'snowball': 7,
                                            'strike': 6,
                                            'suffocate': 7,
                                            'thunder': 7,
                                            'torpedo': 7,
                                            'umbral': 6,
                                            'wind': 4,
                                            'water': 5,
                                            'wet': 3,
                                            'wind': 4,
                                            'windslash': 8,
                                            'zap': 4}
        
        self.life_steal_damage = {'bite': 4,
                                  'necromancy': 8}
        
        self.multi_target_word_damage = {   'airstrike': 5,
                                            'avalanche': 4,
                                            'earthquake': 5,
                                            'eruption': 4,
                                            'explosion': 4,
                                            'fireball': 4,
                                            'firestorm': 4,
                                            'flamethrower': 6,
                                            'frostnova': 4,
                                            'heatwave': 4,
                                            'iceprison': 4,
                                            'judgement': 4,
                                            'landfall': 4,
                                            'landslide': 4,
                                            'lightning': 4,
                                            'obliterate': 5,
                                            'quasar': 3,
                                            'rain': 2,
                                            'rainstorm': 4,
                                            'thunderbolt': 5,
                                            'thunderclap': 5,
                                            'thunderstorm': 6,
                                            'tornado': 3,
                                            'tsunami': 3,
                                            'sandstorm': 4,
                                            'squall': 3,
                                            'sunbeam': 3,
                                            'stonesplitter': 6,
                                            'volcano': 3,
                                            'waterspout': 5,
                                            'waterstorm': 5,
                                            'whirlpool': 4,
                                            'whirlwind': 4,
                                            'zephyr': 3 }
        
        self.healing_spell_ranges = {'bless': [8,12],
                                     'heal': [4,8],
                                     'purify': [8,12],
                                     'recover': [13,20]}

class Spell_Animations:
    def __init__(self):
        pass

    def get_spell_sprite_sheet(self, spell, display):
        '''
        COLOR CODE
        0 = Orange
        1 = Purple
        2 = Light Blue
        3 = Green
        4 = Brown
        5 = White
        6 = Light Purple
        7 = Red
        8 = Dark Blue
        '''
        match spell:
            case 'explosion':
                spell_image = get_image('Assets/Attack Effects/Free/Part 14/672.png', 6)
                self.current_spell_animation  = Spell_Spritesheet(spell_image, 896, 576, 14, 9, 6, 100, display)
                self.current_spell_color = 0
            case 'fire':
                spell_image = get_image('Assets/Attack Effects/Free/Part 14/663.png', 5)
                self.current_spell_animation  = Spell_Spritesheet(spell_image, 1024, 576, 16, 9, 5, 100, display)
                self.current_spell_color = 0
            case 'quasar':
                spell_image = get_image('Assets/Attack Effects/Free/Part 15/720.png', 6)
                self.current_spell_animation  = Spell_Spritesheet(spell_image, 1280, 576, 20, 9, 6, 100, display)
                self.current_spell_color = 1
        return self.current_spell_animation

spell_animations = Spell_Animations()
spell_dict = Spell_Dict()