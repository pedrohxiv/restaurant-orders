from src.models.ingredient import Ingredient, Restriction


def test_ingredient():
    ingredient1 = Ingredient("farinha")
    ingredient2 = Ingredient("ovo")
    ingredient3 = Ingredient("farinha")

    assert ingredient1.name == "farinha"
    assert ingredient1.restrictions == {Restriction.GLUTEN}
    assert repr(ingredient1) == "Ingredient('farinha')"

    assert ingredient2.name == "ovo"
    assert ingredient2.restrictions == {Restriction.ANIMAL_DERIVED}
    assert repr(ingredient2) == "Ingredient('ovo')"

    assert ingredient1 == ingredient3
    assert ingredient1 != ingredient2

    assert hash(ingredient1) == hash(ingredient3)
    assert hash(ingredient1) != hash(ingredient2)
