lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]


listas = list(zip(lista_a, lista_b))

count = 0
lista_soma = [a + b for a, b in listas]
print(f'{lista_a}\n{lista_b}\n')
print(lista_soma)