class BaseDeDados:

    def __init__(self):
        self.__dados = {}

    
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})
        print(f'O cliente "{id} - {nome}" foi adicionado em nossa base de dados.')

        
    def listar_clientes(self):

        if not self.__dados:
            print('listar_clientes: Não há clientes a serem listados!')
            return

        for id, nome in self.__dados['clientes'].items():
            print(f'Cliente {id}: {nome}')

    def remover_cliente(self, id):
        if id not in self.__dados['clientes'].keys():
            print('remover_cliente: O ID informado não existe ou já foi retirado de nossa base de dados.')
        else:
            del self.__dados['clientes'][id]
            print(f'O cliente do "ID {id}" foi removido de nossa base de dados.')

            


bd = BaseDeDados()
bd.listar_clientes()
bd.inserir_cliente(1, 'Cláudio')
bd.inserir_cliente(2, 'Ronaldo')
bd.inserir_cliente(3, 'Júlio')
bd.listar_clientes()
