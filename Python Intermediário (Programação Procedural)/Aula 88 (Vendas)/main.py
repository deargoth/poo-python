from vendas.calc_preço import aumento, redução
from vendas.formata import preço

produto = 49.90
preço_com_aumento = aumento(valor = produto, porcentagem = 15, formata=True)
print(preço_com_aumento)

preço_com_redução = redução(valor = produto, porcentagem = 15, formata=True)
print(preço_com_redução)