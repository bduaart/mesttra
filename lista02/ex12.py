qtdLts = int(input('Digite a QTD de lts de suco necessário: '))
percAgua = int(input('Digite o percentual (%) de concentração de água: '))
percSuco = int(input('Digite o percentual (%) de concentração de suco: '))

if percAgua + percSuco != 100:
    q = str(input('Os valores de concentração não totalizam 100%.\nVocê deseja enquadrar os valores em percentual? (s/n)'))
    if q != 's':
        print('Valores de concentração incorretos. Processo finalizado!')
    else:
        percAgua = percAgua/(percAgua + percSuco) * 100
        percSuco = percSuco/(percAgua + percSuco) * 100
        print(f'Novo percentual do suco: {percSuco:.2f}')
        print(f'Novo percentual de água: {percAgua:.2f}')

print(f'Será necessário para fazer {qtdLts} lts suco de maracujá:\n'
+ f'{qtdLts*(percAgua/100):.2f} lts de água e {qtdLts*(percSuco/100):.2f} lts de suco concentrado de maracujá')
