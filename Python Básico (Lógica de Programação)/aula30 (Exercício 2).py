hour = input('Digite o horário atual [0 - 23]: ')

if hour.isdigit():
    hour = int(hour)
    if hour < 0 or hour > 23:
        print('Horário deve estar entre 0-23!')
    if hour <= 11:
        print('Bom dia!')
    elif 12 <= hour <= 17:
        print('Boa tarde!')
    elif 18 <= hour <= 23:
        print('Boa noite!')
else:
    print('Você não digitou um horário. Tente novamente')
    
    