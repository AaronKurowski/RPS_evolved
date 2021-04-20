from player import Player
from human import Human
from ai import Ai


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = Human()

    def run_game(self):
        # have players select name and check if ai is needed
        self.opening_statement()
        self.player_one.select_name()
        self.player_two.select_name()
        self.battle()
        # check for start
        # battle best of ? rounds
        # display winner
        pass

    def battle(self):
        # TODO: have players choose gestures against each other
        self.player_one.pick_gesture()
        self.player_two.pick_gesture()
        self.decide_round_winner()

    def return_score(self, player):
        # TODO: Return given player score
        pass

    def ready_check(self):
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

    def compare_gestures(self, player_one_gesture, player_two_gesture):
        # this method will compare gestures and possibly
        # if i put the picked gestures in a list and compare the values
        # i can say whoever had the one that wins is the winner
        # if same then tie
        list_of_gestures = [player_one_gesture, player_two_gesture]
        if "Rock" in list_of_gestures and "Scissors" in list_of_gestures:
            index_of_winner = list_of_gestures.index("Rock")
            if index_of_winner == 0:
                print("Player 1 wins!")
                return self.player_one
            else:
                print("Player 2 wins!")
                return self.player_two
        elif "Scissors" in list_of_gestures and "Paper" in list_of_gestures:
            index_of_winner = list_of_gestures.index("Scissors")
            if index_of_winner == 0:
                print("Player 1 wins!")
                return self.player_one
            else:
                print("player 2 wins!")
                return self.player_two
        elif "Paper" in list_of_gestures and "Rock" in list_of_gestures:
            index_of_winner = list_of_gestures.index("Paper")
            if index_of_winner == 0:
                print("Player 1 wins!")
                return self.player_one
            else:
                print("player 2 wins!")
                return self.player_two
        elif "Rock" in list_of_gestures and "Lizard" in list_of_gestures:
            index_of_winner = list_of_gestures.index("Rock")
            if index_of_winner == 0:
                print("Player 1 wins!")
                return self.player_one
            else:
                print("player 2 wins!")
                return self.player_two
        elif "Lizard" in list_of_gestures and "Spock" in list_of_gestures:
            index_of_winner = list_of_gestures.index("Lizard")
            if index_of_winner == 0:
                print("Player 1 wins!")
                return self.player_one
            else:
                print("player 2 wins!")
                return self.player_two
        elif "Spock" in list_of_gestures and "Scissors" in list_of_gestures:
            index_of_winner = list_of_gestures.index("Spock")
            if index_of_winner == 0:
                print("Player 1 wins!")
                return self.player_one
            else:
                print("player 2 wins!")
                return self.player_two
        elif "Scissors" in list_of_gestures and "Lizard" in list_of_gestures:
            index_of_winner = list_of_gestures.index("Scissors")
            if index_of_winner == 0:
                print("Player 1 wins!")
                return self.player_one
            else:
                print("player 2 wins!")
                return self.player_two
        elif "Lizard" in list_of_gestures and "Paper" in list_of_gestures:
            index_of_winner = list_of_gestures.index("Lizard")
            if index_of_winner == 0:
                print("Player 1 wins!")
                return self.player_one
            else:
                print("player 2 wins!")
                return self.player_two
        elif "Paper" in list_of_gestures and "Spock" in list_of_gestures:
            index_of_winner = list_of_gestures.index("Paper")
            if index_of_winner == 0:
                print("Player 1 wins!")
                return self.player_one
            else:
                print("player 2 wins!")
                return self.player_two
        elif "Spock" in list_of_gestures and "Rock" in list_of_gestures:
            index_of_winner = list_of_gestures.index("Spock")
            if index_of_winner == 0:
                print("Player 1 wins!")
                return self.player_one
            else:
                print("player 2 wins!")
                return self.player_two
        else:
            print("It was a tie!")

        # elif "Scissors" in list_of_gestures and "Paper" in list_of_gestures:
        #     index_of_winner = list_of_gestures.index("Scissors")
        #     if index_of_winner == self.player_one.gesture:
        #         return player1
        #     else:
        #         return player2

    def decide_round_winner(self):
        winner = self.compare_gestures(self.player_one.chosen_gesture, self.player_two.chosen_gesture)
        if winner == self.player_one:
            self.player_one.give_point(winner)
            print(winner.name)
            print(f"{winner.name}'s score is: {winner.score}!")
        else:
            self.player_two.give_point()