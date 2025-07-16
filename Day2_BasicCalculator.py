# Simple Calculator for Two Numbers

def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "Error: Cannot divide by zero!"
        return a / b
    else:
        return "Error: Invalid operator!"

# Input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Choose operation (+, -, *, /): ")

# Calculate and print result
result = calculator(num1, num2, op)
print("Result:", result)
