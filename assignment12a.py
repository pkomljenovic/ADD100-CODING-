"""
-----------------------------------------------------------------------
ASSIGNMENT 12A: THE CONFIGURABLE MENU & AUDITOR
-----------------------------------------------------------------------
[✓] 1. Header Docstring included.
[✓] 2. PHASE 1: External menu_config.txt file created in workspace.
[✓] 3. Program reads and parses the .txt file into a Dictionary.
[✓] 4. PHASE 2: break the dictionary into individual variables.
[✓] 5. Menu contains at least 4 categories.
[✓] 6. Print each category and its details.
[✓] 7. try/except used to prevent crashes on FileNotFoundError.
-----------------------------------------------------------------------
"""

# -------------------------
# PHASE 1: CREATE + SAVE MENU
# -------------------------


def get_menu():
    menu = {}
    while True:
        category = input("Enter category (Q to quit): ").upper().strip()
        if category == "Q":
            break
        items = input("Enter items separated by commas: ").strip()
        menu[category] = items
    return menu



def save_menu(menu):
    try:
        with open("menu_config.txt", "w") as file:
            for category, items in menu.items():
                file.write(f"{category};{items}\n")
    except Exception as e:
        print("Error writing to file:", e)


# -------------------------
# PHASE 2: READ + PARSE MENU
# -------------------------


def read_menu():
    menu = {}
    try:
        with open("menu_config.txt", "r") as file:
            for line in file:
                parts = line.strip().split(";")
                if len(parts) == 2:
                    category = parts[0].strip()
                    items = parts[1].strip()
                    menu[category] = items
    except FileNotFoundError:
        print("Error: menu_config.txt not found.")
    return menu


# -------------------------
# BREAK INTO VARIABLES
# -------------------------


def split_menu(menu):
    coffee = menu.get("COFFEE")
    milk = menu.get("MILK")
    flavors = menu.get("FLAVORS")
    shots = menu.get("SHOTS")
    return coffee, milk, flavors, shots


# -------------------------
# PRINT MENU
# -------------------------


def print_menu(coffee, milk, flavors, shots):
    print("\n--- MENU ---")

    if coffee:
        print("\nCOFFEE")
        for item in coffee.split(","):
            print(f"\t{item.strip()}")

    if milk:
        print("\nMILK")
        for item in milk.split(","):
            print(f"\t{item.strip()}")

    if flavors:
        print("\nFLAVORS")
        for item in flavors.split(","):
            print(f"\t{item.strip()}")

    if shots:
        print("\nSHOTS")
        for item in shots.split(","):
            print(f"\t{item.strip()}")


# -------------------------
# MAIN PROGRAM
# -------------------------


def main():
    print("1. Create Menu")
    print("2. Display Menu")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        menu = get_menu()
        save_menu(menu)
        print("Menu saved!")

    elif choice == "2":
        menu = read_menu()
        coffee, milk, flavors, shots = split_menu(menu)
        print_menu(coffee, milk, flavors, shots)

    else:
        print("Invalid choice.")


main()
