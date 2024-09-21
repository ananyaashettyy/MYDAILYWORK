#Simple Calculator Program

def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    elif operation == '%':
        if num2 != 0:
            return num1 % num2
        else:
            return "Error: Division by zero is not allowed."
    elif operation == '**':
        return num1 ** num2
    else:
        return "Invalid operation."


def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def get_operation_input():
    operations = ['+', '-', '*', '/', '%', '**']
    while True:
        operation = input("Enter the operation (+, -, *, /, %, **): ")
        if operation in operations:
            return operation
        else:
            print("Invalid operation! Please enter a valid operation from the list (+, -, *, /, %, **).")


def main():
    print("Calculator")
    
    while True:
       
        num1 = get_number_input("Enter the first number: ")
        num2 = get_number_input("Enter the second number: ")
        operation = get_operation_input()

        
        result = calculate(num1, num2, operation)
        print(f"The result is: {result}")

       
        choice = input("Do you want to perform another calculation? (yes/no): ").lower()
        if choice != 'yes':
            print("Thank you for using the calculator!")
            break

if __name__ == "__main__":
    main()
