class Vehicle:
    weight = 20000  # kg
    max_speed = 300  # km/h
    number_of_seats = 4


class Automobile(Vehicle):
    body_type = 'Sedan'
    engine = 'Internal combustion'  # electric or internal combustion

    def __init__(self, weight: int | float, max_speed: int | float, number_of_seats: int, body_type: str, engine: str):
        self.weight = weight
        self.max_speed = max_speed
        self.number_of_seats = number_of_seats
        self.body_type = body_type
        self.engine = engine


class Aircraft(Vehicle):
    uses = 'Civil'  # military or civil
    flight_distance = None  # flight distance without refiling

    def __init__(self, weight: int | float, max_speed: int | float, number_of_seats: int, uses: str,
                 flight_distance: int | float):
        self.weight = weight
        self.max_speed = max_speed
        self.number_of_seats = number_of_seats
        self.uses = uses
        self.flight_distance = flight_distance


class Boat(Vehicle):
    boat_type = 'Hydroplane'

    def __init__(self, weight: int | float, max_speed: int | float, number_of_seats: int, boat_type: str):
        self.weight = weight
        self.max_speed = max_speed
        self.number_of_seats = number_of_seats
        self.boat_type = boat_type
