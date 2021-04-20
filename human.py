from player import Player


class Human(Player):
    def __init__(self):
        super().__init__()

    def select_name(self):
        self.name = input("\nWhat's your name? >")
        print("Hello " + self.name + "!")