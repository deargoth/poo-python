from numpy import real
from vendas.formata import preço

def aumento(valor, porcentagem, formata=False):
    resultado = valor + (valor * (porcentagem / 100))

    if formata:
        return preço.real(resultado)
    else:
        return resultado

def redução(valor, porcentagem, formata=False):
    resultado = valor - (valor * (porcentagem / 100))
    if formata:
        return preço.real(resultado)
    else:
        return resultado