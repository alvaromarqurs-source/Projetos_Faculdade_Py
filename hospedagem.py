#Tipo de Hospedagem
from os import system
system('cls')
tipo = input('Digite o tipo de hospedagem(S/D/T): ').lower()
if tipo not in 'sSdDtT':
    print('Tipo de hospedagem invalido')
else: 
    qt_d = int(input('Qual a quantidade de diárias: '))
if tipo == 's':
    print(f'Valor total R$ {qt_d*255.5}')
elif tipo == 'd': 
    print(f'Valor total R$ {qt_d*305.5}')
elif tipo == 't':
    print(f'Valor total R$ {qt_d*360.5}')
