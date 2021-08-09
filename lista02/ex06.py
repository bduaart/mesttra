qtdCav = int(input('Informe a quantidade de cavalos: '))
valFerr = float(input('Informe o valor de cada ferradura: R$'))
total = (qtdCav*4) * valFerr

print(f'A quantidade de ferraduras necessárias: {qtdCav*4}')
if total >= 15000.01 and total <= 20000.0:
    print(f'Valor total para a compra das ferraduras: R${abs((total*10/100) - total):.2f}')
elif total >= 20000.01 and total <= 25000.0:
    print(f'Valor total para a compra das ferraduras: R${abs((total*12/100) - total):.2f}')
elif total >= 25000.01 and total <= 30000.0:
    print(f'Valor total para a compra das ferraduras: R${abs((total*15/100) - total):.2f}')
elif total >= 30000.01:
    print(f'Valor total para a compra das ferraduras: R${abs((total*20/100) - total):.2f}')
else:
    print(f'Valor total para a compra das ferraduras: R${total:.2f}')