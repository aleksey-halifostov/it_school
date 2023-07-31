class Calculator:

    @staticmethod
    def add(a, b):
        try:
            return a + b
        except ValueError:
            print("Not correct arguments!")
        except TypeError:
            print("Try to enter integer or float!")

    @staticmethod
    def minus(a, b):
        try:
            return a - b
        except ValueError:
            print("Not correct arguments!")
        except TypeError:
            print("Try to enter integer or float!")

    @staticmethod
    def multiplication(a, b):
        try:
            return a * b
        except ValueError:
            print("Not correct arguments!")
        except TypeError:
            print("Try to enter integer or float!")

    @staticmethod
    def division(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Argument 'b' can't equal 0")
        except TypeError:
            print("Try to enter integer or float!")

    @staticmethod
    def exponentiation(a, b):

        try:
            if b < 0:
                raise LessZero
            return a ** b
        except LessZero:
            print("'b' must be can't be less than 0")
        except TypeError:
            print("Try to enter integer or float!")


class LessZero(Exception):

    def __init__(self, message="Argument 'b' can't be less than 0"):
        super().__init__(message)
