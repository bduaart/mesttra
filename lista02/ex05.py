n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))

if n1 == 0 or n2 == 0:
    print('A operação não pode ser realizada')
    quit()
else:
    print(f'A divisão de {n1} por {n2} é {n1/n2:.2f}')