from decimal import Decimal

JUROS: float = 1.03
APORTE_MENSAL: float = 100

meses_investindo: int = 120

saldo_inicial: float = 0

saldo_atual: float = 0
saldo_sem_juros: float = 0

diferenca: float = 0

mes: int = 1

print('#################################')
print(f'||| Taxa de juros de {JUROS} ao mês, aplicada durante '
      f'{meses_investindo} mêses || ({meses_investindo / 12} anos)|||')
print(f'### Valor depositado por mês {APORTE_MENSAL}, começando com {saldo_inicial} de saldo ###')
print('#################################')
while mes <= meses_investindo:
    saldo_atual = round((saldo_atual * JUROS) + APORTE_MENSAL)
    saldo_sem_juros = saldo_sem_juros + APORTE_MENSAL

    diferenca = saldo_atual - saldo_sem_juros
#
    print(f'Mês|{mes}: Saldo com júros: {saldo_atual}' + f' | saldo sem juros : {saldo_sem_juros}' + f' | soma dos juros: {diferenca}')
#
    mes += 1

print(f' Total | Com júros {mes -1}: R${Decimal(saldo_atual)}' + f' | sem juros: R${saldo_sem_juros}' + f' | soma dos júros : R${diferenca} |')
