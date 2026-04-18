#media de numeros com range
soma = 0
n = int(input('Digite a quantidade de números:'))
for i in range(n):
    num = float(input(f'Digite o {i+1}° número: '))
    soma += num 
    media = soma/n
    print(f"A média dos numeros é: {media:.2f}")
