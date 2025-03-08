class Product:
    def __init__(self, name, price, quantity, description):
        self.name = name
        self._price = price
        self.quantity = quantity
        self._description = description
        
    def get_price(self):
        return self._price

    def check_quantity(self):
        return self.quantity > 10