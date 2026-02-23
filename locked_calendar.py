"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE LOCKED CALENDAR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. MONTHS is defined as a constant tuple ().
[ ] 3. Program uses a for loop to display each month.
[ ] 4. 'try' and 'except' blocks catch a TypeError.
[ ] 5. Comments explain why the modification failed.
-----------------------------------------------------------------------
"""
# 1. Header Docstring included.
# 2. MONTHS is defined as a constant tuple ().
MONTHS = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
# 3. Program uses a for loop to display each month.
for month in MONTHS:
    print(month)
# 4. 'try' and 'except' blocks catch a TypeError.
try:
    # Attempt to modify the MONTHS tuple (which is immutable)
    MONTHS[0] = "Jan"
except TypeError as e:
    # 5. Comments explain why the modification failed.
    print("Error: Cannot modify a tuple because it is immutable.")
    print(f"Details: {e}")
