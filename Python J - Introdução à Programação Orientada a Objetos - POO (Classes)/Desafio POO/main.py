from human.client import Client
from bank.ca import CheckingAccount
from bank.bank import Bank
from bank.sa import SavingAccount

bank = Bank()

client = Client('Vinícius', 34)
account = CheckingAccount(1111, 9092, 0)
client.insert_account(account)

client2 = Client('Pedro', 73)
account2 = SavingAccount(2222, 1892, 0)
client2.insert_account(account2)

client3 = Client('Leonardo', 33)
account3 = CheckingAccount(3333, 9231, 0)
client3.insert_account(account3)

bank.insert_client(client)
bank.insert_client(client2)
bank.insert_client(client3)

if bank.authenticate(client3):
    client3.account.deposit(40)
    client3.account.withdraw(9)
else:
    print('Not authorized.')