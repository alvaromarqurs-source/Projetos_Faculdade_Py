#Baskara
a = float(input('digite o valor de a: ' ))
b = float(input('digite o valor de b: ' ))
c = float(input('digite o valor de c: ' ))
delta = b**-4*a*c
x1 = (-b + delta**0.5 )/(2*a)
x2 = (-b - delta**0.5 )/(2*a)
print(f'O valor de X1 é: {x1:.1f}\n O valor de X2 é{x2:.1f} ')