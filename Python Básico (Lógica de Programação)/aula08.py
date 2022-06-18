nome = 'Vinícius'
idade = 16
altura = 1.78
peso = 60.1
ano = 2022
imc = peso / altura ** 2
nascimento = ano - idade

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg. \nO IMC de {nome} é de {imc:.2f}. \n{nome} nasceu em {nascimento}.')