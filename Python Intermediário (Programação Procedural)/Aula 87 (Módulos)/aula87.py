import math

PI = math.pi

def dobraLista(lista):
    return [x * 2 for x in lista]

def multiplicaLista(lista):
    multiplicado = 1
    for value in lista:
        multiplicado *= value
    return multiplicado    

if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]
    print(dobraLista(lista))
    print(multiplicaLista(lista))