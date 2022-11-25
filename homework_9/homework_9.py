# Напишіть декоратор, який вимірює і виводить на екран час виконання функції в секундах і задекоруйте ним основну
# функцію гри з попередньої дз. Після закінчення гри декоратор має сповістити, скільки тривала гра.


import library


print("\nGame of rock, scissors, paper, lizard, spock")

while True:
    library.game()
    if not library.rematch_check():
        print("Thanks for playing.")
        break
