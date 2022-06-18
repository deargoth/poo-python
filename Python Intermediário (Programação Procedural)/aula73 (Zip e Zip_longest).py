from itertools import zip_longest, count

index = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']

cidade_estados = zip(index, cidades, estados)

for index, cidades, estados in cidade_estados:
    print(f'[{index}] Cidade: {cidades} - {estados}')