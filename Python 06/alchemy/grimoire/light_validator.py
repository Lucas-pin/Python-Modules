def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    allowed_ingredients = light_spell_allowed_ingredients()

    for ing in allowed_ingredients:
        if ingredients.count(ing) > 0:
            break
    else:
        return ingredients + " - INVALID"
    return ingredients + " - VALID"
