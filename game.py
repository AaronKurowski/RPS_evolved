from player import Player
from human import Human
from ai import Ai


class Game:
    def __init__(self):
        self.define_contestants()
        # self.player_one = Human()
        # self.player_two = Human()
        self.number_of_rounds = 0

    def define_contestants(self):
        self.opening_statement()
        opponent = input("\nPress 1 to play against a Human or 2 to play against an AI"
                         "\n >")
        if opponent == '1':
            self.player_one = Human()
            self.player_two = Human()
        else:
            self.player_one = Human()
            self.player_two = Ai()

    def run_game(self):
        # have players select name and check if ai is needed

        self.player_one.select_name()
        self.player_two.select_name()
        self.battle()
        # check for start
        # battle best of ? rounds
        # display winner
        self.display_winner()

    def battle(self):
        # TODO: have players choose gestures against each other
        while self.player_one.score < 3 and self.player_two.score < 3:
            self.player_one.pick_gesture()
            self.player_two.pick_gesture()
            self.display_gestures(self.player_one, self.player_two)
            while self.player_one.chosen_gesture == self.player_two.chosen_gesture:
                print("\nDraw! Choose again!")
                self.number_of_rounds += 1
                self.player_one.pick_gesture()
                self.player_two.pick_gesture()
                self.display_gestures(self.player_one, self.player_two)
            self.decide_round_winner()
            self.number_of_rounds += 1
        # add function to display winner

    def return_score(self, player):
        # TODO: Return given player score
        pass

    def ready_check(self):
        pass

    def display_winner(self):
        if self.player_one.score > self.player_two.score:
            print("\n*************************************")
            print(f"{self.player_one.name} wins in {self.number_of_rounds} rounds!"
                  f"\nBetter luck next time {self.player_two.name}")
            print("*************************************")
        else:
            print("\n*************************************")
            print(f"\n\n{self.player_two.name} wins in {self.number_of_rounds} rounds!"
                  f"\nBetter luck next time {self.player_one.name}")
            print("*************************************")

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
                print("Rock crushes Scissors!")
                print(f"{self.player_one.name} wins this round!")
                return self.player_one
            else:
                print("Rock crushes Scissors!")
                print(f"{self.player_two.name} wins this round!")
                return self.player_two
        elif "Scissors" in list_of_gestures and "Paper" in list_of_gestures:
            index_of_winner = list_of_gestures.index("Scissors")
            if index_of_winner == 0:
                print("Scissors cuts Paper!")
                print(f"{self.player_one.name} wins this round!")
                return self.player_one
            else:
                print("Scissors cuts Paper!")
                print(f"{self.player_two.name} wins this round!")
                return self.player_two
        elif "Paper" in list_of_gestures and "Rock" in list_of_gestures:
            index_of_winner = list_of_gestures.index("Paper")
            if index_of_winner == 0:
                print("Paper covers Rock!")
                print(f"{self.player_one.name} wins this round!")
                return self.player_one
            else:
                print("Paper covers Rock!")
                print(f"{self.player_two.name} wins this round!")
                return self.player_two
        elif "Rock" in list_of_gestures and "Lizard" in list_of_gestures:
            index_of_winner = list_of_gestures.index("Rock")
            if index_of_winner == 0:
                print("Rock crushes Lizard!")
                print(f"{self.player_one.name} wins this round!")
                return self.player_one
            else:
                print("Rock crushes Lizard!")
                print(f"{self.player_two.name} wins this round!")
                return self.player_two
        elif "Lizard" in list_of_gestures and "Spock" in list_of_gestures:
            index_of_winner = list_of_gestures.index("Lizard")
            if index_of_winner == 0:
                print("Lizard poisons Spock!")
                print(f"{self.player_one.name} wins this round!")
                return self.player_one
            else:
                print("Lizard poisons Spock!")
                print(f"{self.player_two.name} wins this round!")
                return self.player_two
        elif "Spock" in list_of_gestures and "Scissors" in list_of_gestures:
            index_of_winner = list_of_gestures.index("Spock")
            if index_of_winner == 0:
                print("Spock smashes Scissors!")
                print(f"{self.player_one.name} wins this round!")
                return self.player_one
            else:
                print("Spock smashes Scissors!")
                print(f"{self.player_two.name} wins this round!")
                return self.player_two
        elif "Scissors" in list_of_gestures and "Lizard" in list_of_gestures:
            index_of_winner = list_of_gestures.index("Scissors")
            if index_of_winner == 0:
                print("Scissors decapitates Lizard!")
                print(f"{self.player_one.name} wins this round!")
                return self.player_one
            else:
                print("Scissors decapitates Lizard!")
                print(f"{self.player_two.name} wins this round!")
                return self.player_two
        elif "Lizard" in list_of_gestures and "Paper" in list_of_gestures:
            index_of_winner = list_of_gestures.index("Lizard")
            if index_of_winner == 0:
                print("Lizard eats Paper!")
                print(f"{self.player_one.name} wins this round!")
                return self.player_one
            else:
                print("Lizard eats Paper!")
                print(f"{self.player_two.name} wins this round!")
                return self.player_two
        elif "Paper" in list_of_gestures and "Spock" in list_of_gestures:
            index_of_winner = list_of_gestures.index("Paper")
            if index_of_winner == 0:
                print("Paper disproves Spock!")
                print(f"{self.player_one.name} wins this round!")
                return self.player_one
            else:
                print("Paper disproves Spock!")
                print(f"{self.player_two.name} wins this round!")
                return self.player_two
        elif "Spock" in list_of_gestures and "Rock" in list_of_gestures:
            index_of_winner = list_of_gestures.index("Spock")
            if index_of_winner == 0:
                print("Spock vaporizes Rock!")
                print(f"{self.player_one.name} wins this round!")
                return self.player_one
            else:
                print("Spock vaporizes Rock!")
                print(f"{self.player_two.name} wins this round!")
                return self.player_two
        else:
            print("It was a tie!")
            return None
            # self.player_one.pick_gesture()
            # self.player_two.pick_gesture()
            # self.decide_round_winner()

    def decide_round_winner(self):
        winner = self.compare_gestures(self.player_one.chosen_gesture, self.player_two.chosen_gesture)
        winner.score += 1
        print(f"{winner.name}'s score is: {winner.score}")

    def display_gestures(self, player1, player2):
        print(f"\n{player1.name} chooses {player1.chosen_gesture}!")
        print(f"{player2.name} chooses {player2.chosen_gesture}!")
        print("--------------------------------------------------")
