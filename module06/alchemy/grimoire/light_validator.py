from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spell_allowed_ingredients()
    valid = any(item.lower() in ingredients.lower() for item in allowed)
    return f"{ingredients} - {'VALID' if valid else 'INVALID'}"
