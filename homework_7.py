# Напишіть гру "rock scissors paper lizard spock". Використайте розділення всієї програми на функції
# (Single-Responsibility principle). Як скелет-заготовку можна використати приклад з заняття.
# До кожної функції напишіть докстрінг або анотацію


from random import choice


print("\nGame of rock, scissors, paper, lizard, spock")

rules = {
    'Rock': ('Scissors', 'Lizard'),
    'Scissors': ('Paper', 'Lizard'),
    'Paper': ('Rock', 'Spock'),
    'Lizard': ('Spock', 'Paper'),
    'Spock': ('Scissors', 'Rock'),
}


def get_player_figure():
    """
    Returns:
        figure (str): Returns player's figure
    """
    while True:
        figure = input("\nEnter the figure. You can choose Rock, Scissors, Paper, Lizard or Spock: ")
        figure = figure.capitalize()
        if figure in rules.keys():
            return figure
        else:
            print("Wrong input\n")


def get_ai_figure():
    """
    Returns:
        figure (str): Return's AI's figure
    """
    figure = choice(list(rules.keys()))

    return figure


def define_winner(player_figure, ai_figure):
    """
    Args:
        player_figure (str): Player's figure
        ai_figure (str): AI's figure

    Returns:
        winner (str): Returns a string which tells who have won
    """
    if player_figure == ai_figure:
        winner = 'Draw'
    elif ai_figure in rules[player_figure]:
        winner = 'Winner: You!'
    else:
        winner = 'Winner: AI'

    return winner


def text_msg(player_figure, ai_figure, winner):
    """
    Args:
         player_figure (str): Player's figure
         ai_figure (str): AI's figure
         winner (str): A string which tells who have won
    """
    print(f"\nYour figure: {player_figure}\nAI figure: {ai_figure}\n{winner}")


def game():
    """
    Main function
    """
    player_figure = get_player_figure()
    ai_figure = get_ai_figure()
    winner = define_winner(player_figure, ai_figure)
    text_msg(player_figure, ai_figure, winner)


def rematch_check():
    """
    Returns:
        (bool): Return will be used to determine if the game should continue
    """
    while True:
        rematch = input("\nPlay again? (y/n): ")
        rematch = rematch.lower()
        if rematch == 'y':
            return True
        elif rematch == 'n':
            return False
        else:
            print("Wrong input")


while True:
    game()
    if not rematch_check():
        print("Thanks for playing.")
        break
