#numero ao quadrado
import subprocess

def dobro(a):
    a = a*a
    return a 
a = int(input('Digite o valor de a: '))
print(f'valor de a antes do metodo é {a}')
a = dobro(a)
print(f'valor de a depois do metodo é:{a}')