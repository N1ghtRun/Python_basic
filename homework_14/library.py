from random import choice
from os import stat


class GameFigure:
    """
    Args:
         value (str): Figure
    """

    value = None

    rules = {
        'Rock': ('Scissors', 'Lizard'),
        'Scissors': ('Paper', 'Lizard'),
        'Paper': ('Rock', 'Spock'),
        'Lizard': ('Spock', 'Paper'),
        'Spock': ('Scissors', 'Rock'),
    }

    def get_player_figure(self):
        while True:
            self.value = input("\nEnter the figure. You can choose Rock, Scissors, Paper, Lizard or Spock: ")
            self.value = self.value.capitalize()
            if self.value in self.rules.keys():
                break
            else:
                print("Wrong input\n")

    def get_ai_figure(self):
        self.value = choice(list(self.rules.keys()))


class Statistics:

    def __init__(self, player_figure, ai_figure, winner):
        self.player_figure = player_figure.value
        self.ai_figure = ai_figure.value
        self.winner = winner

    def write_statistics(self):
        # counter will help to collect statistics
        with open("counter.txt", "r") as file:
            # check if the file is not empty
            if stat("counter.txt").st_size != 0:
                counter = int(file.readline()) + 1
            else:
                counter = 1

        with open("counter.txt", "w") as file:
            file.write(str(counter))

        with open("statistics.txt", "a") as file:
            data = f"Game number: {counter}\n" \
                   f"Player's figure: {self.player_figure}\n" \
                   f"AI figure: {self.ai_figure}\n" \
                   f"{self.winner}\n\n"
            file.write(data)


class Game:
    """
    Args:
         player_figure (GameFigure): Player's figure
         ai_figure (GameFigure): AI's figure
    """
    def __init__(self, player_figure, ai_figure):
        self.player_figure = player_figure
        self.AI_figure = ai_figure
        self.winner = ''

    def define_winner(self):
        if self.player_figure.value == self.AI_figure.value:
            winner = 'Draw'
        elif self.AI_figure.value in GameFigure.rules[self.player_figure.value]:
            winner = 'Winner: You!'
        else:
            winner = 'Winner: AI'

        return winner

    def text_msg(self):
        print(f"\nYour figure: {self.player_figure.value}\nAI figure: {self.AI_figure.value}\n{self.winner}")

    @staticmethod
    def rematch_check():
        while True:
            rematch = input("\nPlay again? (y/n): ")
            rematch = rematch.lower()
            if rematch == 'y':
                return True
            elif rematch == 'n':
                return False
            else:
                print("Wrong input")

    def game(self):
        while True:
            self.player_figure.get_player_figure()
            self.AI_figure.get_ai_figure()

            self.winner = self.define_winner()
            self.text_msg()
            statistics = Statistics(self.player_figure, self.AI_figure, self.winner)
            statistics.write_statistics()
            if not self.rematch_check():
                print("Thanks for playing.")
                break
