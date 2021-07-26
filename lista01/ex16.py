n = int(input('Digite um número de 4 dígitos: '))

nMilhar = n%1000
nCentena = nMilhar%100
nDezena = nCentena%10
nUnidade = nDezena%1

print(f'Milhares: {round((n-nMilhar)/1000)}')
print(f'Centenas: {round((nMilhar-nCentena)/100)}')
print(f'Dezenas: {round((nCentena-nDezena)/10)}')
print(f'Unidades: {round(nDezena-nUnidade)}')