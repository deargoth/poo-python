# Exercício 1

def saudação(msg = 'Hello', name = 'usuário'):
    print(msg, name)
# saudação('Oi', 'mundo')

'----' 

# Exercício 2
def soma(n1, n2, n3):
    return n1+n2+n3
printar = soma(3,3,3)
# print(printar)

'----'

# Exercício 3

def percentual(n1, n2):
    porcento = (n2 / 100)
    somar = n1 + (n1 * porcento)
    return somar
# print(percentual(100,50))

def fizzbuzz(var):
    if var == 0:
        return 0
    if var % 5 == 0 and var % 3 == 0:
        return 'FizzBuzz'
    if var % 3 == 0:
        return 'Fizz'
    if var % 5 == 0:
        return 'Buzz'
    return var