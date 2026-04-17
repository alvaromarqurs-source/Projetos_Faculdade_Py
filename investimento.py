# Sistema de  investimento
from os import system
from datetime import datetime,timedelta
def formata_valor(valor):
    return f'R${valor:_.2f}'.replace('.',',').replace('_','.')
system('cls')
try: 
    c= float(input('Capital inical: '))
    t = float(input('taxa de juros mensal (%): '))
    p = int(input('Quantidade de meses: '))
    m = c* (1+t/100)**p
    hoje = datetime.now()
    vencimento = hoje + timedelta(days=30*p)
    print('Resumo do investimento')
    print(f'Capital Inicial: R${formata_valor(c)}')
    print(f'Taxa De Juros: {t} % ao mês')
    print(f'Período: {p} meses')
    print(f'\nMontante final {formata_valor(m)}')
    print('\nDatas')
    print (f'aplicação: {hoje.strftime('%d/%m/%Y')}')
    print(f'vencimento: {vencimento.strftime('%d/%m/%Y')}')
except ValueError:
    print('Valor Incoreto! Tente novamente........ ')
else:
    c = f'R${c:_.2f}'.replace('.',',').replace('_','.')
    m = f'R${m:_.2f}'.replace('.',',').replace('_','.')
    print('Resumo do investimento')
    print(f'Capital Inicial: R${c}')
    print(f'Taxa De Juros: {t} % ao mês')
    print(f'Período: {p} meses')
    print(f'\nMontante final {m}')
    print('\nDatas')
    print (f'aplicação: {hoje.strftime('%d/%m/%Y')}')
    print(f'vencimento: {vencimento.strftime('%d/%m/%Y')}')
