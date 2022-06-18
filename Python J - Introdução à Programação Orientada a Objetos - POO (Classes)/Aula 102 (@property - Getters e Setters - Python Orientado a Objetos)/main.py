from produto import Produto

produto1 = Produto('cALCulaDORA', 'R$15')
produto1.desconto(10)

produto2 = Produto('CAlcinha', 'PR45')
produto1.desconto(10)

print(produto1.nome, produto1.preço)
print(produto2.nome, produto2.preço)