print('Digite o seu CPF abaixo. \nDigite sem nenhum tipo de pontuação.')
cpfUser = input('CPF: ')
print()

while len(cpfUser) > 11 or not cpfUser.isnumeric():
    print('CPF inválido! Digite novamente.')
    cpfUser = input('CPF: ')

novoCpf = cpfUser[:-2]
count = 10
valores = []
    
# Verificar primeiro digito
for valide in novoCpf:
    inteiro = int(valide)
    conta = inteiro * count
    valores.append(conta)
    count -= 1
    if count < 2:   
        break
sumList = sum(valores)
conta = 11 - (sumList % 11)
if conta > 9:
    firstDigit = 0
elif conta <= 9:
    firstDigit = conta
novoCpf += str(firstDigit)

#Verificar segundo digito:
count = 11
valores = []

for valide in novoCpf:
    inteiro = int(valide)
    conta = inteiro * count
    valores.append(conta)
    count -= 1
    if count < 2:
        break
sumList = sum(valores)
conta = 11 - (sumList % 11)
if conta > 9:
    secondDigit = 0
elif conta <= 9:
    secondDigit = conta
novoCpf += str(secondDigit)

if novoCpf == cpfUser:
    print('CPF Válido.')
else:
    print('Inválido.')
    
#Formatar o CPF
listLetras = []
novoCpf = ''
countLetra = 0
count = 0

for letra in cpfUser:
    listLetras.append(letra)
for num in listLetras:
    novoCpf += num
    countLetra += 1
    if countLetra % 3 == 0:
        novoCpf += '.'

string = novoCpf
newCpf = novoCpf[:11] + '-' + novoCpf[12:]
print(f'O seu CPF formatado é {newCpf}')
