class Gesture:
    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two
        self.win_conditions = {
            # gesture: [what it beats]
            'rock': ['lizard', 'scissors'],
            'paper': ['rock', 'spock'],
            'scissors': ['paper', 'lizard'],
            'lizard': ['paper', 'spock'],
            'spock': ['rock', 'scissors']
        }

    def define_winner(self, player_one_gesture, player_two_gesture):
        for i in self.win_conditions:
            if player_one_gesture.lower() == i and player_two_gesture.lower() == i:
                print("\nDraw! Choose again!")
                return None
            elif player_one_gesture.lower() == i and player_two_gesture.lower() in self.win_conditions[i]:
                # prints gestures and the action
                print(f"{player_one_gesture.title()}"
                      f"{self.gesture_action(player_one_gesture.lower(), player_two_gesture.lower())}"
                      f"{player_two_gesture.title()}!")
                print(f"{self.player_one.name} wins this round!")
                return self.player_one
            elif player_one_gesture.lower() == i and player_two_gesture.lower() not in self.win_conditions[i]:
                # prints gestures and the action
                print(f"{player_two_gesture.title()}"
                      f"{self.gesture_action(player_one_gesture.lower(), player_two_gesture.lower())}"
                      f"{player_one_gesture.title()}!")
                print(f"{self.player_two.name} wins this round!")
                return self.player_two

    def gesture_action(self, player_one_gesture, player_two_gesture):
        list_of_gestures = [player_one_gesture, player_two_gesture]
        if 'rock' in list_of_gestures and 'scissors' in list_of_gestures:
            return " crushes "
        elif 'scissors' in list_of_gestures and 'paper' in list_of_gestures:
            return " cuts "
        elif 'paper' in list_of_gestures and 'rock' in list_of_gestures:
            return " covers "
        elif 'rock' in list_of_gestures and 'lizard' in list_of_gestures:
            return " crushes "
        elif 'lizard' in list_of_gestures and 'spock' in list_of_gestures:
            return " poisons "
        elif 'spock' in list_of_gestures and 'scissors' in list_of_gestures:
            return " smashes "
        elif 'scissors' in list_of_gestures and 'lizard' in list_of_gestures:
            return " decapitates "
        elif 'lizard' in list_of_gestures and 'paper' in list_of_gestures:
            return " eats "
        elif 'paper' in list_of_gestures and 'spock' in list_of_gestures:
            return " disproves "
        else:
            return " vaporizes "
