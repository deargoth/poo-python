name = input('Digite o seu primeiro nome: ')

sizeName = len(name)
if sizeName <= 4:
    print('Seu nome é curto.')
elif sizeName > 6:
    print('Seu nome é muito grande.')
else:
    print('Seu nome é normal.')