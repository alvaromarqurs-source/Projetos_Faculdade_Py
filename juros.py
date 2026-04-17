#juros  nas parcelas
from os import system
system('cls')
valor = float(input('digite o valor da compra:'))
qt_parcelas = (int(input('qual a opção de parcelamento 2 | 4 | 6 | 8 :')))
if qt_parcelas == 2:
    	juro = 3
elif qt_parcelas == 4:
        juro = 7
elif qt_parcelas == 6:
        juro = 9
elif qt_parcelas == 8:
        juro = 12
else:
    	juro = -1
if juro < 0:
    print('Opção invalida! Tente novamente...')
else:
    valor = valor + valor * juro/100
    parcela = valor / qt_parcelas
    print (f'Valor total R${valor:.2f}\n{qt_parcelas} de R${parcela:.2f}')