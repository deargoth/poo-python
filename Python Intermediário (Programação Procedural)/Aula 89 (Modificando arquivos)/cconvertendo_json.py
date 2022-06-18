#     print(chave)
# import json

# with open('aula89.json', 'r') as file:
#     pessoas_json = file.read()
#     pessoas_json = json.loads(pessoas_json)

# print(pessoas_json)
# for chave, valor in pessoas_json.items():
#     for key, value in valor.items():
#         print(f'\t{key} = {value}')
#     print()

import json

with open('aula89.json', 'r') as file:
    dicionario_json = file.read()
    dicionario_json = json.loads(dicionario_json)
    
print(dicionario_json)

for key, value in dicionario_json.items():
    print(f'{key}:')
    for chave, valor in value.items():
        print(f'\t{chave}: {valor}')