n = int(input('Digite um número de até 4 dígitos: '))

nMilhar = n%1000
nCentena = nMilhar%100
nDezena = nCentena%10
nUnidade = nDezena%1

if n >= 9999 or n < 0:
    print('Número inválido!')
elif n < 1000 and n > 100:
    print(f'Centenas: {round((nMilhar-nCentena)/100)}')
    print(f'Dezenas: {round((nCentena-nDezena)/10)}')
    print(f'Unidades: {round(nDezena-nUnidade)}')
elif n < 100 and n > 10:
    print(f'Dezenas: {round((nCentena-nDezena)/10)}')
    print(f'Unidades: {round(nDezena-nUnidade)}')
elif n < 10:
    print(f'Unidades: {round(n)}')
else:
    print(f'Milhares: {round((n-nMilhar)/1000)}')
    print(f'Centenas: {round((nMilhar-nCentena)/100)}')
    print(f'Dezenas: {round((nCentena-nDezena)/10)}')
    print(f'Unidades: {round(nDezena-nUnidade)}')