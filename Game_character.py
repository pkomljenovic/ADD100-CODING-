"""
ASSIGNMENT 10B: SPRINT 3 - REFACTORING & DATA ACCOUNTABILITY
Project: Game Character Setup System
Developer: [Your Name]
"""

# GLOBAL CONSTANTS
SAVE_FILE = "characters.txt"
DEFAULT_CLASS = "Warrior"
DEFAULT_WEAPON = "Sword"
DEFAULT_POINTS = 5
CLASS_OPTIONS = ("Warrior", "Mage", "Archer")
WEAPON_OPTIONS = ("Sword", "Bow", "Staff", "Dagger")


def get_player_info():
    """Gets player name and kingdom with default values."""
    name = input("Player Name: ").title() or "Unknown Hero"
    kingdom = input("Kingdom Name: ").title() or "No Kingdom"
    return name, kingdom


def create_character(default_class=DEFAULT_CLASS, default_weapon=DEFAULT_WEAPON, default_points=DEFAULT_POINTS):
    """Collects character setup choices using default parameters."""
    print(f"Available Classes: {CLASS_OPTIONS}")
    char_class = input("Choose a class: ").title() or default_class

    print(f"Available Weapons: {WEAPON_OPTIONS}")
    weapon = input("Choose a weapon: ").title() or default_weapon

    points_input = input("Assign skill points: ")
    skill_points = int(points_input) if points_input.isdigit() else default_points

    return {
        "class": char_class,
        "weapon": weapon,
        "points": skill_points
    }


def calculate_power(character_data):
    """Calculates total power level."""
    base_power = 10
    bonus_power = character_data["points"] * 2
    return base_power + bonus_power


def save_and_display_character(player, kingdom, power):
    """Displays the character summary."""
    print("\n--- CHARACTER SUMMARY ---")
    print(f"HERO: {player}")
    print(f"KINGDOM: {kingdom}")
    print(f"POWER LEVEL: {power}")


def main():
    # 1. Player Identity Phase
    name, kingdom = get_player_info()

    # 2. Character Creation Phase
    character = create_character()

    # 3. Power Calculation Phase
    total_power = calculate_power(character)

    # 4. Final Display Phase (Keyword Arguments)
    save_and_display_character(player=name, kingdom=kingdom, power=total_power)


main()