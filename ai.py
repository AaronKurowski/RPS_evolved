from player import Player
from random import *


class Ai(Player):
    def __init__(self):
        self.name = "CPU"
        self.random = Random()
        super().__init__()

    def pick_gesture(self):
        # TODO: This will overwrite method from player class for ai capabilities
        # i want to search the gesture list and pull a random
        random_index = self.random.randint(0, 4)
        print(random_index)
        self.chosen_gesture = self.gesture[random_index]
        print(self.chosen_gesture)
