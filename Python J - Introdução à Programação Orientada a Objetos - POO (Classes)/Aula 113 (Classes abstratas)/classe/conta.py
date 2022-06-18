from abc import ABC, abstractmethod
from classe.loging import LogMixin
import re


class Conta(ABC, LogMixin):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        if isinstance(valor, str):
            self._saldo = float(re.sub(r'[^0-9]', '', valor))
        self._saldo = valor

    # Getters:
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def conta(self):
        return self._conta
    
    
    @abstractmethod
    def depositar(self, valor):
        print(f'Estaremos depositando R${valor:.2f} em sua conta.')
        self._saldo =+ valor
        self.details()

    def sacar(self, valor):
        if self._saldo < valor:
            print('SACAR: Saldo insuficiente.')
            return
        
        print(f'Estaremos sacando R${valor:.2f} de sua conta.')
        self._saldo -= valor
        self.details()
    
    def details(self):
        print(f'DETALHES: Agência: {self._agencia} | Conta: {self._conta} | Saldo: R${self._saldo:.2f}\n')