from aula80 import produtos, pessoas, lista


def filtraPessoas(p):
    if p['idade'] >= 18:
        return True
    else:
        return False
# pessoas.sort(key = lambda item: item['idade'])
idades_filtradas = filter(lambda item: item['idade'] >= 18, pessoas)
# idades_filtradas = filter(filtraPessoas, pessoas)

for idades in idades_filtradas:
    print(idades)