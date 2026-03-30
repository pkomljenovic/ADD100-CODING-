"""
ASSIGNMENT 10B: SPRINT 3 - REFACTORING & DATA ACCOUNTABILITY
Project: Gaming Store Checkout
Developer: [Predrag Komljenovic]
"""

# GLOBAL CONSTANTS
MENU_FILE = "games.txt"
TAX_RATE = 0.07
DEFAULT_WARRANTY = "No"
PLATFORM_OPTIONS = ("PlayStation", "Xbox", "Nintendo Switch", "PC")

def get_customer_info():
    """Collects customer name and pickup number."""
    name = input("Customer Name: ").title()
    pickup_number = input("Pickup Number: ")
    return name, pickup_number

def take_order(warranty=DEFAULT_WARRANTY):
    """Collects game order details."""
    game_title = input("Game Title: ").title()
    print(f"Available Platforms: {PLATFORM_OPTIONS}")
    platform = input("Choose Platform: ").title()

    edition = input("Edition (Standard/Deluxe): ").title()

    user_warranty = input("Add Warranty? (Yes/No, press Enter for default): ").title()
    if user_warranty != "":
        warranty = user_warranty

    return {
        "game_title": game_title,
        "platform": platform,
        "edition": edition,
        "warranty": warranty
    }

def calculate_total(order_data):
    """Calculates total cost based on edition and warranty."""
    base_price = 59.99

    if order_data["edition"] == "Deluxe":
        base_price += 20.00

    if order_data["warranty"] == "Yes":
        base_price += 9.99

    tax = base_price * TAX_RATE
    return base_price + tax

def print_receipt(customer, pickup_number, total):
    """Prints checkout receipt."""
    print("\n--- GAME STORE RECEIPT ---")
    print(f"PICKUP #: {pickup_number} | CUSTOMER: {customer}")
    print(f"TOTAL: ${total:.2f}")

def main():
    # 1. Customer Info
    name, pickup_number = get_customer_info()

    # 2. Order Info
    current_order = take_order()

    # 3. Price Calculation
    final_total = calculate_total(current_order)

    # 4. Receipt Output using KEYWORD ARGUMENTS
    print_receipt(customer=name, pickup_number=pickup_number, total=final_total)

main()