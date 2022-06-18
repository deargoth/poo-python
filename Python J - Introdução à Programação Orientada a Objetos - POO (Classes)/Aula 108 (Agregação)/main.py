from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

produto1 = Produto('Xiaomi', 1000)
produto2 = Produto('Camiseta', 50)
produto3 = Produto('Teclado', 150)

carrinho.inserir_produto(produto1)
carrinho.inserir_produto(produto2)
carrinho.inserir_produto(produto3)
carrinho.listar_produtos()
carrinho.soma_total()