"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Ask user for Monthly Income (float).
[ ] 3. Ask user for 5 DIFFERENT expense amounts (float).
[ ] 4. Calculate Total Expenses and Remaining Balance.
[ ] 5. Calculate Percentage of Income Spent.
[ ] 6. Output formatted to 2 decimal places (:,.2f or :.2%).
-----------------------------------------------------------------------
"""

# 1. Header Docstring
"""
This program calculates the total expenses, remaining balance,
and percentage of income spent based on user input for monthly income
and five different expense amounts.
"""
# 2. Ask user for Monthly Income (float).
monthly_income = float(input("Enter your Monthly Income: "))
# 3. Ask user for 5 DIFFERENT expense amounts (float).
expense1 = float(input("Enter expense amount 1: "))
expense2 = float(input("Enter expense amount 2: "))
expense3 = float(input("Enter expense amount 3: "))
expense4 = float(input("Enter expense amount 4: "))
expense5 = float(input("Enter expense amount 5: "))
# 4. Calculate Total Expenses and Remaining Balance.
total_expenses = expense1 + expense2 + expense3 + expense4 + expense5
remaining_balance = monthly_income - total_expenses
# 5. Calculate Percentage of Income Spent.
percentage_spent = (total_expenses / monthly_income) * 100
# 6. Output formatted to 2 decimal places (:,.2f or :.2%).
print(f"\nTotal Expenses: ${total_expenses:,.2f}")
print(f"Remaining Balance: ${remaining_balance:,.2f}")
print(f"Percentage of Income Spent: {percentage_spent:.2f}%")