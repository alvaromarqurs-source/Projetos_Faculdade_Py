#média
import subprocess

n1 = float(input('digite um numero: '))
n2 = float(input('digite outro numero: '))
m = (n1+n2)/2
print(f'a sua média é: {m}')

#segundo modelo com Def
def media(n1,n2):
    return ((n1+n2)/2) 

n1 = float(input('digite um numero: '))
n2 = float(input('digite outro numero: '))
print(f'Média = {media(n1,n2)} ')