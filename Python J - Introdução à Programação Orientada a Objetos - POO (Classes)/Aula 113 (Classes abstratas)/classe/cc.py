from distutils.log import error, info
from classe.conta import Conta
import re

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    # Getter
    @property
    def limite(self):
        return self._limite

    def depositar(self, valor):
        info = f'Depositando R${valor:.2f} em sua conta.'
        print(info)
        self.log_info(info)
        self._saldo += valor
        self.details()
        
    def sacar(self, valor):
        if (self._saldo + self.limite) < valor:
            error = 'Saldo para saque insuficiente'
            print(error)
            self.log_error(error)
            return

        info = f'Sacando R${valor:.2f} de sua conta.'
        print(info)
        self.log_info(info)
        self._saldo -= valor
        self.details()