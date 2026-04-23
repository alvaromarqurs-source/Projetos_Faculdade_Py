alunos =[]
soma = 0 

x = int(input('Digite a quantidade de alunos:'))
for i in range(x):
    nome = input(f'Digite o nome do {i+1}° aluno:').capitalize()
    nota = float(input(f'Digite a nota do aluno {nome}:'))
    alunos.append((nome,nota))
    soma +=nota
media = soma/x
print(f'A média da turma é {media:.2f} ')
print(alunos)

for nome,nota in alunos:
    if nota > media:
        print(f'Parabens {nome} sua nota está acima da média')
