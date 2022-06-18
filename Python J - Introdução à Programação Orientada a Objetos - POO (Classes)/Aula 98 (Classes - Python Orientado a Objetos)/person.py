class Person:
    ano_atual = 2022
    
    def __init__(self, nome, idade, falando=False, comendo=False):
        self.nome = nome
        self.idade = idade
        self.falando = falando
        self.comendo = comendo
        
    def get_name(self):
        print(f'Olá, eu sou {self.nome}!')
        
    def falar(self, assunto):
        if self.falando:
            print(f'{self.nome} já está falando algo!')
            return
        
        if self.comendo:
            print(f'{self.nome} não pode falar pois está comendo!')
            return
        
        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True
    
    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando!!')
            return

        print(f'{self.nome} parou de falar!')
        self.falando = False
    
    def comer(self, alimento):
        if self.falando:
            print(f'{self.nome} não pode comer pois está falando!')
            return
        
        print(f'{self.nome} começou a comer {alimento}')
        self.comendo = True
        
    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} já não está comendo!')
            return
        
        print(f'{self.nome} parou de comer!')
        self.comendo=False
        
    def get_ano_nascimento(self):
        birthday = self.ano_atual - self.idade
        print(f'O ano de nascimento de {self.nome} é {birthday}')
