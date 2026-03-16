"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global Constants BASES and FRUITS defined as Tuples.
[ ] 3. Professional function get_price(size) returns a float.
[ ] 4. Professional function blend(size, base, fruit, scoops) for output.
[ ] 5. main() function handles try/except for scoops (int).
[ ] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""

BASES = ("water", "milk", "juice")
FRUITS = ("strawberry", "banana", "mango", "blueberry")


def get_price(size):
    """
    Returns the price of the smoothie based on size.

    Parameters:
        size (str): The smoothie size.

    Returns:
        float: The price of the smoothie.
    """
    size = size.lower()

    if size == "small":
        return 4.99
    elif size == "medium":
        return 5.99
    elif size == "large":
        return 6.99
    else:
        return 0.0


def blend(size, base, fruit, scoops):
    """
    Displays the smoothie order details.

    Parameters:
        size (str): The smoothie size.
        base (str): The smoothie base.
        fruit (str): The fruit selected.
        scoops (int): Number of fruit scoops.
    """
    price = get_price(size)

    print("\n--- Smoothie Order ---")
    print(f"Size: {size}")
    print(f"Base: {base}")
    print(f"Fruit: {fruit}")
    print(f"Scoops: {scoops}")
    print(f"Total Price: ${price:.2f}")
    print("Your smoothie is being blended!")


def main():
    """
    Runs the smoothie ordering program.
    """
    size = input("Choose a size (small, medium, large): ").lower()
    base = input(f"Choose a base {BASES}: ").lower()
    fruit = input(f"Choose a fruit {FRUITS}: ").lower()

    try:
        scoops = int(input("How many scoops of fruit would you like? "))
        blend(size, base, fruit, scoops)
    except ValueError:
        print("Invalid input. Please enter a whole number for scoops.")


main()