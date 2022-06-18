# from time import sleep, time

# def velocidade(função):
#     def interna(*args, **kwargs):
#         start_time = time()
#         resultado = função(*args, **kwargs) 
#         end_time = time()
#         tempo = end_time - start_time
#         print(f'A função "{função.__name__}" demorou {round(tempo)} segundos para ser finalizada.')
#         return resultado
#     return interna

# @velocidade
# def demora():
#     for vel in range(1, 4):
#         print(vel)
#         sleep(1)

# demora()

def função_decoradora(função_decorada):
    def função_interna(*args, **kwargs):
        resultado = função_decorada(*args, **kwargs)

        try:
            resultado.append('Isso foi adicionado pelo decorador.')
        except AttributeError:
            ...

        return resultado
    return função_interna

@função_decoradora
def nome_de_clientes():
    nomes = ['Luiz', 'Maria', 'João']
    return nomes

print(nome_de_clientes())