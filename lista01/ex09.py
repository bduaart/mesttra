conta = float(input('Informe o valor da conta R$: '))

valorDiv = conta/3 

print(f'Carlos pagará: R${int(valorDiv)}')
print(f'André pagará: R${int(valorDiv)}')
print(f'Felipe pagará: R${conta - int(valorDiv*2):.2f}')