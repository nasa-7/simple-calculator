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

HISTORY_FILE = "history.txt"
def save_to_history(a, op, b, result):
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"{a} {op} {b} = {result}\n")
def show_history():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            print("--- History ---")
            print(f.read() or "(empty)")
    except FileNotFoundError:
            print("No history yet.")



def main():
    print("Simple Calculator (type 'h' for history, 'q' to quit)")
    while True:
        op = input("Operation (+, -, *, /, **, %), h, or q: ").strip()
        if op.lower() == "q":
            print("Goodbye!")
            break
        if op.lower() == "h":
            show_history()
            continue
        if op not in OPERATIONS:
            print("Invalid operation, try again.")
            continue
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number, try again.")
            continue
        result = OPERATIONS[op](a, b)
        print("Result:", result)
        save_to_history(a, op, b, result)


