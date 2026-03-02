"""
-----------------------------------------------------------------------
ASSIGNMENT 7A: STRING MASTERY LAB
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with your name.
[ ] 2. Task 1: String Basics (Length, Indexing, ASCII) completed.
[ ] 3. Task 2: The Cleanup Crew (Strip, Case, Replace) completed.
[ ] 4. Task 3: Validation (isdigit check) completed.
[ ] 5. Task 4: The Duck Loop (.join and direct iteration) completed.
-----------------------------------------------------------------------
Name: [Predrag Komljenovic]
-----------------------------------------------------------------------
"""

# --- TASK 1: TUNING THE GUITAR ðŸŽ¸ ---
instrument = "Acoustic Guitar"
# Task 1 outputs
print("\n--- Task 1: Tuning the Guitar ---")
print(f"Instrument: {instrument}")
print(f"Length: {len(instrument)}")
print(f"First letter: {instrument[0]}")
print(f"Last letter: {instrument[-1]}")
min_char = min(instrument)
max_char = max(instrument)
print(f"Lowest ASCII char: '{min_char}' (ord={ord(min_char)})")
print(f"Highest ASCII char: '{max_char}' (ord={ord(max_char)})")


# --- TASK 2: THE CLEANUP CREW ðŸ§µ ---
messy_input = "   vOLUME_knob_11   "
print("\n--- Task 2: The Cleanup Crew ---")
cleaned = messy_input.strip()
print(f"After strip(): '{cleaned}'")
uppered = cleaned.upper()
print(f"After upper(): '{uppered}'")
replaced = uppered.replace("_", " ")
print(f"After replace(): '{replaced}'")


# --- TASK 3: THE VALIDATOR ðŸ” ---
serial_number = "90210"
print("\n--- Task 3: The Validator ---")
if serial_number.isdigit():
	print("Valid Serial")
else:
	print("Invalid Serial")


# --- TASK 4: THE DUCK BRIDGE ðŸ¦†ðŸŽµ ---
# We are going to sing about a Duck!
# We can't change strings (immutable), so we convert to a list
name_string = "DUCKY"
duck_letters = list(name_string)
count = 0

print("\n--- Singing the Duck Song! ---")
duck_emoji = "🦆"
for char in name_string:
	current_name = " ".join(duck_letters)
	print("There was a teacher who had a duck and Ducky was his Name-o")
	print(f"({current_name}) \n" * 3)
	print("and Ducky was his Name-o!\n")
	# replace current index with the duck emoji
	duck_letters[count] = duck_emoji
	count += 1

final_name = " ".join(duck_letters)
print("--- Finale! ---")
print("There was a teacher who had a duck and Ducky was his Name-o")
print(f"({final_name}) \n" * 3)
print("and Ducky was his Name-o!\n")
