#calculadora 2
def media(num1,num2):
    return (num1 + num2)/2
def diferença(num1,num2):
    if num1 < num2: 
        return num2 - num1
    else: 
        return num1 - num2
def produto(num1,num2):
        return num1 * num2
def div(num1,num2):
    if num2==0:
        print('Não é possivel dividir por 0')
    else:
        print(f'A divisão é {num1/num2}')
while True:
    print('[1] Média\n[2] Difereça entre o maior e o menor')
    print('[3] Produto\n[2] Divisão do primeiro pelo segundo')
    print('[5] saor')
    op = int(input('Digite uma opção'))
    if op == 5: break
num1 = float(input('Digite o priemiro número'))
num2 = float(input('Digite o segundo número'))
match op:
    case 1:(f'A media dos numeros é{media(num1,num2)}')
    case 2:(f'A diferença entre os numeros é {diferença(num1,num2)}')
    case 3:(f'O produto entre os numeros é{produto(num1,num2)} ')
    case 4: div(num1,num2)
    case _:print('opção invalida')