from employee import ContractEmployee, Freelancer, Employee
from user import User
from product import Product
from standard_user import StandardUser

def main():
    products = [
        Product("Laptop", 5000, 20, "Laptop performant"),
        Product("Telefon", 3000, 5, "Telefon inteligent"),
        Product("Tableta", 1500, 15, "Tableta cu ecran mare"),
    ]

    employees = {
        "ion": ContractEmployee("Ion Popescu", "ion.popescu@company.com", "Str. Unirii 10", 7000, "2024-12-31"),
        "maria": Freelancer("Maria Ionescu", "maria.ionescu@freelance.com", "Str. Libertatii 5", 5000, 3),
    }

    users = {
        "andrei": StandardUser("Andrei Georgescu", "andrei.georgescu@email.com", "Str. Victoriei 20", "0722123456"),
        "elena": User("Elena Dumitrescu", "elena.dumitrescu@email.com", "Str. Independentei 15", "0744654321", "parola_elena"),
    }

    new_user = StandardUser("Nume Nou", "emailnou@email.com", "Adresa Noua", "0755112233")
    if new_user.check_email():
        users["nou"] = new_user
        print("Utilizator nou înregistrat cu succes!")
    else:
        print("Adresă de e-mail invalidă.")

    for key, user in users.items():
        if user.check_login("andrei.georgescu@email.com", "parola_andrei"):
            print(f"{user.name} s-a conectat.")

    andrei = next(user for key, user in users.items() if user.name == "Andrei Georgescu")
    andrei.add_product(products[0], 2)
    total_spent = andrei.total_spent()
    discount = andrei.calculate_discount()
    print(f"Total cheltuit: {total_spent}, Reducere: {discount * 100}%")

    for employee in employees.values():
        employee.checkin()
        employee.checkout()

    most_hours_employee = max(employees.values(), key=lambda emp: emp.get_working_hours())
    most_hours_employee._salary *= 1.5
    print(f"Angajatul cu cele mai multe ore: {most_hours_employee.name}, Salariu actualizat: {most_hours_employee._salary}")

    try:
        new_product = Product("Căști", 200, 30, "Căști wireless")
        products.append(new_product)
        print("Produs nou adăugat cu succes!")
    except Exception as e:
        print(f"Eroare la adăugarea produsului: {e}")

if __name__ == "__main__":
    main()