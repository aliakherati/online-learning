from review import Review
from product import Product

class User:
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self._review = []

    def sell_product(self, name:str, description:str, price:int):
        product = Product(name, description, self, availability=True)
        print(f"{product} is on the market!")

    def buy_product(self, product:Product):
        if product._availability:
            print(f"{self} is buying {product}")
            product._availability = False
        else:
            print(f"{product} is no longer available.")

    def write_review(self, description:str, product:Product):
        review = Review(description, self, product._name)
        self._review.append(review)
        product._review.append(review)

    def __str__(self) -> str:
        return f"User(id: {self._id}, name: {self._name})"
