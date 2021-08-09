conta = float(input('Informe o valor da conta R$: '))

valorDiv = conta/3 

if valorDiv <= int(valorDiv) + 0.30:
    print(f'Carlos pagará: R${int(valorDiv)}')
    print(f'André pagará: R${int(valorDiv)}')
    total = conta - int(valorDiv*2)
else:
    total = conta/3
    print(f'Carlos pagará: R${total:.2f}')
    print(f'André pagará: R${total:.2f}')

print(f'Felipe pagará: R${total:.2f}')