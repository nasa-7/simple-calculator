"""Simple Calculator
Contributors: Arwa Ahmed, Anfal Abdelhameed, Ahmed Malik
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b  # BUG: crashes when b is 0


OPERATIONS = {"+": add, "-": subtract, "*": multiply, "/": divide}


def main():
    print("Simple Calculator")
    a = float(input("Enter first number: "))
    op = input("Operation (+, -, *, /): ")
    b = float(input("Enter second number: "))
    print("Result:", OPERATIONS[op](a, b))  # BUG: crashes on bad input


if __name__ == "__main__":
    main()