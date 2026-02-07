"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[ ] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[ ] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""
# 1. Header Docstring
"""
Author: Predrag Komljenovic
Description: This program contains two tasks. The first task is a while loop that simulates a nagging kid asking "Are we there yet?" until the user responds with "yes". The second task is a for loop that counts backwards from 99 to 1, printing the number of bottles of beer on the wall.
"""
# 2. Task 1: While Loop (The Nagging Kid)
nagging = True
while nagging:
    response = input("Are we there yet? ")
    if response.lower() == "yes":
        nagging = False
# 3. Task 2: For Loop (99 Bottles of Beer)
for bottles in range(99, 0, -1):
    print(f"{bottles} bottles of beer on the wall!")
