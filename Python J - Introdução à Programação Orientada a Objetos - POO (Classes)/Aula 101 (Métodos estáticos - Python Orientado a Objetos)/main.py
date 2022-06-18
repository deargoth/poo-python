from pessoa import Pessoa

pessoa1 = Pessoa.por_ano_nascimento('Vini', 2006)
print(pessoa1.idade)

print(pessoa1.gera_id())