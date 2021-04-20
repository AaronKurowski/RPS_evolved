from random import *


class Player:
    def __init__(self):
        self.name = ""
        self.score = 0
        self.chosen_gesture = ""
        self.gesture = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

    def pick_gesture(self):
        # prints the options the user can pick and stores their input
        print("\n")
        print("  ||  ".join(self.gesture))
        self.chosen_gesture = input("^^ Choose from the list above! ^^"
                                    "\n>")

    def select_name(self):
        self.name = input("\nWhat's your name? >")
        print("Hello " + self.name + "!")

    def modify_score(self):
        # if player win: += 1
        # if player lose: += 0
        pass
