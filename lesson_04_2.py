while True:
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    if not age.isdigit() or int(age) <= 0:
        print("Ошибка, повторите ввод")
    elif int(age) < 10:
        print(f"Привет шкет, {name}")
    elif int(age) <= 18:
        print(f"Как жизнь, {name}?")
    elif int(age) < 100:
        print(f"Что желаете {name}?")
    else:
        print(f"{name}, вы лжете - в наше время столько не живут...")

    # Check if user want to stop program
    is_continue = input("Желаете выйти? (Д/Y): ")
    if is_continue.upper() in ("Y", "Д"):
        break
