paoVend = int(input('Digite a quantidade de pães vendidos: '))
broasVend = int(input('Digite a quantidade de broas vendidos: '))
reforma = float(input('Digite o valor da reforma: '))

totalBroas = broasVend * 1.60
totalPaes = paoVend * 0.12
totalVenda = totalPaes+totalBroas
poupanca = totalVenda/10

print(f'Faturamento com a venda de broas: {totalBroas:.2f}\n'
+ f'Faturamento com a venda de pães: {totalPaes:.2f}\n'
+ f'Faturamento diário (pães + broas): {totalVenda:.2f}\n' 
+ f'Valor do depósito na poupança {poupanca:.2f}\n'
+ f'Para pagar a reforma serão necessários: {int(round(reforma/poupanca))} dias')

if int(reforma/poupanca > 120):
    print(f'Para realizar a reforma em 120 dias será necessário depositar diariamente R${reforma/120:.2f}')