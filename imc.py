#IMC
def metodo_imc(peso,altura):
    return peso/altura **2
peso = float(input("qual é seu peso: "))
altura = float(input('qual é sua altura:'))

print(f' seu Imc é: {metodo_imc(peso,altura):.2f}')