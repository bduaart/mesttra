sal = int(input('Informe o salário: '))

salNovo = sal*1.15
descINSS = 0.11*salNovo
descFGTS = 0.08*salNovo
descTotal = descINSS + descFGTS

print(f'\nSalário inicial: {sal:.2f}')
print(f'Salário Reajustado: {salNovo:.2f}')
print(f'Desconto 11% INSS: {descINSS:.2f}')
print(f'Desconto 8% FGTS: {descFGTS:.2f}')
print(f'Total de desconto INSS+FGTS: {descTotal:.2f}')
print(f'Salário Final {salNovo - descTotal:.2f}')