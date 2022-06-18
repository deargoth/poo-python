import json

pessoas = {
    'Pessoa 1': {
        'nome': 'Luiz',
        'idade': 32
    },
    'Pessoa 2': {
        'nome': 'Jeyza',
        'idade': 40
    }
}

pessoas_json = json.dumps(pessoas, indent=True)

with open('aula89.json', 'w+') as file:
    file.write(pessoas_json)