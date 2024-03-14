class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __repr__(self):
        return f"{self.name}, {self.description}, {self.price}, {self.quantity}"

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
