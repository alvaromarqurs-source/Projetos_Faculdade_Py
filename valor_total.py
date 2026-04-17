#Valor Total
valor = float(input('Digite o seu R$'))
comissao = valor*(10/100)
valor += comissao
print(f'valor total R${valor:.2f}')