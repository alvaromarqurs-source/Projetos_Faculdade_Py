#Rodizio  de placa
placa = int(input('Digite a placa com 8 carcteres:'))
if len(placa) > 8:
    print('Placa Invalida!')
else:
    digito = int(placa[7])
match digito:
    case 1 | 2: print('Nao pode rodar segunda-feira')
    case 3 | 4: print('Nao pode rodar terça-feira')
    case 5 | 6: print('Nao pode rodar quarta-feira')
    case 7 | 8: print('Nao pode rodar quinta-feira')
    case 9 | 0: print('Nao pode rodar sexta-feira')
    case _:print('Digito invalido')
    