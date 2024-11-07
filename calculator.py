# Simple calculator for Colab (text-based)

def calculator():
    print("Welcome to the Text-based Calculator!")
    print("Options:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    try:
        choice = int(input("Choose an option (1/2/3/4): "))
        
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice. Please select a valid option.")
            return

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print(f"The result is: {num1 + num2}")
        elif choice == 2:
            print(f"The result is: {num1 - num2}")
        elif choice == 3:
            print(f"The result is: {num1 * num2}")
        elif choice == 4:
            if num2 != 0:
                print(f"The result is: {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the calculator
calculator()
