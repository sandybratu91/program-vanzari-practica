import re
from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class Person(ABC):
    def __init__(self, name, email, address, password=None):
        self.name = name
        self._email = email
        self._password = None
        self._address = address
        self._login = False

    def check_email(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if(re.fullmatch(regex, self._email)):
            return True
        else:
            return False

    def check_login(self, email, password):
        if self._email == email and self._password == password:
            self._login = True
            return True
        return False

    def set_password(self, password):
        self._password = password

    @abstractmethod
    def display_info(self):
        pass
