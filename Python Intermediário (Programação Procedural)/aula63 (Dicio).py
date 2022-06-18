perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {'A': '1', 'B': '4', 'C': '8', 'D': '2'},
        'certaResposta': 'B',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 4x4? ',
        'respostas': {'A': '1', 'B': '4', 'C': '16', 'D': '2'},
        'certaResposta': 'C',
    }
}
countCertain = 0
for chavesPer, dadosRes in perguntas.items():
    print(f'{chavesPer}: {dadosRes["pergunta"]}')
    print(f'   Respostas:')
    for indexRes, resposta in dadosRes['respostas'].items():
        print(f'\t[{indexRes}]: {resposta}')
    respostaUser = input('Sua resposta é: ').upper().strip()
    if respostaUser[0] == dadosRes['certaResposta']:
        print('Você acertou!')
        countCertain =+ 1
        print()
    else:
        print('Você errou!! =(')
    print()
print(f'Nossas perguntas acabaram!! \nVocê acertou {countCertain} perguntas!')