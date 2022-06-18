import módulos

while True:
    print('\n[1] Validar CNPJ\n[2] Gerar CNPJ\n[3] SAIR')
    opção = input('Digite "1" ou "2" ou "3": ')
    
    if opção in '1':
        cnpj = input('\nCNPJ: ').strip()
        if cnpj in '0':
            break
        novo_cnpj = módulos.new_cnpj(cnpj)
        if novo_cnpj == cnpj:
            print(f'CNPJ "{cnpj}" é válido')
        else:
            print('Inválido.')
            
    if opção in '2':
        print(f'O CPF gerado é "{módulos.gera_cnpj()}" e estará na sua área de transferência.')
    
    if opção in '3':
        print('Finalizando o programa. Obrigado por utilizar!')
        break
