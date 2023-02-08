class Product:
    def __init__(self, name:str, description:str, price:int, seller:str, availability:bool=True):
        self._name = name
        self._description = description
        self._price = price
        self._seller = seller
        self._availability = availability
        self._review = []

    def __str__(self):
        return f"Product({self._name}: {self._description} at ${self._price}"
