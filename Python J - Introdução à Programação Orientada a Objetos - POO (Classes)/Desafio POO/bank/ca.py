from bank.account import Account
from funct.verifytype import verify_type

class CheckingAccount(Account):
    def __init__(self, agency, number, balance, limit=200):
        super().__init__(agency, number, balance)
        self._limit = limit

    def withdraw(self, value):
        value = float(verify_type(value))
        if (self._balance + self._limit) < value:
            print('Balances exceeded.')
            return

        print(f'Withdrawing US${value:.2f}')
        self._balance -= value
        print(f'Current balance: US${self._balance:.2f}')
        
    def deposit(self, value):
        return super().deposit(value)


        