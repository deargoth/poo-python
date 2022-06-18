# logged_user = True
# msg = 'Usuário está logado.' if logged_user else 'Usuário precisa logar.'
# print(msg)

try:
    idade = int(input('Qual a sua idade? '))
except ValueError:
    print('Você não digitou um número :(')
    
msg = 'Você está liberado!' if (idade >= 18) else 'Você não está liberado.'
print(msg) 