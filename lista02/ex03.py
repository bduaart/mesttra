n1 = float(input('Informe o valor da primeira nota: '))
n2 = float(input('Informe o valor da segunda nota: '))
n3 = float(input('Informe o valor da terceira nota: '))

nn1 = n1*1
nn2 = n2*2
nn3 = n3*3

print(f'A média ponderada das notas {n1, n2, n3} é {(nn1+nn2+nn3)/6:.2f}')

if nn1 > nn2 and nn1 > nn3:
    print(f'A nota 1 ({n1:.2f}) é a maior nota após o cálculo do peso 1 ({nn1:.2f})')
elif nn2 > nn1 and nn2 > nn3:
    print(f'A nota 2 ({n2:.2f}) é a maior nota após o cálculo do peso 2 ({nn2:.2f})')
elif nn3 > nn1 and nn3 > nn2:
    print(f'A nota 3 ({n3:.2f}) é a maior nota após o cálculo do peso 2 ({nn3:.2f})')
elif nn1 > nn3 and nn2 > nn3:
    print(f'A nota 1 ({n1:.2f}) e a nota 2 ({n2:.2f}) é a maior nota após o cálculo do peso 1 ({nn1:.2f}) e peso 2 ({nn2:.2f})')
elif nn1 > nn2 and nn3 > nn2:
    print(f'A nota 1 ({n1:.2f}) e a nota 3 ({n3:.2f}) é a maior nota após o cálculo do peso 1 ({nn1:.2f}) e peso 3 ({nn3:.2f})')
elif nn2 > nn1 and nn3 > nn1:
    print(f'A nota 2 ({n2:.2f}) e a nota 3 ({n3:.2f}) é a maior nota após o cálculo do peso 2 ({nn2:.2f}) e peso 3 ({nn3:.2f})')
elif nn1 == nn2 and nn2 == nn3:
    print('As três notas são iguais')