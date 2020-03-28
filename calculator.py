import sys
import time

def get_numbers():
    first_number = float(input("Enter the first number:\n"))
    second_number = float(input("Enter the second number:\n"))

    return first_number, second_number

def add(first_number, second_number):
    addition = first_number + second_number

    return addition

def subtract(first_number, second_number):
    subtraction = first_number - second_number

    return subtraction

def multiply(first_number, second_number):
    multiplication = first_number * second_number

    return multiplication

def divide(first_number, second_number):
    division = first_number / second_number

    return division
def quit():
    print("The application will now exit.")
    time.sleep(2)
    sys.exit()


def menu():
    print("******Main Menu******")
    time.sleep(1)

    choice = input("""
    A: Add
    B: Subtract
    C: Multiply
    D: Divide
    Q: Quit
    
    Please make a selection from A, B, C, D, or Q:\n
    """)

    if choice == "A" or choice == "a":
        number1, number2 = get_numbers()
        result = add(number1, number2)
        print("Your addition result is " + str(result))
    elif choice == "B" or choice == "b":
        number1, number2 = get_numbers()
        result = subtract(number1, number2)
        print("Your subtraction result is " + str(result))
    elif choice == "C" or choice == "c":
        number1, number2 = get_numbers()
        result = multiply(number1, number2)
        print("Your multiplication result is " + str(result))    
    elif choice == "D" or choice == "d":
        number1, number2 = get_numbers()
        result = divide(number1, number2)
        print("Your division result is " + str(result))    
    elif choice == "Q" or choice == "q":
        quit()
    else:
        print("Invalid credentials. Please try again.")
        time.sleep(1)
        menu()

menu()
