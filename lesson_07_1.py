import random

check_int = lambda x: "Ваше число равно 0" if x == 0 else "Не четное" if x % 2 else "Четное"

print(check_int(random.randint(0, 10)))
