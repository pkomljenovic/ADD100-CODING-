"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[ ] 1. Create a list of 20 seats (numbered 1-20).
[ ] 2. Display the list of available seats.
[ ] 3. Ask user for a seat number (0 to quit).
[ ] 4. Remove the selected seat from the list.
[ ] 5. Handle invalid inputs (seat taken or doesn't exist).
[ ] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
"""
# 1. Create a list of 20 seats (numbered 1-20).
seats = list(range(1, 21))
while True:
    # 2. Display the list of available seats.
    print(f"Available Seats: {seats}")

    # 3. Ask user for a seat number (0 to quit).
    choice = input("Enter seat number to purchase (0 to quit): ").strip()

    if choice == "0":
        print("Thank you for using the ticket sales system. Goodbye!")
        break

    if choice.isdigit():
        seat_number = int(choice)

        # 5. Handle invalid inputs (seat taken or doesn't exist).
        if seat_number in seats:
            # 4. Remove the selected seat from the list.
            seats.remove(seat_number)
            print(f"Seat {seat_number} purchased successfully.")
        else:
            print(f"Seat {seat_number} is not available. Please choose another seat.")
    else:
        print("Invalid input. Please enter a valid seat number.")
    # 6. Repeat until user quits or seats are empty.
    if not seats:
        print("All seats have been sold. Thank you!")
        break