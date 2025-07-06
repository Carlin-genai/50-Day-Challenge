# even_odd_checker.py
"""
A tiny utility to:
1. Check whether a single number is even or odd.
2. Apply that check to every number in a list.
"""

def is_even(num: int) -> bool:
    """Return True if num is even, False if odd."""
    return num % 2 == 0


def check_list(numbers: list[int]) -> list[str]:
    """
    Return a list of strings describing whether each
    element in 'numbers' is even or odd.
    """
    results = []
    for n in numbers:
        result = f"{n} is {'even' if is_even(n) else 'odd'}"
        results.append(result)
    return results


if __name__ == "__main__":
    # --- Single‑number check ---
    single = int(input("Enter a number to test: "))
    print(f"{single} is {'even' if is_even(single) else 'odd'}")

    # --- List check ---
    raw = input("Enter several integers separated by spaces: ")
    num_list = [int(s) for s in raw.split()]
    print("\nResults for the list:")
    for line in check_list(num_list):
        print("  •", line)
