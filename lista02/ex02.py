salMin = float(input('Informe o valor do salário mínimo: R$'))
salFun = float(input('Informe o valor do salário do funcionário: R$'))

if salFun < salMin:
    print('O funcionário ganha menos que um salário mínimo!')
else:
    print(f'O funcionário recebe {salFun/salMin:.1f} salário mínimos!')