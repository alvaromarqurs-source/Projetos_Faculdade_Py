nomes =[]
notas =[]
x = int(input('Digite a quantidade de alunos:'))
for i in range(x):
    nome = input(f'Digite o nome do {i+1}:').capitalize()
    nota = float(input(f'Digite a nota do aluno{nome}:'))

    nomes.append(nomes)
    notas.append(nota)

while True:
    n = int(input(f'Digite o indice do aluno(0 - {x-1}):'))
    if n>=0 and n<(x-1):
        break
    else:
        print('Digite um valor válido')
        
print(f'A nota do aluno {nomes[n]} é {notas[n]}')

nome = input('Digite o nome do aluno:')
if nome in nomes:
    indice = nomes.index(nome)
    print (f'A  nota do aluno{nomes[indice]} é {notas[indice]}')
else:
    print('Aluno não encontrado')
