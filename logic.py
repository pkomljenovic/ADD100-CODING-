"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with your name.
[ ] 2. Ask user for two integers (num1 and num2).
[ ] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[ ] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""
# 1. Header Docstring
"""
Author: Predrag Komljenovic
Description: This program performs various logical checks on two integers provided by the user and categorizes one of the integers based on its value.
"""
# 2. Ask user for two integers
num1 = int(input("Enter the first integer (num1): "))
num2 = int(input("Enter the second integer (num2): "))
# 3. Perform 6 logical checks
both_greater_than_zero = num1 > 0 and num2 > 0
both_greater_than_hundred = num1 > 100 and num2 > 100
either_even = num1 % 2 == 0 or num2 % 2 == 0
either_less_than_hundred = num1 < 100 or num2 < 100
not_equal = num1 != num2
not_zero = num1 != 0 and num2 != 0
# Print results of logical checks
print(f"Both numbers greater than 0: {both_greater_than_zero}")
print(f"Both numbers greater than 100: {both_greater_than_hundred}")
print(f"Either number is even: {either_even}")
print(f"Either number is less than 100: {either_less_than_hundred}")
print(f"Numbers are not equal: {not_equal}")
print(f"Neither number is zero: {not_zero}")
# 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero)
if num1 > 0:
    print("num1 is Positive")
elif num1 < 0:
    print("num1 is Negative")
else:    print("num1 is Zero")
