from pessoa import Pessoa

pessoa1 = Pessoa('Vini', 16)
pessoa2 = Pessoa.por_ano_nascimento('Vini', 2006)

print(pessoa1.idade)
pessoa1.get_ano_nascimento()
print()
print(pessoa2.idade)
pessoa2.get_ano_nascimento()
