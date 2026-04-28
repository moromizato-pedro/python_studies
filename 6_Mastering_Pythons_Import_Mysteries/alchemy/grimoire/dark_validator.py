from dark_spellbook import dark_spell_allowed_ingredients

def validate_ingredients(ingredients: str) -> str:
    is_valid = "INVALID"
    for ingredient in dark_spell_allowed_ingredients():
        if ingredients.lower().find(ingredient) != -1:
            is_valid = "VALID"
            break
    return f"{ingredients} - {is_valid}"
