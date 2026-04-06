"""
-----------------------------------------------------------------------
ASSIGNMENT 11A: THE OFFICE HERO DASHBOARD
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constants OFFICE_NAME and TAX_RATE defined in ALL_CAPS.
[ ] 3. Function 'process_expenses' returns TWO values (float, string).
[ ] 4. main() function uses try/except for numeric price/qty inputs.
[ ] 5. main() calls function using KEYWORD ARGUMENTS.
[ ] 6. main() correctly unpacks and prints both return values.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS
OFFICE_NAME = "Tech Office"
TAX_RATE = 0.05

def process_expenses(item_name, price, quantity):
    # Calculate subtotal
    subtotal = price * quantity
    
    # Calculate tax
    tax = subtotal * TAX_RATE
    
    # Final total
    total = subtotal + tax
    
    # Create summary string
    summary = f"{OFFICE_NAME} purchased {quantity} x {item_name}"
    
    return total, summary  # RETURN TWO VALUES


def main():
    item = input("Enter item name: ")
    
    try:
        price = float(input("Enter item price: "))
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid input. Defaulting values.")
        price = 1.0
        quantity = 1

    # KEYWORD ARGUMENTS + UNPACKING
    final_total, summary_text = process_expenses(
        item_name=item,
        price=price,
        quantity=quantity
    )

    print(f"\nTotal Cost: ${final_total:.2f}")
    print(summary_text)


# Run program
main()