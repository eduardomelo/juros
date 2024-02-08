from decimal import Decimal

JUROS= 1.03
APORTE_MENSAL = 100

meses_investindo = 120

saldo_inicial = 0

saldo_atual = 0
saldo_sem_juros = 0

diferenca = 0

mes = 1

print('#################################')
print(f'||| Taxa de juros de {JUROS} ao mês, aplicada durante {meses_investindo} mêses || ({meses_investindo / 12} anos)|||')
print(f'### Valor depositado por mês {APORTE_MENSAL}, começando com {saldo_inicial} de saldo ###')
print('#################################')
while mes <= meses_investindo:
    saldo_atual = round((saldo_atual * JUROS) + APORTE_MENSAL)
    saldo_sem_juros = saldo_sem_juros + APORTE_MENSAL

    diferenca = saldo_atual - saldo_sem_juros

    #print(f'|{mes}: {saldo_atual}' + f' | saldo sem juros :: {saldo_sem_juros}' + f' | diferença: {diferenca}')

    mes+=1

print(f'|{mes -1}: {Decimal(saldo_atual)}' + f' | saldo sem juros :: {saldo_sem_juros}' + f' | diferença: {diferenca}')