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

    def give_point(self, player):
        player.score += 1


    def opening_statement(self):
        # TODO: General opening lines to start the game
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock!"
              "\n\nHere are the rules:"
              "\n\nRock crushes Scissors"
              "\nScissors cuts Paper"
              "\nPaper covers Rock"
              "\nRock crushes Lizard"
              "\nLizard poisons Spock"
              "\nSpock smashes Scissors"
              "\nScissors decapitates Lizard"
              "\nLizard eats paper"
              "\nPaper disproves Spock"
              "\nSpock vaporizes Rock")