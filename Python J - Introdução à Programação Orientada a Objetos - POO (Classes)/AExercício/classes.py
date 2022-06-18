from inspect import Attribute
from random import randint
import afunctions

class DataBase:
    def __init__(self):
        self.dicio = {}
    
    
    def insert_client(self, client, ident):
        # @staticmethod
        # def create_id():
        #     identificação = randint(0, 999)
        #     return identificação
        
        # ident = create_id()
        ident = str(ident)
        
        
        if 'clients' not in self.dicio:
            self.dicio['clients'] = {ident: client}
            
        else:
            self.dicio['clients'].update({ident: client})

            
    def list_clients(self):
        for identific, client in self.dicio['clients'].items():
            for address in client.address:
                print(f'ID: {identific}\nName: {client.name} | CPF: {client.cpf} | Age: {client.age} | {address.city} - {address.states}\n')

    def delete_client(self):
        self.list_clients()
        id_to_remove = input('Wich client do you want to delete? (ID): ')

        if id_to_remove in self.dicio['clients'].keys():
            del self.dicio['clients'][id_to_remove]
            print(f'Client of ID {id_to_remove} was removed.\n')
            
        else:
            print('We couldnt encounter a client with this ID.')

class Client:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
        self.__address = []
        self.__cpf = ''
        
        
    @property
    def name_getter(self):
        return self._name
    
    @name_getter.setter
    def name(self, valor):
        self._name = valor.title()
    
    @property
    def age(self):
        return self.__age
    
    @property
    def address(self):
        return self.__address
    
    @property
    def cpf(self):
        try:
            return self.__cpf.cpf
        except AttributeError:
            print(f'Error on validating CPF of {self.name}.\n')
            return self.__cpf


    def set_address(self, city, states):
        self.__address.append(Address(city, states))
    
    def informations(self):
        for address in self.__address:
            print(f'Name: {self.name} | Age: {self.__age} | CPF: {self.cpf} | Town: {address.city} - {address.states}')
            
    def set_cpf(self, cpf):
        past_cpf = Cpf(cpf)
        if past_cpf.validate(cpf):
            self.__cpf = past_cpf
        else:
            self.__cpf = 'CPF inválido.'
        
    
class Address:
    def __init__(self, city, states):
        self.__city = city
        self.__states = states
    
    @property
    def city(self):
        return self.__city
    
    @property
    def states(self):
        return self.__states
    
class Cpf:
    def __init__(self, cpf):
        self.cpf = cpf
    
    def validate(self, cpf):
        validate = afunctions.validating_cpf(cpf)
        if validate:
            return True
        else:
            return False
    