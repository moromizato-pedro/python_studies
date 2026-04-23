from string import capwords


def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    message = None
    seed = f"{capwords(seed_type)} seeds: "
    if unit == "packets":
        message = f"{quantity} {unit} available"
    elif unit == "grams":
        message = f"{quantity} {unit} total"
    elif unit == "area":
        message = f"covers {quantity} square meters"
    if message:
        print(seed + message)
    else:
        print("Unknown unit type")
