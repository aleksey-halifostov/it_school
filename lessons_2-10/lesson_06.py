import random


def guess(num):
    attempt = 3
    while attempt > 0:
        user_choice = int(input(f"Угадайте число от 1 до 10({attempt} попытки): "))
        if user_choice == num:
            print(f"Вы угадали! это число {num}")
            break
        attempt -= 1
    else:
        print("К сожалению, вы не угадали")


guess(random.randint(0, 10))
