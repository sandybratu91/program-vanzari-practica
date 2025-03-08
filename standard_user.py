from user import User

class StandardUser(User):
    def __init__(self, name, email, address, phone):
        super().__init__(name, email, address, "parola_andrei", phone)

    def calculate_discount(self):
        # Implementează logica de calcul a reducerii aici
        # De exemplu, o reducere fixă de 10%
        return 0.1  # 10% reducere