from random import randint

cpfUser = str(randint(100000000, 999999999))
print()

while len(cpfUser) > 11 or not cpfUser.isnumeric():
    print('CPF inválido! Digite novamente.')
    cpfUser = input('CPF: ')

novoCpf = cpfUser
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

print(novoCpf)

#Formatar o CPF
listLetras = []
formatedCpf = ''
countLetra = 0
count = 0

for letra in novoCpf:
    listLetras.append(letra)
for num in listLetras:
    formatedCpf += num
    countLetra += 1
    if countLetra % 3 == 0:
        formatedCpf += '.'

string = formatedCpf
newCpf = formatedCpf[:11] + '-' + formatedCpf[12:]
print(f'O seu CPF formatado é {newCpf}')
