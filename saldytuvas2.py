class Product:
    def __init__(self, name:str, quantity:float, **kwargs) -> None:
        self.name = name
        self.quantity = quantity
        self.unit_of_measurement = 'unit' # options: kg, g, L, ml
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        return f'{self.name}: {self.quantity}'
    
    def __repr__(self) -> str:
        return f'{self.name}, {self.quantity}'
    

class Recipe:
    ingredients = []
    instructions = []

    def add_ingredients(self, product:Product):
        self.ingredients.append(product)
        pass

    def change_ingredient_quantity(self, ingredient_id: int, new_quantity:float):
        self.ingredients[ingredient_id].quantity = new_quantity
        pass

    def remove_ingridient(self, ingredient_id:int):
        self.ingredients.pop(ingredient_id)


class Fridge:
    content = []
    
    def check_product(self, product_name:str) -> (int, Product):
        for product_id, product in enumerate(self.contents):
            if product.name == product_name:
                return product_id, product
        return None, None 
    
    def add_product(self, product_name, quantity):
        product_id, product = self.check_product(name) 
        if product is not None:
            product.quantity += quantity
        else:
            self.contents.append(Product(name, quantity))


    def check_product_quantity(self, product:Product, quantity:float):
        product_id, product = self.check_product(name) #nenaudojamus kintamuosius galima vadinti tiesiog _
        return product.quantity - quantity

    def remove_product(self, name:str, quantity:float):
        pass

    def print_contents(self):
        pass

    def check_recipe(self, recipe:Recipe):
        pass
    

def main ():
    fridge = Fridge()
    #meniu