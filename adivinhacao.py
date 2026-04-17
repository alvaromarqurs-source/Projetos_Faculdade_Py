#jogo de adivinhação
from random import randint
from time import time
from os import system 

def play ():
    num_sorte = randint(0,100)
    tentativas = 0
    inicio = time()
    system('cls')
    while True:
        chute = int(input('Digite um numero inteiro: '))
        if chute < num_sorte:
            print('# o numero sorteado é maior')
        elif chute > num_sorte:
            print(' o nuemro sorteado é menor')
        else:
                fim = time()
                tempo = fim - inicio
                print(f'Parabéns # você acertou em {tentativas} tentativas')
                print(f'tempo gasto {tempo:.1f} segundos')
                input('Enter para encerrar.....')
        break
    tentativas +=1
while True:
    play()
    resp = input('Deseja jogar novamente? s/n')
    if resp in 'nN': 
         break 