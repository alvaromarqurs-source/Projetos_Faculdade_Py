#media do aluno com while
i = 1
while i <=3:
    nome = input(f'Digite o nome do {i}° aluno:')
    nota1 = float(input(f'Digite a 1° nota do {nome}:'))
    nota2 = float(input(f'Digite a 2° nota do {nome}:'))
    media = (nota1+nota2)/2
    print(f' A media do aluno {nome} é {media:.2f}') 
i+=1
