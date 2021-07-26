fatAnterior = float(input('Digite o valor do faturamento anterior: '))
meta = fatAnterior * 1.20
aumento = meta-fatAnterior
print(f'A meta do próximo mês é: R$ {meta:.2f}\n'
+ f'Um aumento de R$ {aumento:.2f}\n'
+ 'Quantidade de peças a serem vendidas para antigirmos a meta:\n')

print(f'Produto 1: {aumento/150:.2f}')
print(f'Produto 2: {aumento/220:.2f}')
print(f'Produto 3: {aumento/97:.2f}')