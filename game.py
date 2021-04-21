import math
from human import Human
from ai import Ai


class Game:
    def __init__(self):
        self.define_contestants()
        self.number_of_rounds = 0

    def define_contestants(self):
        # prompts user to pick a human or ai opponent
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
        self.player_one.select_name()
        self.player_two.select_name()
        self.battle()
        self.display_winner()

    def battle(self):
        win_limit = self.best_of()
        while self.player_one.score < win_limit and self.player_two.score < win_limit:
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

    def best_of(self):
        # lets user pick best of however many rounds
        # chooses best of 3 if user chooses below 3
        while True:
            try:
                chosen_best_of = input("\nBest of how many rounds? Minimum = 3"
                                       "\n>")
                chosen_best_of = int(chosen_best_of)
            except ValueError:
                print("\nMake sure you type a positive integer!")
                continue
            except TypeError:
                print("\nMake sure you type a positive integer!")
                continue
            else:
                if chosen_best_of >= 3 and chosen_best_of % 2 == 0:
                    return (chosen_best_of / 2) + 1

                elif chosen_best_of >= 3 and chosen_best_of % 2 == 1:
                    return math.ceil((chosen_best_of / 2))
                else:
                    return 3

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
            print(f"{self.player_two.name} wins in {self.number_of_rounds} rounds!"
                  f"\nBetter luck next time {self.player_one.name}")
            print("*************************************")

    def opening_statement(self):
        # General opening lines to start the game
        print("\nWelcome to Rock, Paper, Scissors, Lizard, Spock!"
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
        # adds gestures to a list and picks the user with winning gesture
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

    def decide_round_winner(self):
        winner = self.compare_gestures(self.player_one.chosen_gesture, self.player_two.chosen_gesture)
        winner.score += 1
        print("--------------------------------------------------")
        print(f"{winner.name}'s score is: {winner.score}")

    def display_gestures(self, player1, player2):
        print(f"\n{player1.name} chooses {player1.chosen_gesture}!")
        print(f"{player2.name} chooses {player2.chosen_gesture}!")
        print("--------------------------------------------------")
