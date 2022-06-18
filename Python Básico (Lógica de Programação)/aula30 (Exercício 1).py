number = input('Digite um número inteiro: ')

if number.isnumeric():
    number = int(number)
    if number % 2 == 0:
        print('É par!')
    else:
        print('Não é par!')
else:
    print('Você não digitou um número inteiro. Rode o programa novamente')