# 1. Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів, які містять дві голосні
# літери підряд.
# 2. Є два довільних числа які відповідають за мінімальну і максимальну ціну. Є Dict з назвами магазинів і цінами:
# { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166,
# "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}. Напишіть код, який знайде і виведе на екран назви
# магазинів, ціни яких попадають в діапазон між мінімальною і максимальною ціною. Наприклад:
# lower_limit = 35.9
# upper_limit = 37.339
# > match: "x-store", "main-service"


# Task 1
print("\nTask 1")
# Getting data from the user
while True:
    data_string = input("Enter the data in the string: ")
    if data_string:
        break
    else:
        print("String can't be empty!\n")

vowels = 'aeiuo'
# Creating the list containing words from the input and which will be used in the cycle
data_list = data_string.split()
# List which will contain words with 2 vowels in a row
res_list = []
counter = 0
# variable for comparing symbols in the inner cycle
previous_element = ' '
# going through elements in the list
for element in data_list:
    for symbol in element.lower():
        if symbol in vowels and previous_element in vowels:
            counter += 1
            res_list.append(element)
            break
        else:
            previous_element = symbol
    previous_element = ' '

print(f"\nWords with two vowels in the row: {counter}")
print(f"List with your input: {data_list}")
print(f"List with words that has 2 vowels in the row: {res_list}")


# Task 2
print("\n\nTask 2")
lower_limit = 35.9
upper_limit = 37.339
stores = {"cito": 47.999, "BB_studio": 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324,
           "x-store": 37.166, "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}
match_list = []

for item in stores.items():
    if lower_limit <= item[1] <= upper_limit:
        match_list.append(item[0])

if match_list:
    print("Match:", ", ".join(match_list))
else:
    print("No matches!")
