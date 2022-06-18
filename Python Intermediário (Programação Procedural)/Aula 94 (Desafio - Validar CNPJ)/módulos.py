"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Dígitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segundo digito
"""


import re
import random
import clipboard

def verificar_seq(cnpj):
    sequencia = cnpj[0] * len(cnpj)
    if sequencia == cnpj:
        return True
    else:
        return False
    
def fórmula(numero):
    digito = 11 - (numero % 11)
    return digito


def remover_caracteres(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def firstDigit(cnpj):
    cnpj = remover_caracteres(cnpj)
    
    novo_cnpj = cnpj[:-2]

    count = 5
    soma_calculo = 0
    
    for numero in novo_cnpj:
        numero = int(numero)
        calculo =+ (numero * count)
        soma_calculo += calculo
        count -= 1
        if count < 2:
            count = 9
    primeiro_digito = fórmula(soma_calculo)
    if primeiro_digito > 9:
        primeiro_digito = 0
    return str(primeiro_digito)


def secondDigit(cnpj):
    novo_cnpj = cnpj[:-2]
    primeiro_digito = firstDigit(cnpj)
    novo_cnpj += primeiro_digito
    novo_cnpj = remover_caracteres(novo_cnpj)

    count = 6
    soma_calculo = 0
    
    for numero in novo_cnpj:
        numero = int(numero)
        calculo = numero * count
        soma_calculo += calculo
        count -= 1
        if count < 2:
            count = 9
            
    segundo_digito = fórmula(soma_calculo)
    if segundo_digito > 9:
        segundo_digito = 0
    
    return str(segundo_digito)


def new_cnpj(cnpj):
    primeiro_digito = firstDigit(cnpj)
    segundo_digito = secondDigit(cnpj)
    novo_cnpj = cnpj[:-2]
    novo_cnpj += primeiro_digito + segundo_digito
    if verificar_seq(cnpj):
        return False
    return novo_cnpj

def gera_cnpj():
    primeiro_digito = random.randint(0,9)
    segundo_digito = random.randint(0,9)
    segundo_bloco = random.randint(100, 999)
    terceiro_bloco = random.randint(100, 999)
    quarto_bloco = '0001'
    
    inicio_cnpj = f'{primeiro_digito}{segundo_digito}.{segundo_bloco}.{terceiro_bloco}/{quarto_bloco}-00'
    cnpj_gerado = new_cnpj(inicio_cnpj)
    clipboard.copy(cnpj_gerado)
    return cnpj_gerado