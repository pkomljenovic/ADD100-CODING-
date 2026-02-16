# ATM Program

balance = 1000.00

while True:
    print("\n===== ATM MENU =====")
    print("1. Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Exit")

    choice = input("Enter selection: ").strip()

    match choice:

        # 1. Balance
        case "1":
            print(f"Current Balance: ${balance:.2f}")

        # 2. Deposit
        case "2":
            amount = input("Enter deposit amount: ").strip()

            if amount.replace('.', '', 1).isdigit():
                amount = float(amount)

                if amount <= 0:
                    print("Deposit must be greater than $0.00")
                else:
                    balance += amount
                    print(f"Deposited: ${amount:.2f}")
                    print(f"New Balance: ${balance:.2f}")
            else:
                print("Invalid amount. Numbers only.")

        # 3. Withdraw
        case "3":
            amount = input("Enter withdrawal amount: ").strip()

            if amount.replace('.', '', 1).isdigit():
                amount = float(amount)

                if amount <= 0:
                    print("Withdrawal must be greater than $0.00")

                elif amount > balance:
                    print("Insufficient funds. No overdrafts allowed.")

                else:
                    balance -= amount
                    print(f"Withdrawn: ${amount:.2f}")
                    print(f"New Balance: ${balance:.2f}")
            else:
                print("Invalid amount. Numbers only.")

        # 4. Transfer
        case "4":
            amount = input("Enter transfer amount: ").strip()

            if amount.replace('.', '', 1).isdigit():
                amount = float(amount)

                if amount <= 0:
                    print("Transfer must be greater than $0.00")

                elif amount > balance:
                    print("Insufficient funds. Transfer cancelled.")

                else:
                    balance -= amount
                    print(f"Transferred: ${amount:.2f}")
                    print(f"New Balance: ${balance:.2f}")
            else:
                print("Invalid amount. Numbers only.")

        # 5. Exit
        case "5":
            print("Thank you for using the ATM. Goodbye!")
            break

        # Invalid choice
        case _:
            print("Invalid Selection")
