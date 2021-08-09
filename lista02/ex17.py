qtdSand = int(input(f'Digite a quantidade de sanduíches: '))
qtdPres = (50*qtdSand)

print(f'Para produzir {qtdSand} sanduíches serão necessários: \n'
+ f'{(100*qtdSand):.2f} Kgs de mussarela\n'
+ f'{qtdPres:.2f} Kgs de presunto\n'
+ f'{(120*qtdSand):.2f} Kgs de hambúrguer')

dispPres = float(input('Qual a quantidade em Kgs disponível de presunto?: '))
if dispPres >= qtdPres:
    quit()
else:
    print(f'Será possível produzir apenas {int(dispPres/50)} sanduíches com presunto')
    print(f'Será necessário {int(90*(qtdSand- dispPres/50))/1000:.3f} kgs de mortadela para produzir {int(qtdSand- dispPres/50)} sanduíches restantes.')
    print(f'Da quantidade de presunto disponível sobrará {((dispPres/50)*50-(dispPres/50)*50):.3f} kgs')