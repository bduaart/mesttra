paoVend = int(input('Digite a quantidade de pães vendidos: '))
broasVend = int(input('Digite a quantidade de broas vendidos: '))
reforma = int(input('Digite o valor da reforma: '))

totalBroas = broasVend * 1.50
totalPaes = paoVend * 0.12
totalVenda = totalPaes+totalBroas
poupança = totalVenda/10

print(f'Faturamento com a venda de broas: {totalBroas:.2f}\n'
+ f'Faturamento com a venda de pães: {totalPaes:.2f}\n'
+ f'Faturamento diário (pães + broas): {totalVenda:.2f}\n' 
+ f'Valor do depósito na poupança {poupança:.2f}\n'
+ f'Para pagar a reforma serão necessários: {int(reforma/poupança)}')
