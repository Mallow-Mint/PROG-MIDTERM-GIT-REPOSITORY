class State():
    def __init__(self, game):
        self.game = game
        self.previous_state = None
    
    def update(self, delta_time):
        pass

    def render(self, surface):
        pass

    def enter_state(self):
        if len (self.game.STATE_STACK) > 1:
            self.previous_state = self.game.STATE_STACK[-1]
        self.game.STATE_STACK.append(self)
    
    def exit_state(self):
        self.game.STATE_STACK.pop()