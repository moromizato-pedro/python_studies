import alchemy.grimoire as grim

def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    valid_ingredients = grim.dark_validator.validate_ingredients(ingredients)
    if "VALID" in valid_ingredients:
        spell_status = "Spell recorded"
    else:
        "Spell rejected"
    return f"{spell_status}: {spell_name} ({valid_ingredients})"
