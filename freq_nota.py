# calcular frequencia  e  nota do  aluno para aprovação
from os import system
system('cls')
freq = float(input('digite sua frequencia: '))
nota = float(input('digite sua nota: '))

if freq>= 75:
    print(f'Sua frenquência é {freq}')
elif nota >=6:
    print (f'Sua nota é {nota}, Aprovado' )
else:
    (print(f'Sua frequencia é {freq} e sua nota é {nota}, Reprovado'))

# segundo metodo

from os import system
system('cls')
freq = float(input('digite sua frequencia: '))
nota = float(input('digite sua nota: '))
if freq>= 75:
    print(f'sua frequência {freq}')
elif nota>=6:
    print (f'Sua nota é {nota}')
    print (f' frenquência:{freq} \n nota: {nota} \n situação: Aprovado' )
else:
    (print(f'Sua frequencia é {freq} e sua nota é {nota}, Reprovado'))
