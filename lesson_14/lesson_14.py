class Car(object):
    FUEL_TYPES = ['бензин', 'дизель', 'электричество', 'гибрид']
    COLORS = []
    NUMBER_OF_CARS = 0

    def __init__(self, model, year, color, fuel_type):
        self.model = model
        self.year = year
        self.color = color

        if color not in Car.COLORS:
            Car.COLORS.append(color)

        self.fuel_type = Car.is_valid_fuel_type(fuel_type, Car.FUEL_TYPES)
        Car.NUMBER_OF_CARS += 1
        self.number = Car.NUMBER_OF_CARS

    @staticmethod
    def is_valid_fuel_type(fuel, valid_fuels):
        if fuel not in valid_fuels:
            fuel = valid_fuels[0]

        return fuel

    def __str__(self):
        return f"Модель: {self.model}, Год выпуска: {self.year}, Тип двигателя: {self.fuel_type}, Цвет: {self.color}"

    @property
    def numbers(self):
        return f"{self.number} from {Car.NUMBER_OF_CARS}"

    @classmethod
    def get_used_colors(cls):
        return len(cls.COLORS)

    @classmethod
    def get_number_of_cars(cls):
        return cls.NUMBER_OF_CARS


car_1 = Car('Zaz', 1979, 'black', 'дизель')
car_2 = Car('BMW', 2000, 'red', 'бензин')
car_3 = Car('VOLVO', 2012, 'black', 'электричествоcccc')
car_4 = Car('Mersedes', 2012, 'black', 'гибрид')

print('COLORS:', Car.get_used_colors())
print('NUMBER_OF_CARS:', Car.get_number_of_cars())

for item in (car_1, car_2, car_3, car_4):
    print('item:', item)
    print('numbers:', item.numbers)
