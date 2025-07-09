# Step 1: Set the minimum password length
MIN_LENGTH = 8

# Step 2: Ask the user to enter a password
password = input("Enter your password: ")

# Step 3: Check if the password meets the minimum length
if len(password) >= MIN_LENGTH:
    print("✅ Password is valid.")
else:
    print(f"❌ Password too short! Must be at least {MIN_LENGTH} characters.")
