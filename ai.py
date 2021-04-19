from player import Player


class Ai(Player):
    def __init__(self):
        self.name = "CPU"
        super().__init__()

    def pick_gesture(self):
        # TODO: This will overwrite method from player class for ai capabilities
        pass
