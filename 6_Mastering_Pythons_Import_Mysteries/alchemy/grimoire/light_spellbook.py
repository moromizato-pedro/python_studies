from light_validator import validate_ingredients

def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    if "VALID" in validate_ingredients(ingredients):
        spell_status = "Spell recorded"
    else:
        "Spell rejected"
    return f"{spell_status}: {spell_name} ({validate_ingredients})"
