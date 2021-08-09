peso = int(input('Informe o peso em KG: '))

print(f'Caso a pessoa engorde 15%, ficará com: {peso*1.15:.2f}Kg')
print(f'Caso a pessoa engorde 20%, ficará com: {peso*1.20:.2f}Kg')

if peso*1.20 - peso*1.15 >= 4.5:
    print('Você deve procurar uma nutricionista!')