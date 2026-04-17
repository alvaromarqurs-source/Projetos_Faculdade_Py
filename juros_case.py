#juros  das  parcelas com case
from os import system
system('cls')
valor = float(input('digite o valor da compra:'))
qt_parcelas = (int(input('qual a opção de parcelamento 2 | 4 | 6 | 8 :')))
match qt_parcelas:
    case 2: juro = 3
    case 4: juro = 7
    case 6: juro = 9
    case 8: juro = 12
    case _: juro = -1
if juro < 0:
    print('Opção invalida! Tente novamente...')
else:
    valor = valor + valor * juro/100
    parcela = valor / qt_parcelas
    print (f'Valor total R${valor:.2f}\n{qt_parcelas} de R${parcela:.2f}')