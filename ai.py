from player import Player
from random import *


class Ai(Player):
    def __init__(self):
        self.random = Random()
        super().__init__()
        self.npc = ["Jarvis", "Hal", "Stiffler", "Billy Binks", "Scooter", "Yoder"]

    def pick_gesture(self, name):
        # randomly selects gesture
        random_index = self.random.randint(0, 4)
        self.chosen_gesture = self.gesture[random_index]

    def select_name(self):
        # randomly selects name
        random_index = self.random.randint(0, 2)
        self.name = self.npc[random_index]
        print("\n" + self.name + " the NPC is ready to play!")
