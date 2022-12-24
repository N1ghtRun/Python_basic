import requests


class ExchangeRate:

    day = None
    month = None
    year = None
    url = None
    response_object = None
    exchange_json = None

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def set_url(self):
        self.url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date=" \
                   f"{self.year}{self.month}{self.day}&json"

    def get_json(self):
        # getting response object
        try:
            self.response_object = requests.get(self.url)
        except:
            print("Couldn't get response object")
            quit()

        # status code check
        if self.response_object.status_code // 100 == 4:
            print(f"Response status code: {self.response_object.status_code}")
            print("Most likely typo in the request. \n")
            quit()
        elif self.response_object.status_code // 100 == 5:
            print(f"Response status code: {self.response_object.status_code}")
            print("Unable to get correct response from the server :(")
            quit()

        # check for correct JSON
        if len(self.response_object.json()) > 1:
            self.exchange_json = self.response_object.json()
        else:
            print("Couldn't load correct JSON. Check parameters")
            quit()

    def save_data(self):
        data = ""
        with open(f"{self.day}_{self.month}_{self.year}.txt", "w") as file:
            for i in range(1, len(self.exchange_json)):
                data += f"{i}. {self.exchange_json[i-1]['txt']} to UAH: {self.exchange_json[i-1]['rate']}\n"
            file.write(data)
