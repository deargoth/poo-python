from itertools import count

contador = count()

nomes = [
    'Vinicius',
    'Julia',
    'Daysehe',
    'Leozin',
]

lista = zip(contador, nomes)
print(list(lista))