from person import Person
from datetime import datetime, timedelta


class Employee(Person):
    def __init__(self, name, email, address, salary):
        super().__init__(name, email, address)
        self._salary = salary
        self._working_hours = timedelta(0)
        self._start_time = None

    def increase_salary(self, percentage):
        self._salary *= (1 + percentage / 100)

    def checkin(self):
        if self._login:
            self._start_time = datetime.now()

    def checkout(self):
        if self._start_time:
            self._working_hours += datetime.now() - self._start_time
            self._start_time = None

    def get_working_hours(self):
        return self._working_hours

    def get_salary(self):
        return self._salary
    
class ContractEmployee(Employee):
    def __init__(self, name, email, address, salary, contract_end):
        super().__init__(name, email, address, salary)
        self.contract_end = contract_end

    def display_info(self):
        return f"Contract Employee: {self.name}, Email: {self._email}, Address: {self._address}, Salary: {self._salary}, Contract End: {self.contract_end}"

class Freelancer(Employee):
    def __init__(self, name, email, address, salary, projects):
        super().__init__(name, email, address, salary)
        self.projects = projects

    def display_info(self):
        return f"Freelancer: {self.name}, Email: {self._email}, Address: {self._address}, Salary: {self._salary}, Projects: {self.projects}"

