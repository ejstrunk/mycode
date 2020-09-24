#!/usr/bin/env python3

import sys

def main():
    print("Welcome to the Calculator! Input \"q\" at any time to quit.")
    user_input = " "
    result = 0.0
    result_string = " "
    choice = " "
    x = 0.0
    y = 0.0
    while user_input != "q":
        x = input("Please input your first number:\n>").lower()
        if x == "q":
            exit() 
        else:
            try:
                x = float(x)
            except:
                print("Please use a valid number")
                continue
        y = input("Please input your second number:\n>").lower()
        if y == "q":
            exit()
        else:
            try:
                y = float(y)
            except:
                print("Please use a valid number")
                continue
        while choice != "q":
            choice = input("Would you like to add, subtract, multiply, or divide?\n>").lower()
            if choice == "q":
                exit(x,y)
            elif choice == "add":
                add(x,y)
            elif choice == "subtract":
                subtract(x,y)
            elif choice == "multiply":
                multiply(x,y)
            elif choice == "divide":
                divide(x,y)
            else:
                print(f"{choice} is not a valid option")
                continue
            choice = input("Would you like to go again?\n>").lower()
            if choice in ["yes", "yep", "yup", "yah", "ya", "y"]:
                main()
            else:
                exit()
                
def exit():
    print("Goodbye")
    sys.exit()


def add(x,y):
    result = x + y
    print(f"The sum is {result}")

def subtract(x,y):
    result = x - y
    print(f"The difference is {result}")
    
def divide(x,y):
    result = x / y
    print(f"The quotient is {result}")

def multiply(x,y):
    result = x * y
    print(f"The product is {result}")

main()
