from art import logo
import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

operations = {
    "+" : add,
    "-" : subtract,
    "/" : divide,
    "*" : multiply
    }

def calculator():
    print(logo)
    n1 = float(input("What's the first number?: "))
    continue_calculation = True
    while continue_calculation:
        operator = input("+\n-\n*\n/\nPick an operator: ")
        n2 = float(input("What's the next number?: "))
        result = operations[operator](n1, n2)
        print(f"{n1} {operator} {n2} = {result}")
        n1 = result
        continue_calculation = input(f"Type 'y' to continue calculating with {result}, type 'n' to start new calculation or 'end' um zu stoppen:\n").lower()
        if continue_calculation == 'n' or continue_calculation == "no":
            os.system('cls' if os.name == 'nt' else 'clear')
            calculator()
            break
        elif continue_calculation == "end":
            print("Calculator ended")
            break

calculator()