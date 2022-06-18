def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista

clientes1 = lista_de_clientes(['João', 'Maria', 'Gustavo'])
clientes2 = lista_de_clientes(['Gustavo', 'Leo', 'Joao'])

print(clientes1)
print(clientes2)
