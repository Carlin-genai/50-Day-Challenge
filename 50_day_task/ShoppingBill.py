# Step 1: Get prices of 3 items from the user
item1 = float(input("Enter the price of item 1: ₹"))
item2 = float(input("Enter the price of item 2: ₹"))
item3 = float(input("Enter the price of item 3: ₹"))

# Step 2: Get tax percentage from the user
tax_percent = float(input("Enter tax percentage (e.g., 18 for 18%): "))

# Step 3: Calculate subtotal (sum of item prices)
subtotal = item1 + item2 + item3

# Step 4: Calculate tax amount
tax_amount = (tax_percent / 100) * subtotal

# Step 5: Calculate total cost including tax
total = subtotal + tax_amount

# Step 6: Print the final total
print(f"\nSubtotal: ₹{subtotal:.2f}")
print(f"Tax Amount (@{tax_percent}%): ₹{tax_amount:.2f}")
print(f"Total Cost: ₹{total:.2f}")
