
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operator"
while True:
 
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter the operator (+, -, *, /): ").strip()

        result = calculate(num1, num2, operator)
        print(f"The result of {num1} {operator} {num2} is: {result}")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An error occurred: {e}")

    try_again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if try_again != 'yes':
        print("Exiting the calculator.")
        break
