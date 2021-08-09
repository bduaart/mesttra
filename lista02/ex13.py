qtdFrangos = int(input('Digite a quantidade de frangos'))
valorAli = float(input('Digite o valor do chip de alimentação: R$'))
valorId = float(input('Digite o valor do chip de identificação: R$'))

print(f'O valor total para identificar os frangos é: \nChip alimentação: R${valorAli*qtdFrangos*2:.2f}'
+ f'\nChip Identificação: R${valorId*qtdFrangos:.2f}')
if valorId > valorAli:
    if valorId - valorAli <= (20*valorId)/100:
        print(f'A quantidade do chip de alimentação sofreu aumento de 20% de {qtdFrangos*2} unidades para {qtdFrangos*2*1.20} unidades')
        print(f'Adicional de 20%: R${(valorAli*qtdFrangos*2*1.20)-valorAli*qtdFrangos*2}')
        print(f'Valor total: R${valorId*qtdFrangos + valorAli*qtdFrangos*2*1.20}') 
    else:
        print(f'Valor total: R${valorAli*qtdFrangos*2 + valorId*qtdFrangos}')
elif valorAli > valorId:
    if valorAli - valorId <= (20*valorAli)/100:
        print(f'A quantidade do chip de identificação sofreu aumento de 20% de {qtdFrangos} unidades para {qtdFrangos*1.20} unidades')
        print(f'Adicional de 20%: R${(valorId*qtdFrangos*1.20)-valorId*qtdFrangos}')
        print(f'Valor total: R${valorAli*qtdFrangos*2 + valorId*qtdFrangos*1.20}')     
    else:
        print(f'Valor total: R${valorAli*qtdFrangos*2 + valorId*qtdFrangos}')
else:
        print(f'Valor total: R${valorAli*qtdFrangos*2 + valorId*qtdFrangos}')