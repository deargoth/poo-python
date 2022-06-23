import re

class Person:
    def __init__(self, name: str, age: int):
        if self.__class__ is Person:
            raise TypeError("Person class cannot be instanciated")
        self.name = name
        self.age = age

    # Getters
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @name.setter
    def name(self, value):
        self._name = value.title()

    @age.setter
    def age(self, value):
        if isinstance(value, str):
            value = int(re.sub(r'[^0-9]', '', value))
        self._age = value
