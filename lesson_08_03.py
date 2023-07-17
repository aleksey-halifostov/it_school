from datetime import datetime


def my_decorator(func):
    def check_time():
        time = datetime.now()
        func()
        print(datetime.now() - time)

    return check_time


@my_decorator
def hello():
    print("Hello world!")


@my_decorator
def summa():
    print(2 + 3)


hello()
summa()
