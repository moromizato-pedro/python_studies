from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    valid_ingredients = validate_ingredients(ingredients)
    if "VALID" in valid_ingredients:
        spell_status = "Spell recorded"
    else:
        spell_status = "Spell rejected"
    return f"{spell_status}: {spell_name} ({valid_ingredients})"
