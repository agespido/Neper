import json


class Ingredient:
    name: str
    quantity: str

    def tojson(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class Recipe:
    name: str
    type: str
    kcal: float
    ingredients: []

    @property
    def tojson(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
