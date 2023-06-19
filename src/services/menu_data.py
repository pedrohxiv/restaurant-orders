from src.models.dish import Dish
from src.models.ingredient import Ingredient

import csv


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.ingredients = set()
        self.load_menu_data(source_path)

    def load_menu_data(self, source_path: str) -> None:
        with open(source_path, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                dish_name, dish_price, ing_name, ing_quantity = row

                dish = self.get_dish(dish_name, float(dish_price))
                ingredient = self.get_ingredient(ing_name)

                dish.add_ingredient_dependency(ingredient, int(ing_quantity))

    def get_dish(self, name: str, price: float) -> Dish:
        for dish in self.dishes:
            if dish.name == name and dish.price == price:
                return dish

        dish = Dish(name, price)
        self.dishes.add(dish)
        return dish

    def get_ingredient(self, name: str) -> Ingredient:
        for ingredient in self.ingredients:
            if ingredient.name == name:
                return ingredient

        ingredient = Ingredient(name)
        self.ingredients.add(ingredient)
        return ingredient
