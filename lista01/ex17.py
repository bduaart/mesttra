qtdSand = int(input(f'Digite a quantidade de sanduíches: '))

print(f'Para produzir {qtdSand} sanduíches serão necessários: \n'
+ f'{(100*qtdSand)/1000:.2f} Kgs de mussarela\n'
+ f'{(50*qtdSand)/1000:.2f} Kgs de presunto\n'
+ f'{(120*qtdSand)/1000:.2f} Kgs de hambúrguer')
