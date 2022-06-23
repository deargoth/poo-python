from funct.verifytype import verify_type
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, agency, number, balance):
        self._agency = agency
        self._number = number
        self.balance = balance
        
    @property
    def agency(self):
        return self._agency
    
    @property
    def number(self):
        return self._number

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        value = float(verify_type(value))
        self._balance = value

    
    @abstractmethod
    def withdraw(self, value):
        value = float(verify_type(value))
        if value > self._balance:
            print('Balance exceeded.')
            return
        
        print(f'Withdrawing US${value:.2f}')
        self._balance -= value
        print(f'Current balance: US${self._balance:.2f}')
        
    def deposit(self, value):
        value = float(verify_type(value))
        self._balance += value
        print(f'Depositing: US${value:.2f}')
    