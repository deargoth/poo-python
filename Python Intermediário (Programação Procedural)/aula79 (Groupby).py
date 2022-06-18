from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Vini', 'nota': 'B'},
    {'nome': 'Dayse', 'nota': 'B'},
    {'nome': 'Leticia', 'nota': 'A'},
    {'nome': 'Fábio', 'nota': 'D'},
    {'nome': 'Rose', 'nota': 'C'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'A'},
    {'nome': 'Lorraine', 'nota': 'C'},
    {'nome': 'José', 'nota': 'C'},
    {'nome': 'Aldo', 'nota': 'B'},
]

ordenar = lambda item: item['nota']
alunos.sort(key=ordenar)
agrupando = groupby(alunos, ordenar)

for agrupamento, valorAgrupado in agrupando:
    print(f'Agrupamento {agrupamento}:')
    for alunos in valorAgrupado:
        print(f"\tNome: {alunos['nome']}")
        print(f"\tNota: {alunos['nota']}")
    print()