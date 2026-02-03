"""
Name:Predrag Komljenovic 
📚 Assignment 2A: Variables & Input
📅 Date: January 26th 2026
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included (Assignment Name, Date, File Name).
[ ] 2. Program asks for at least 5 different inputs (variables).
[ ] 3. Output uses F-Strings to combine text and variables.
[ ] 4. Output uses at least one escape sequence (\n or \t).
[ ] 5. Code contains comments explaining the steps.
[ ] 6. Program runs without errors.
-----------------------------------------------------------------------
"""
# Program to create a sprint badge based on user input
# Asking for user inputs
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
sprint_number = input("Enter sprint number: ")
sprint_date = input("Enter sprint date: ")
team_name = input("Enter team name: ")
# Creating the badge using f-strings and escape sequences
badge = f"""
----------------------------------------
\tSprint Badge
\tName: {first_name} {last_name}
\tSprint Number: {sprint_number}
\tDate: {sprint_date}
\tTeam: {team_name}
----------------------------------------
"""
# Displaying the badge
print(badge) 