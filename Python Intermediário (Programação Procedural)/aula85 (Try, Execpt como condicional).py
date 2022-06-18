def convertendo(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass

while True:
    número = convertendo(input('Digite um número: '))

    if número is not None:
        print(número * 2)
    else:
        print('Isso não é um número.')