# Напишіть программу "Касир в кінотеватрі", яка буде виконувати наступне:
# Попросіть користувача ввести свсвій вік (можно використати константу або input()).
# - якщо користувачу менше 7 - вивести повідомлення "Де твої батьки?"
# - якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
# - якщо користувачу більше 65 - вивести повідомлення "Покажіть пенсійне посвідчення!"
# - якщо вік користувача з двох однакових цифр - вивести повідомлення "Як цікаво!"
# - у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!"
# P.S. На екран має бути виведено лише одне повідомлення, якщо вік користувача з двох однакових цифр то має бути
# виведено тільки відповідне повідомлення! Також подумайте над варіантами, коли введені невірні або неадекватні дані.

print("КАСА")
age = str(input("Введіть, будь ласка, свій вік: "))
# Довжина строки
age_length = len(age)
# Змінна для перевірки на однакові цифри в році
same_digits = age_length > 1 and age.count(age[0]) == age_length

# Перевірка на чисельний ввід даних
if not age.isnumeric():
    print('Можна використовувати тільки цілі числа!')
else:
    # Міняємо тип данних в змінній age на int для зручності
    age = int(age)
    # перевірка на адекватність
    if age < 1 or age > 125 or age_length > 3:
        print('Неадекватні дані')
    # перевірка на однакові цифри
    elif same_digits:
        print('Як цікаво!')
    elif age < 7:
        print("Де твої батьки?")
    elif age < 16:
        print("Це фільм для дорослих!")
    elif age > 65:
        print("Покажіть пенсійне посвідчення!")
    else:
        print("А білетів вже немає!")