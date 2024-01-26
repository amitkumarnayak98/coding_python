def add_numbers (a, b):
    return a + b

def subtract_numbers (a, b):
    return a - b

def multiply_numbers (a, b):
    return a * b

def divide_numbers (a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Error: Division by zero is not allowed.")

def power (base, exponent):
    return base ** exponent

#Input
try:
    operator = input("Enter an operator (+, -, *, /, ^): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")
    exit(1)

# Calculation
try:
    if operator == '+':
        result = add_numbers(num1, num2)
    elif operator == '-':
        result = subtract_numbers(num1, num2)
    elif operator == '*':
        result = multiply_numbers(num1, num2)
    elif operator == '/':
        result = divide_numbers(num1, num2)
    elif operator == '^':
        result = power(num1, num2)
    else:
        raise ValueError("Error: Invalid operator.")
except ValueError as e:
    print(e)
    exit(1)

# Output
print(f"Result: {result}")

