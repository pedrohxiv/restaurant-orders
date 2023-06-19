from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction
import pytest


def test_dish():
    dish1 = Dish("Lasanha", 24.70)
    dish2 = Dish("Salmão Grelhado", 28.20)
    dish3 = Dish("Lasanha", 24.70)

    assert dish1.name == "Lasanha"
    assert dish1.price == 24.70
    assert repr(dish1) == "Dish('Lasanha', R$24.70)"

    assert dish2.name == "Salmão Grelhado"
    assert dish2.price == 28.20
    assert repr(dish2) == "Dish('Salmão Grelhado', R$28.20)"

    assert dish1 == dish3
    assert dish1 != dish2

    assert hash(dish1) == hash(dish3)
    assert hash(dish1) != hash(dish2)

    ingredient1 = Ingredient("massa de lasanha")
    ingredient2 = Ingredient("queijo mussarela")
    ingredient3 = Ingredient("presunto")

    dish1.add_ingredient_dependency(ingredient1, 1)
    dish1.add_ingredient_dependency(ingredient2, 1)
    dish1.add_ingredient_dependency(ingredient3, 1)

    assert dish1.recipe == {
        ingredient1: 1,
        ingredient2: 1,
        ingredient3: 1
    }

    assert dish1.get_ingredients() == {ingredient1, ingredient2, ingredient3}

    assert dish1.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.GLUTEN,
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
    }

    with pytest.raises(TypeError):
        Dish("Lasanha", "24.70")

    with pytest.raises(ValueError):
        Dish("Lasanha", -24.70)
