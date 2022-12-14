#  Візьміть свою гру з HW8 і перепишіть ії в обʼєктному стилі. Зробіть максимум взаємодії (як явної так і неявної) на
#  рівні обʼєктів. Рекомендую подумати над такими класами як Player, GameFigure, Game. Памʼятайте про чистоту і простоту
#  коду (DRY, KISS), коментарі та докстрінги.


import library

# creating figure object for the player
player_figure = library.GameFigure()
# creating figure object for the AI
AI_figure = library.GameFigure()


game = library.Game(player_figure, AI_figure)
game.game()
