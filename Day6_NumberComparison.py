# Step 1: Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2: Compare the numbers
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is smaller than {num2}")
else:
    print("Both numbers are equal")
