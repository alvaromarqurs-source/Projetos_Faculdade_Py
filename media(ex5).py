alunos =[]

x = int(input('Digite a quantidade de alunos:'))
for i in range(x):
    nome = input(f'Digite o nome do {i+1}:').capitalize()
    n1 = float(input(f'Digite a 1° nota do aluno{nome}:'))
    n2 = float(input(f'Digite a 2° nota do aluno{nome}:'))
    media =(n1+n2)/ 2
    alunos.append((nome,media))

print(10,'-')
while True:
    n = int(input('Digite o n° do aluno que deseja:')) 
    if n>=0 and n<len(alunos):
        break
result = 'Aprovado' if alunos[n][1] >= 6.0 else 'Reprovado'
print(f'O aluno{alunos[n][0]} foi {result} com media {alunos[n][1]:.2f}')   
