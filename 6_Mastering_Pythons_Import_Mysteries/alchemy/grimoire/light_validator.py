import alchemy.grimoire as grim

def validate_ingredients(ingredients: str) -> str:
    is_valid = "INVALID"
    for ingredient in grim.light_spellbook.light_spell_allowed_ingredients():
        if ingredients.lower().find(ingredient) != -1:
            is_valid = "VALID"
            break
    return f"{ingredients} - {is_valid}"
