from person import Person
from product import Product

class User(Person):
    def __init__(self, name, email, address, password, phone):
        super().__init__(name, email, address, password)
        self.phone = phone  # Public
        self.is_verified = False
        self.shopping_history = {}  # Public (Product object: quantity)

    def add_product(self, product, quantity):
        # If product already in shopping history, increase quantity
        if product in self.shopping_history:
            self.shopping_history[product] += quantity
        else:
            self.shopping_history[product] = quantity

    def total_spent(self):
        # Calculate total spent using Product price and quantity
        return sum(product._price * quantity for product, quantity in self.shopping_history.items())

    def verify_email(self):
        if self.check_email():
            self.is_verified = True
        else:
            raise ValueError("Invalid email address")

    def display_info(self):
        return f"User: {self.name}, Email: {self._email}, Total Spent: {self.total_spent()}, Verified: {self.is_verified}"
 
    def calculate_discount(self):
        # Implementează logica de calcul a reducerii aici
        # De exemplu, o reducere fixă de 5%
        return 0.05  # 5% reducere