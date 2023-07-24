import time
import lesson_12_1 as transport


class Truck(transport.Auto):

    def __init__(self, max_load, brand, age, mark, color="No information", weight=0):
        self.max_load = max_load
        super().__init__(brand, age, mark, color, weight)

    def move(self):
        print("Attention")
        super().move()

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(transport.Auto):

    def __init__(self, max_speed, brand, age, mark, color="No information", weight=0):
        self.max_speed = max_speed
        super().__init__(brand, age, mark, color, weight)

    def move(self):
        print(f"max speed is {self.max_speed}")
        super().move()


my_car = Car(300, "Audi", 0, "RS6", color="Black", weight=1100)
car_1 = Car(150, "Reno", 2, "Logan", color="Blue")
truck_1 = Truck(3, "Reno", 4, "Magnum", weight=3000)
truck_2 = Truck(5, "DAF", 0, "XF")

for elem in (my_car, car_1, truck_1, truck_2):
    print(f"Properties of object is: {elem.__dict__}")
