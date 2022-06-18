import re

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)
    
    def listar_produtos(self):
        for produto in self.produtos:
            print(f'Nome: {produto.nome} | Preço: R${produto.preço}')
    
    
    @property
    def preço(self):
        return self._produtos
    
    @preço.setter
    def preço(self, valor):
        for produto in self.produtos:
            valor = re.sub(r'[^0-9]', '', produto.preço)

        return valor
    
    def soma_total(self):
        total = 0
        nomes = []

        for produto in self.produtos:
            total += produto.preço
            nomes.append(produto.nome)
        print(f"A soma total de seus {len(self.produtos)} produtos é de R${total}")


class Produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço