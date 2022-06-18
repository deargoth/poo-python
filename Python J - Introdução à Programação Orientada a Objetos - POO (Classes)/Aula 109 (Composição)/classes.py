class Client:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.address = []
        
    def append_address(self, city, states):
        self.address.append(Address(city, states))

    def show_addres(self):
        for address in self.address:
            print(address.city, address.states)
        


class Address:
    def __init__(self, city, states):
        self.city = city
        self.states = states


client1 = Client('Lucas', 18)
client1.append_address('Rio', 'RJ')
client1.show_addres()