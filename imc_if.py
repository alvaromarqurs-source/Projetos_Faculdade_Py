#Imc  com if,elif,else
peso = int(input('digite seu peso: '))
altura = int(input('digite seu altura: '))
def imc(peso,altura):
    return( peso/altura**2)
imcc = imc(peso,altura)
if imcc <20:
    result = "abaixo do peso"
elif imcc <25:
    result = 'peso normal'
elif imcc <30:
    result = 'sobrepeso'
elif imcc <35:
    result = 'obeso morbido'
else:
    result = 'obeso mórbido'
print(f'IMC = {imcc:.2f},{result}')