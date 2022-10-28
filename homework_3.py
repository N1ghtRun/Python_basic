# 1. Напишіть код, який зформує строку, яка містить певну інформацію про символ за його номером у слові.
# Наприклад "The [номер символу] symbol in '[тут слово]' is '[символ з відповідним порядковим номером в слові]'".
# Слово та номер символу отримайте за допомогою input() або скористайтеся константою. Наприклад
# (слово - "Python" а номер символу 3) - "The 3 symbol in 'Python' is 't' ".
#
# 2. Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою). Напишіть код, який визначить
# кількість слів, в цих даних.
#
# 3. Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0,
# 'Lorem Ipsum']. Напишіть код, який сформує новий list (наприклад lst2), який би містив всі числові змінні
# (int, float), які є в lst1. Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.


# Завдання 1
print('\nЗавдання 1:')
# Отримуємо слово від користувача
while True:
    word = input('Введіть слово (можна використовувати тільки 1 слово написане літерами): ')
    if not word.isalpha():
        print('Помилка вводу, спробуйте ще раз')
        continue
    else:
        break

# Отримуємо номер символу
while True:
    symbol_number = input('Введіть номер символу (цифрами): ')
    if not symbol_number.isnumeric():
        print('Введені нечислові або нецілочисленні дані, або число з мінусом, спробуйте ще раз')
        continue
    elif int(symbol_number) > len(word):
        print('Номер перевищую довжину слова, спробуйте ще раз')
        continue
    elif symbol_number == '0':
        print('Нульового символу не існує, спробуйте ще раз')
    else:
        break

symbol_number = int(symbol_number)
result = f"The {symbol_number} symbol in '{word}' is '{word[symbol_number-1]}' "
print(result)


# Завдання 2
print('\nЗавдання 2:')
while True:
    words = input('Введіть строку зі слів (можна використовувати тільки слова написані літерами): ')
    if not words.replace(' ', '').isalpha():
        print('Ввод має складатися тільки зі слів')
        continue
    else:
        break

words_counter = words.count(' ')
print(f"Введена строка складається із '{words_counter+1}' слів")


# Завдання 3
print('\nЗавдання 3:')
sample_list = ['1', '2', 3, True, 'False', 5, 198.3, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum', 12.3, -99]
result_list = []
for number in sample_list:
    if type(number) is int or type(number) is float:
        result_list.append(number)

print('Старий список:', sample_list)
print('Новий список: ', result_list)


"""

3 questions (optional):
    - what is the result of this course for me
    Answer: Improvement of my programming skills
    
    - how I plane to use this result
    Answer: I will use the result to earn money from it, but I see other benefits of this course, such as being in the
    community, getting valuable experience from the teachers, brain training, deeper understanding of IT in general, 
    having a good time in the process etc
    
    - what I am ready to sacrifice for the result
    Answer: the most valuable thing that I have - my time. Also it's not a sacrifice in my opinion, more like an
    investment.

"""
