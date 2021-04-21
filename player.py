class Player:
    def __init__(self):
        self.name = ""
        self.score = 0
        self.chosen_gesture = ""
        self.gesture = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

    def pick_gesture(self, name):
        # prints the options the user can pick and stores their input
        while True:
            print("\n")
            print("  ||  ".join(self.gesture))
            self.chosen_gesture = input(f"^^ {name}! Type an option from the list above! ^^"
                                        "\n>").title()
            if self.chosen_gesture not in self.gesture:
                print("\nThat is not an option. Try retyping!")
                continue
            else:
                break

    def select_name(self):
        self.name = input("\nWelcome player, what is your name? >")
        print("Hello " + self.name + "!")
