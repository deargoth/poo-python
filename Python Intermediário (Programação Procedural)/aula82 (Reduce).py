from aula80 import produtos, pessoas, lista
from functools import reduce

somando_valores = reduce(lambda acumulador, item: item['preço'] + acumulador, produtos, 0)
print(somando_valores)