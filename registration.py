"""
Assignment 5A – Input Validation Program
Author: Predrag Komljenovic
Description:
This program collects registration information and validates all user input.

Validation Implemented:
1. Name – letters only using a while loop
2. Age – positive integer using try/except (type safety)
3. Chaperone – yes/no validation using a while loop
4. Ticket Count – positive integer using try/except

All fields prevent invalid data before continuing execution.
"""

# Assignment 5A: Input Validation (Fixed Version)
# Now includes 4 inputs, proper validation loops, and try/except for type safety

# ---- Name ----
name = input("Enter your name: ")
while not name.isalpha():
    print("Invalid input. Please enter a valid name (letters only).")
    name = input("Enter your name: ")

# ---- Age ----
while True:
    try:
        age = int(input("Enter your age: "))
        if age <= 0:
            raise ValueError
        break
    except:
        print("Invalid input. Please enter a positive number for age.")

# ---- Chaperone ----
chaperone = input("Do you have a chaperone? (yes/no): ").upper()
while chaperone not in ["YES", "NO"]:
    print("Invalid input. Please enter 'yes' or 'no'.")
    chaperone = input("Do you have a chaperone? (yes/no): ").upper()

# ---- Ticket Count (4th required field) ----
while True:
    try:
        tickets = int(input("How many tickets would you like?: "))
        if tickets <= 0:
            raise ValueError
        break
    except:
        print("Invalid input. Please enter a positive number of tickets.")

# ---- Output ----
print("\n----- Registration Info -----")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Chaperone: {chaperone}")
print(f"Tickets: {tickets}")
