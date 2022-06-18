import re

class Produto:

    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço

    #Getter
    @property
    def preço(self):
        return self._preço

    #Setter
    @preço.setter
    def preço(self, valor):
        if isinstance(valor, str):
            valor = float(re.sub(r'[^0-9]', '', valor))
        
        self._preço = valor


    #Getter
    @property
    def nome(self):
        return self._nome
    
    #Setter
    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

        

    def desconto(self, porcentagem):
        self.preço = self.preço - (self.preço * (porcentagem / 100))

        