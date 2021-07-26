qtdCavalos = int(input('Informe a quantidade de cavalos: '))
valFerradura = float(input('Informe o valor de cada ferradura: R$'))

totFerradura = qtdCavalos*4
print(f'Quantidade de ferraduras necessárias: {totFerradura}')
print(f'Valor total para a compra das ferraduras: R$ {(totFerradura*valFerradura)}')