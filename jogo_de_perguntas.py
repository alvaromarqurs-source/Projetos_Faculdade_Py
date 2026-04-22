contador = 0 
resp = input('1- telefonou para vítima? ')
if resp in 'sS':
    contador +=1
resp = input('2- Esteve no local do crime? ')
if resp in 'sS':
    contador +=1
resp = input('3- Mora perto da vitima?')
if resp in 'sS':
    contador +=1
resp = input('4- Devia $$ para a vitima?')
if resp in 'sS':
    contador +=1
resp = input('5- Já trabalhou com a vitima?')
if resp in 'sS':
    contador +=1

if contador == 2:
    print('Suspeito')
elif contador == 3 or contador == 4:
    print('Cumplice')
elif contador == 5:
    print('Assasino')
else:
    print('Inocente')
