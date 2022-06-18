def saudação(msg = 'Hello', nome = 'Vinícius'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    return f'{msg} {nome}'
função = saudação()
print(função)