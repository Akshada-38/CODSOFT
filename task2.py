# Simple Calculator

# Function to perform the calculation
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        # Handle division by zero
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Invalid operation."

# Main function to interact with the user
def main():
    # Prompt user for input
    print("Welcome to the simple calculator!")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        return
    
    print("Select an operation:")
    print(" + : Addition")
    print(" - : Subtraction")
    print(" * : Multiplication")
    print(" / : Division")

    operation = input("Enter the operation (+, -, *, /): ").strip()

    # Perform calculation and display result
    result = calculate(num1, num2, operation)
    print(f"The result is: {result}")

# Run the calculator
if __name__ == "__main__":
    main()
