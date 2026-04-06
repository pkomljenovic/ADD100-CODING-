"""
-----------------------------------------------------------------------
ASSIGNMENT 11A REVISED: THE BUG TRACKING LOG
-----------------------------------------------------------------------
[ ] 1. Program uses a while loop to keep asking for bugs.
[ ] 2. Uses the datetime module to get a timestamp format.
[ ] 3. Stores the timestamp, file name, description, and priority in a dictionary.
[ ] 4. Uses `with open("bug_log.txt", "a")` to append to the file safely.
[ ] 5. The bug_log.txt file is formatted neatly with newlines.
-----------------------------------------------------------------------
"""

import datetime

def log_bug():
    # Get user input
    file_name = input("File name: ")
    description = input("Description of error: ")
    priority = input("Priority (High, Medium, Low): ")

    # Generate timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Store in dictionary
    bug_dict = {
        timestamp: [file_name, description, priority]
    }

    # Append to file
    with open("bug_log.txt", "a") as file:
        file.write(f"""[{timestamp}]
File: {bug_dict[timestamp][0]}
Status: {bug_dict[timestamp][1]}
Priority: {bug_dict[timestamp][2]}
--------------------------------------------------
""")

def main():
    while True:
        choice = input("Enter 'log' to record a bug, or 'quit' to stop: ").lower()

        if choice == "log":
            log_bug()
        elif choice == "quit":
            print("Bug log updated!")
            break
        else:
            print("Invalid input. Try again.")

# Run program
main()