from time import sleep

def criar_tarefas():
    nova_tarefa = input('\nDigite sua nova tarefa: ').strip()
    if nova_tarefa not in lista:
        tarefas = lista.append(nova_tarefa)
        print(f'Criando a tarefa "{nova_tarefa}"')
    else:
        print(f'A tarefa "{nova_tarefa}" já existe.')

def listar_tarefas():
    print(f'\nSua lista de tarefas atual é {lista}')

def desfazer_tarefa():
    try:
        print(f'\nRemovendo item "{lista[-1]}" da lista de tarefas.')
        apagados.append(lista[-1])
        lista.pop()
    except IndexError:
        print('Não há mais valores para desfazer.')

def refazer_tarefa():
    try:
        print(f'Refazendo a tarefa {apagados[-1]}')
        lista.append(apagados[-1])
        apagados.pop()
    except IndexError:
        print('Não há mais itens para refazer.')

def organizar_lista():
    if len(lista) >= 1:
        lista.sort()
        print('Sua lista foi organizada.')
    else:
        print('Não há itens para organizar no momento.')

def salvar_sair():
    with open('lista_de_tarefas.txt', 'w+') as file:
        for enumerador, itens in enumerate(lista):
            file.write(f'Tarefa {enumerador+1}: {itens}\n')
    print('Seu arquivo foi salvo e o programa será finalizado. Obrigado!')


lista = []
apagados = []

while True:
    print('\n[1] Adicionar tarefa\n[2] Listar tarefas\n[3] Desfazer última tarefa\n[4] Refazer última tarefa\n[5] Organizar a lista (A-Z)\n[6] Salvar lista e sair')
    opção_tarefas = input('O que você quer fazer? ').strip()

    while opção_tarefas not in ['1', '2', '3', '4', '5', '6']:
        print('Opção inválida.')
        opção_tarefas = input('O que você quer fazer? ').strip()
        
    if opção_tarefas in '1': 
        criar_tarefas()
        sleep(0.9)
    
    if opção_tarefas in '2':
        listar_tarefas()
        sleep(1.4)
        
    if opção_tarefas in '3':
        desfazer_tarefa()
        sleep(0.9)
        
    if opção_tarefas in '4':
        refazer_tarefa()
        sleep(0.9)
        
    if opção_tarefas in '5':
        organizar_lista()
        sleep(0.9)
        

    if opção_tarefas in '6':
        salvar_sair()
        break
