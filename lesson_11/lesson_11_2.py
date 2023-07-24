import json
import random
import csv


def phone_number():
    number = ""
    if random.randint(0, 3):
        operators = ['095', '066', '098', '096', '050', '097']
        number = random.choice(operators)
        for i in range(0, 7):
            number += str(random.randint(0, 9))

    return number


def main():
    with open("01.json") as file:
        data = json.load(file)

    with open("02.csv", "w") as file:
        file = csv.writer(file)
        file.writerow(("ID", "Имя", "Возраст", "Телефон"))

        for key in data:
            line = [key]
            for elem in data[key]:
                line.append(elem)

            line.append(phone_number())
            file.writerow(line)


main()
