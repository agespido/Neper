import json


class Ingredient:
    def __init__(self, name):
        self.name= name
        self.quantity = None

    def add_quantity(self, quant: str):
        self.quantity = quant

    def tojson(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)


class Recipe:
    def __init__(self, name: str, type: str, ingredients=[]):
        self.name = name
        self.type = type
        self.kcal = 0.0
        self.protein = 0.0
        self.fat = 0.0
        self.sat_fat = 0.0
        self.ins_fat = 0.0
        self.carbs = 0.0
        self.sugar = 0.0
        self.ingredients = ingredients

    def add_ingredient(self, ing: Ingredient):
        self.ingredients.append(ing)

    @property
    def tojson(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)
