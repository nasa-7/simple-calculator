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
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b

def power(a, b):
    return a ** b


def modulus(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a % b

OPERATIONS = {"+": add, "-": subtract, "*": multiply, "/": divide, "**": power, "%": modulus}


def main():
    print("Simple Calculator")
    a = float(input("Enter first number: "))
    op = input("Operation (+, -, *, /, **, %):")
    b = float(input("Enter second number: "))
    print("Result:", OPERATIONS[op](a, b))  # BUG: crashes on bad input


if __name__ == "__main__":
    main()