from distutils.log import error
from classe.conta import Conta
import re


class ContaPoupanca(Conta):
    def depositar(self, valor):
        info = f'Depositando R${valor:.2f}'
        print(info)
        self.log_info(info)
        self._saldo += valor
        self.details()

    def sacar(self, valor):
        if self._saldo < valor:
            error = 'Saldo para saque insuficiente.'
            print(error)
            self.log_error(error)
            return

        msg = f'Sacando R${valor:.2f}.'
        print(msg)
        self.log_info(msg)
        self._saldo -= valor
        self.details()