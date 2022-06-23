from bank.account import Account

class SavingAccount(Account):
    def __init__(self, agency, number, balance):
        super().__init__(agency, number, balance)
        
    def withdraw(self, value):
        return super().withdraw(value)
    
    def deposit(self, value):
        return super().deposit(value)