sal = int(input('Informe o salário: '))

salNovo = sal*1.05
descIR = 0.00
descIRNovo = 0.00
descINSS = 0.11*salNovo
descFGTS = 0.08*salNovo

print(f'\nSalário inicial: {sal:.2f}')
print(f'Salário Reajustado: {salNovo:.2f}')
print(f'Desconto 11% INSS: {descINSS:.2f}')
print(f'Desconto 8% FGTS: {descFGTS:.2f}')

if sal > 1903.99 and sal < 2826.65:
    descIR = sal*0.075
elif sal > 2826.66 and sal < 3751.05:
    descIR = sal*0.15
elif sal > 3751.06 and sal < 4664.68:
    descIR = sal*0.225
elif sal > 4664.68:
    descIR = sal*0.275

if salNovo > 1903.99 and salNovo < 2826.65:
    descIRNovo = salNovo*0.075
elif salNovo > 2826.66 and salNovo < 3751.05:
    descIRNovo = salNovo*0.15
elif salNovo > 3751.06 and salNovo < 4664.68:
    descIRNovo = salNovo*0.225
elif salNovo > 4664.68:
    descIRNovo = salNovo*0.275

descTotalNovo = descINSS + descFGTS + descIRNovo
descTotal = 0.11*sal + 0.08*sal + descIR

print(f'Desconto IR: {descIRNovo:.2f}')
print(f'Total de desconto INSS+FGTS+IR: {descTotalNovo:.2f}')
print(f'Salário Final {salNovo - descTotalNovo:.2f}')
if salNovo-descTotalNovo < sal-descTotal:
    print('O novo salário final é menor do que o salário recebido antes do aumento')