"""
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[ ] 3. Function 'make_pizza' defines 4 specific parameters.
[ ] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[ ] 5. main() displays the Global Pantry list to the user.
[ ] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
"""
from typing import Tuple
# Global constant for available pizza toppings
TOPPINGS: Tuple[str, ...] = ("pepperoni", "mushrooms", "onions", "sausage", "bacon", "extra cheese", "black olives", "green peppers", "pineapple", "spinach")   

def make_pizza(size: str, crust_type: str, toppings: Tuple[str, ...], is_delivery: bool = False) -> None:
    """Create and display a pizza order summary.

    :param size: Pizza size selected by the user.
    :param crust_type: Crust style selected by the user.
    :param toppings: Tuple of validated topping names.
    :param is_delivery: Delivery flag; False means pickup.
    :return: None
    """
    print(f"Creating a {size} pizza with {crust_type} crust.")
    print("Toppings:")
    for topping in toppings:
        print(f"- {topping}")
    if is_delivery:
        print("This pizza will be delivered.")
    else:
        print("This pizza will be for pickup.")


def main() -> None: 
    """Collect input safely, validate values, and place a pizza order.

    :return: None
    """
    print("Welcome to the Pizza Engine!")
    print("Available toppings:")
    for topping in TOPPINGS:
        print(f"- {topping}")

    try:
        size_input = input("Enter pizza size [Medium]: ").strip()
        size = size_input if size_input else "Medium"

        crust_input = input("Enter crust type [Regular]: ").strip()
        crust_type = crust_input if crust_input else "Regular"

        topping_input = input(
            "Choose toppings (comma-separated, leave blank for cheese): "
        ).strip()

        if topping_input:
            requested = tuple(
                topping.strip().lower()
                for topping in topping_input.split(",")
                if topping.strip()
            )
        else:
            requested = ("extra cheese",)

        invalid = [t for t in requested if t not in TOPPINGS]
        if invalid:
            print("Invalid toppings ignored:", ", ".join(invalid))

        valid_toppings = tuple(t for t in requested if t in TOPPINGS)
        if not valid_toppings:
            valid_toppings = ("extra cheese",)

        delivery_input = input("Delivery? (y/n) [n]: ").strip().lower()
        is_delivery = delivery_input in ("y", "yes")

        # Use explicit keyword arguments for the function call.
        make_pizza(
            size=size,
            crust_type=crust_type,
            toppings=valid_toppings,
            is_delivery=is_delivery,
        )
    except (ValueError, TypeError) as exc:
        print(f"Input error: {exc}. Using safe defaults.")
        make_pizza(
            size="Medium",
            crust_type="Regular",
            toppings=("extra cheese",),
            is_delivery=False,
        )


if __name__ == "__main__":
    main()