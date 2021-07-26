qtdLts = int(input('Digite a QTD de lts de suco necessário: '))

tonel = qtdLts / 10
print(f'Será necessário para fazer {qtdLts} lts suco de maracujá:\n'
+ f'{tonel*8:.2f} lts de água e {tonel*2:.2f} lts de suco concentrado de maracujá')
