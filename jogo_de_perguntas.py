contador = 0 
perguntas = ['1- telefonou para vítima?','2- Esteve no local do crime? ',
             '3- Mora perto da vitima?','4- Devia $$ para a vitima?',
             '5- Já trabalhou com a vitima?']
for perguntas in perguntas:
    resp =input(f'{perguntas}')
    if resp in 'sS':
        contador += 1

if contador == 2:
    print('Suspeito')
elif contador == 3 or contador == 4:
    print('Cumplice')
elif contador == 5:
    print('Assasino')
else:
    print('Inocente')
