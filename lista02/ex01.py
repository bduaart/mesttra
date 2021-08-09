frente = float(input("Quantos metros o terreno possui de frente: "))
lat = float(input("Quantos metros o terreno possui de lateral: "))
m2 = float(input("Informe o valor do metro quadrado: "))
valor = (frente*lat)*m2

print(f"Área total do terreno de {frente}m de frente com {lat}m de lateral é {frente*lat}")
if frente-lat < (10/100*frente/1):
    print(f"O terreno recebeu um acréscimo de 22% e custará R$ {valor * 1.22}")
elif frente < (40/100*lat/1):
    print(f"O terreno recebeu um decréscimo de 12% e custará R$ {abs((valor*12/100) - valor)}")
elif frente > (70/100*lat/1):
    print(f"O terreno recebeu um decréscimo de 15% e custará R$ {abs((valor*15/100) - valor)}")
else:
    print(f'O terreno não recebeu nenhuma alteração e custará R$ {valor}')