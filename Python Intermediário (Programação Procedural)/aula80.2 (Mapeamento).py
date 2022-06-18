from aula80 import produtos, pessoas, lista

# for pessoa in pessoas:
#     print(pessoa)

novo_dic = map(lambda nome: nome['nome'], pessoas)
for enumerador, nome in enumerate(novo_dic):
    print(f'O nome {enumerador} é {nome}')