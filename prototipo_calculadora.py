import contas

print('[1]soma')
print('[2]subtração')
print('[3]multiplicação')
print('[4]divisao')
print('[0] sair')


n1 = float(input('digite o primeiro numero:'))
n2 = float(input('digite o segundo numero:'))

print(f'{n1}+{n2} = {contas.soma(n1,n2)}')
print(f'{n1}+{n2} = {contas.subtracao(n1,n2)}')
print(f'{n1}+{n2} = {contas.multiplicacao(n1,n2)}')
print(f'{n1}+{n2} = {contas.divisao(n1,n2)}')
