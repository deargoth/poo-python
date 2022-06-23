from human.person import Person


class Client(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.account = None
        
    def insert_account(self, account):
        self.account = account
        
    def show_account(self):
        if self.account:
            print(f"Agency: {self.account.agency} | Number: {self.account.number} \
| Balance: {self.account.balance}")
        
        else:
            print('You do not have a account yet.')