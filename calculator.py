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
    print("Simple Calculator (type 'q' to quit)")
    while True:
        op = input("Operation (+, -, *, /, **, %) or q: ").strip()
        if op.lower() == "q":
            print("Goodbye!")
            break

        if op not in OPERATIONS:
            print("Invalid operation, try again.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number, try again.")
            continue

        print("Result:", OPERATIONS[op](a, b))




if __name__ == "__main__":
    main()