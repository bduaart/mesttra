fatAnterior = float(input('Digite o valor do faturamento anterior: '))
print('\n=== Código dos Produtos === \nProduto 1: 101\nProduto 2: 122\nProduto 3: 163')
prod = int(input('Digite o código do produto que se deseja bater a meta: '))

if prod != 101 and prod != 122 and prod != 163:
    print('Código de produto não encontrado!')
    quit()

meta = fatAnterior * 1.20
aumento = meta-fatAnterior
print(f'A meta do próximo mês é: R$ {meta:.2f}\n'
+ f'Um aumento de R$ {aumento:.2f}\n'
+ 'Quantidade de peças a serem vendidas para antigirmos a meta:\n')

if prod == 101:
    print(f'Produto 1: {aumento/150:.2f}')
elif prod == 122:
    print(f'Produto 2: {aumento/220:.2f}')
else:
    print(f'Produto 3: {aumento/97:.2f}')