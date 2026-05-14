# Import the regular expression module to clean the input
import re
# Create loops to allow the user to perform multiple calculations until they choose to exit
while True:
    # Welcome the user to the calculator
    print("Welcome to the simple calculator!")
    # Ask the user for the first number
    num1 = (input("Enter the first number: "))
    # Ask the user for the second number
    num2 = (input("Enter the second number: "))
    # Clean the input and convert to float
    num1 = float(re.sub(r'[^0-9.]', '', num1))
    num2 = float(re.sub(r'[^0-9.]', '', num2))
    # Ask the user for the operation they want to perform
    operation = input("Enter the operation (+, -, *, /): ")
    # Clean the operation input
    operation = re.sub(r'[a-zA-Z0-9\s]', '', operation)
    # Perform the calculation based on the operation
    if operation == "+":
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result:.2f} to 2 decimal places.")
    elif operation == "-":
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result:.2f} to 2 decimal places.")
    elif operation == "*":
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result:.2f} to 2 decimal places.")
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result:.2f} to 2 decimal places.")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please enter one of +, -, *, /.")
    # Ask the user if they want to perform another calculation
    again = input("Do you want to perform another calculation? (yes/no): ")
    if again.lower() == "no":
        print("Exiting the calculator. Goodbye!")
        break
    elif again.lower() == "yes":
        print("Starting a new calculation...")
        continue
    else:
        print("Invalid input. Exiting the calculator. Goodbye!")
        break
