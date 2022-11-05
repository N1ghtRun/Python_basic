# завдання 1
# урл http://api.open-notify.org/astros.json
# вивести список всіх астронавтів, що перебувають в даний момент на орбіті (дані не фейкові, оновлюються в режимі
# реального часу)
#
# завдання 2
# апі погоди (всі токени я для вас вже прописав)
# https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=47503e85fabbabc93cff28c52398ae97&units=metric
# де city_name - назва міста на аглійській мові (наприклад, odesa, kyiv, lviv)
# роздрукувати тепрературу та швидкість вітру. з вказівкою міста, яке було вибране


import requests
from tabulate import tabulate


# Task 1
print("\nTASK 1\n")

url = 'http://api.open-notify.org/astros.json'
response = requests.get(url)

# Checking for 200 responds from the server. // 100 to make sure that the first digit of status code is 2
if response.status_code // 100 == 2:
    # Main dictionary
    data = response.json()
    # List containing dict with astronauts
    astronauts = data["people"]
    # Total number of astronauts
    astronauts_counter = data["number"]

    print("List of the astronauts currently on the orbit: \n")
    print(tabulate(astronauts, headers='keys', tablefmt='pipe'))
    print(f"\nTotal number: {astronauts_counter}\n")
else:
    print("Unable to get correct response from the server :(")
    print(f"Response status code: {response.status_code}")


# Task 2
print("\nTASK 2\n")
print("Weather checker")

while True:
    city_name = input("Type in the city name to check the weather. Only letters allowed (case insensitive): ")
    print("\n")
    # In my opinion this line is readable...
    if not city_name.replace("-", "").replace("'", "").isalpha():
        print("Only letters allowed, try again")
    else:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=47503e85fabbabc93cff28c52398ae97" \
              "&units=metric"
        response = requests.get(url)
        if response.status_code // 100 == 4:
            print(f"Response status code: {response.status_code}")
            print("Most likely typo in the city name, try again. \n")
        elif response.status_code // 100 == 5:
            print("Unable to get correct response from the server :(")
            print(f"Response status code: {response.status_code}")
            quit()
        else:
            # Main dictionary
            data = response.json()
            temperature = f"{data['main']['temp']} °C"
            wind_speed = f"{data['wind']['speed']} m/sec"
            result_data = {"City": city_name.capitalize(), "Current temperature": temperature, "Wind speed": wind_speed}
            print(tabulate([result_data, ], headers='keys', tablefmt='grid', stralign='center'), "\n")
            print("\nNow you can choose another city")
