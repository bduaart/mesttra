n = int(input("Informe o número para o cálculo da tabuada"))

print(f'Tabuada do + e - para o número {n}')
i = 0
while i < 10:
    print(f'{n} + {i} = {n+i}   {n} - {i} = {abs(n-i)}')
    i += 1

print(f'\nTabuada do * e / para o número {n}')
i = 0
while i < 10:
    if i == 0:
        print(f'{n} * {i} = {n*i}   Não existe divisão para zero')
    else:
        print(f'{n} * {i} = {n*i}   {n} / {i} = {n/i}')
    i += 1