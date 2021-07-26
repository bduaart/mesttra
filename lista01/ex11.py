anoNasc = int(input('Digite o ano de nascimento'))
anoAtual = int(input('Digite o ano atual'))

print(f'A idade desta pessoa é {anoAtual - anoNasc} anos, {(anoAtual - anoNasc) * 12} meses, '
    + f'{(anoAtual - anoNasc) * 48} semanas e {(anoAtual - anoNasc) * 365} dias ')
