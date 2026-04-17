#decimal bara binario
num = int(input('Digite um número decimal: '))
binario = ''
while num >0:
    dig = num%2
    binario = str(dig) + binario
    num = num/2
print(f'O decimal{num} equivale ao binário{binario} ')