from bank.account import Account


class Bank:
    def __init__(self):
        self.agencies = [1111, 2222, 3333]
        self.clients = []

    def insert_client(self, client):
        if not client.account:
            print(f"The client {client.name} does not have an account.")
            return
            
        if client.account.agency not in self.agencies:
            print(f"The agency {client.account.agency} it's not accepted on our bank. Sorry!\n")
            return

        self.clients.append(client)

    def list_clients(self):
        print('Clients:')
        for client in self.clients:
            print(f'\tName: {client.name} | Age: {client.age} | Account: {client.account.agency} \
- {client.account.number} - R${client.account.balance:.2f}')

    def authenticate(self, client):
        if client not in self.clients:
            print(f"The client {client.name} it's not registered in our bank.")
            return False
        
        return True