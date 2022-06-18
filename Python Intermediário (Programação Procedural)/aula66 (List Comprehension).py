l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [variavel for variavel in l1]

ex2 = [variavel * 2 for variavel in l1]

l2= ['Mauro', 'Vinícius', 'Julia']
ex3 = [valor.replace('a', '@') for valor in l2]

tupla = (
    ('valor', 'chave'),
    ('valor2', 'chave2')
)

ex5 = [(v, c) for v, c in tupla]
ex5 = dict(ex5)

l3 = list(range(100))
ex6 = [valor for valor in l3 if valor % 3 == 0 if valor % 8 == 0]
ex7 = [valor if valor % 3 == 0 else 'Não é' for valor in l3]
print(ex7)