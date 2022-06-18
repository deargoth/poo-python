# dicionário = {'k1': 'Olá, Vinícius',
#               'k2': 'Eae, Carlos.',
#               'k3': 'Salve Leandro!.'}

# print(dicionário['k3'])

# dicionário = dict(k1='Olá, Vinícius', k2='Eae, Carlos.', k3='Salve Leandro!')

# chave = dicionário.get('k3')
# if chave == None:
#     print("Não há a chave 'k3' no seu dict, porém iremos criá-la.")
#     dicionário['k3'] = 'Without value.' 
    
# dicionário.update({'k1': 'Novo Valor.'})
# print(dicionário['k1'])

# print('k2' in dicionário.keys())
# print('Eae, Carlos.' in dicionário.values())

# print(len(dicionário))

# for keys, values in dicionário.items():
#     print(f"{keys}: {values}")


# clientes = {
#     'firstClient': {
#         'nome': 'Vinícius',
#         'sobrenome': 'Eugênio',
#     },
#     'secondClient': {
#         'nome': 'Adriana',
#         'sobrenome': 'Clark',
#     },
#     'thirtyClient': {
#         'nome': 'Alberto',
#         'sobrenome': 'Ferreira',
#         'idade': 30,
#     }
# }

# for keysClients, valuesClients in clientes.items():
#     print(f"Exibindo '{keysClients}':")
#     for clientDados, responseDados in valuesClients.items():
#         print(f'\t{clientDados} = {responseDados}')


dicionário = {1: 'a', 2: 'b', 3: 'c', 'd': ['Luiz', 'Otávio']}
dicionário2 = {
    'a': 'b',
    'c': 'd',
    'e': 'f',
}
# dicionário.popitem()
dicionário.update(dicionário2)
print(dicionário)
