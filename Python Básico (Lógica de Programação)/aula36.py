frase = 'o rato comeu a bunda do rei de roma'
size = len(frase)
contador = 0
new_string = ''
inputUser = input('Qual letra deseja colocar maiúscula? ').lower()
 
while contador < size:
    letra = frase[contador]
    if letra == inputUser:
        new_string += inputUser.upper()
    else:
        new_string += letra
    contador += 1
print(new_string)
