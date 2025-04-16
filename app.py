def calculator():
    """
    A simple calculator function that allows the user to perform basic arithmetic operations.

    The user can select one of the following operations:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Percentage

    The function prompts the user to input their choice of operation and the required numbers.
    It then performs the selected operation and displays the result.

    Operations:
    - Addition: Adds two numbers.
    - Subtraction: Subtracts the second number from the first.
    - Multiplication: Multiplies two numbers.
    - Division: Divides the first number by the second (if the second number is not zero).
    - Percentage: Calculates the percentage of the given number (divides the number by 100).

    Input:
    - choice (str): The operation to perform (1/2/3/4/5).
    - num1 (float): The first number.
    - num2 (float, optional): The second number (not required for percentage calculation).

    Output:
    - Prints the result of the selected operation.
    - Displays an error message if the user attempts to divide by zero or enters an invalid choice.
    """
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Percentage")

    # Take input from the user
    choice = input("Enter choice (1/2/3/4/5): ")

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        if choice == '5':
            print(f"The result is: {num1 / 100}")
        else:
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"The result is: {num1 + num2}")
            elif choice == '2':
                print(f"The result is: {num1 - num2}")
            elif choice == '3':
                print(f"The result is: {num1 * num2}")
            elif choice == '4':
                if num2 != 0:
                    print(f"The result is: {num1 / num2}")
                else:
                    print("Error: Division by zero is not allowed.")
    else:
        print("Invalid input. Please select a valid operation.")

if __name__ == "__main__":
    calculator()