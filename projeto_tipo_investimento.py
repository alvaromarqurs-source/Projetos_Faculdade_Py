#projeto tipo de investimento
from os import system
from datetime import datetime,timedelta
system('cls')
def montante(c,t,p):
    m = c* (1+t/100)**p
    return(m)
    
try: 
    investimento = input('Escolha o tipo de investimento (CDB ou LCI): ')
    c= float(input('Capital inical: '))
    t = float(input('taxa de juros mensal (em %): '))
    p = int(input('Quantidade de meses: '))
    

    hoje = datetime.now()
    vencimento = hoje + timedelta(days=30*p)
    
except ValueError:
    print('Entrada inválida!')
    print('Insira valores numéricos para o capital, taxa de juros e meses\n\nPressione Enter para sair....')
else:
    print('\nResumo do investimento:')
    print(f'Tipo de Investimento: {investimento}')
    print(f'Capital Inicial: {c}')
    print(f'Taxa De Juros: {t} % ao mês')
    print(f'Período: {p} meses')
    print(f'Montante: R${montante(c,t,p):_.2f}')
    print('\nDatas:')
    print (f'aplicação: {hoje.strftime('%d/%m/%Y')}')
    print(f'vencimento: {vencimento.strftime('%d/%m/%Y')}')
    print('\nPressione Enter para Sair...')
