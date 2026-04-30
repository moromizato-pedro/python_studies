import alchemy.grimoire as grim

def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    valid_ingredients = grim.light_validator.validate_ingredients(ingredients)
    if "VALID" in valid_ingredients:
        spell_status = "Spell recorded"
    else:
        "Spell rejected"
    return f"{spell_status}: {spell_name} ({valid_ingredients})"
