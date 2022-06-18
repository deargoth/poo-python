from abc import ABC, abstractclassmethod

class Person(ABC):
    def __init__(self, forename, age):
        self.forename = forename
        self.age = age
        self.nomeclasse = self.__class__.__name__
    
    def speak(self):
        print(f"{self.nomeclasse} it's speaking...")

class Student(Person):
    def study(self):
        print(f"{self.nomeclasse} it's studying.")

class Client(Person):
    def buy(self):
        print(f"{self.nomeclasse} it's buying.")
        
    def speak(self):
        print('Im speaking has a CLIENT!')
        
class ClientVIP(Client):
    def __init__(self, forename, surname, age):
        Person.__init__(self, forename, age)
        self.surname = surname
    
    @property
    def name(self):
        return f'{self.forename} {self.surname}'