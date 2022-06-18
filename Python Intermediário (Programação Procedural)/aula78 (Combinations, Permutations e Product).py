from itertools import combinations, permutations, product

pessoas = [
    'Luiz',
    'Otávio',
    'Fernanda',
    'Dayse',
    'Gabriel',
    'Salvatore' 
]

for grupo in product(pessoas, repeat=2):
    print(grupo)