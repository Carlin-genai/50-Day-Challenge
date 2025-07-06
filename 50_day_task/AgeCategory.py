"""
age_category.py
Determine whether someone is a child, teenager, adult, or senior
based on their age (in years).
"""

def get_age_category(age: int) -> str:
    """
    Returns a string describing the life‑stage category
    for a given age in years.
    """
    if age < 0:
        return "Invalid age"
    elif age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"

def main():
    try:
        # 1️⃣  Ask the user for input
        age_input = input("Enter your age in years: ")

        # 2️⃣  Convert the input to an integer
        age = int(age_input)

        # 3️⃣  Determine the category
        category = get_age_category(age)

        # 4️⃣  Display the result
        print(f"You are classified as: {category}")

    except ValueError:
        print("Please enter a valid integer for age.")

if __name__ == "__main__":
    main()
