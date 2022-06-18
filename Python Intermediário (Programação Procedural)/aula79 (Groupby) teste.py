from itertools import groupby

alunos = [
    {'nome': 'Vinícius', 'nota': 'C'},
    {'nome': 'Carlos', 'nota': 'A'},
    {'nome': 'Pedro', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Marcelo', 'nota': 'A'},
    {'nome': 'Larissa', 'nota': 'F'},
    {'nome': 'Daniel', 'nota': 'F'},
    {'nome': 'Yago', 'nota': 'B'},
    {'nome': 'Lucas', 'nota': 'B'},
    {'nome': 'Giovana', 'nota': 'C'},
    {'nome': 'Gertrudes', 'nota': 'A'},
    {'nome': 'Gabriel', 'nota': 'A'},   
]


ordenando = lambda item: item['nota']
alunos.sort(key=ordenando)
agrupar = groupby(alunos, ordenando)

for nota, agrupado in agrupar:
    print(f'\nAgrupamento {nota}:')
    for item in list(agrupado):
        print(f'\t{item["nome"]} | Nota: {item["nota"]}')