op = str(input('Informe a operação desejada [+,-,*,/]:'))
if op == '+' or op == '-' or op == '*' or op == '/':
    num = int(input('Informe o número para cálculo da tabuada: '))
    i = 0
    if op == '+':
        while i < 10:
            print(f'Tabuda do {op} para o número {num}')
            print(f'{num} + {i} = {num+i}')
            i += 1
    elif op == '-':
        while i < 10:
            print(f'Tabuda do {op} para o número {num}')
            print(f'{num} - {i} = {abs(num-i)}')
            i += 1
    elif op == '*':
        while i < 10:
            print(f'Tabuda do {op} para o número {num}')
            print(f'{num} * {i} = {num*i}')
            i += 1
    elif op == '/':
        i = 1
        while i < 10:
            print(f'Tabuda do {op} para o número {num}')
            print(f'{num} / {i} = {abs(num/i)}')
            i += 1
else:
    print(f'Operação digitada "{op}" incorreta!')
