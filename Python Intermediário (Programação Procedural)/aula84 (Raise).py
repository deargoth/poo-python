def dividindo(n1, n2):
    try:
        return n1/n2
    except ZeroDivisionError as error:
        print(error)
        raise ZeroDivisionError('Não é possível dividir um número por 0.')
print(dividindo(2,0))