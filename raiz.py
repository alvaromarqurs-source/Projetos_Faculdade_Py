#raiz com bliblioteca Math
import math
numero = float(input('Digite um numero positivo: '))
raiz = math.sqrt(numero)
if numero >=0:
    print(f" a raiz do numero {numero} é {raiz:.2f}")
else:
    print(f'o numero {numero} é negativo, digite um numero positivo')
