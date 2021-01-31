import math

while True:
    def calc(number1, number2):
        opr = input("Что будем делать (+, -, *, **, /, //, %, fac, ceil, sqrt) ")

        if opr == "+":
            print(number1 + number2)

        elif opr == "-":
            print(number1 - number2)

        elif opr == "*":
            print(number1 * number2)

        elif opr == "**":
            print(number1 ** number2)

        elif opr == "/":
            print(number1 / number2)

        elif opr == "//":
            print(number1 // number2)

        elif opr == "%":
            print(number1 % number2)

        elif opr == "fac":
            print(math.factorial(number1))

        elif opr == "ceil":
            print(math.ceil(number1))

        elif opr == "sqrt":
            print(math.sqrt(number1))
    number1 = float(input("Введите первое число "))
    number2 = float(input("Введите второе число "))
    calc(number1, number2)
