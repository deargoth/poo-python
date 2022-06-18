class Computador:

    def __init__(self, marca):
        self.__marca = marca
        self.__ferramenta = None

    # Getter
    @property
    def marca(self):
        return self.__marca

    # Getter
    @property
    def ferramenta(self):
        return self.__ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


    def rodar_vscode(self):
        print('O computador está rodando VSCode.')


class Teclado:
    def __init__(self, marca):
        self.__marca = marca
    
    #Getter
    @property
    def marca(self):
        return self.__marca
    
    def escrever(self):
        print('O teclado está escrevendo...')