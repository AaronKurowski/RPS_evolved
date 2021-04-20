from player import Player
from human import Human
from ai import Ai


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = Ai()

    def run_game(self):
        # have players select name and check if ai is needed
        self.opening_statement()
        self.player_one.select_name()
        print(f"\n{self.player_two.name} prepares himself...")
        # check for start
        # battle best of ? rounds
        # display winner
        pass

    def player_turn(self):
        # TODO: display which players turn it is and execute
        pass

    def return_score(self, player):
        # TODO: Return given player score
        pass

    def display_winner(self):
        pass

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

    def compare_gestures(self):
        # this method will compare gestures and possibly
        # if i put the picked gestures in a list and compare the values
        # i can say whoever had the one that wins is the winner
        # if same then tie
        pass

    def decide_round_winner(self):
        # TODO: Decide who the winner is based on compare_gestures. Might not need this
        pass
