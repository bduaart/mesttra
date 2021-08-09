print('Área do Trapézio')
basMaior = int(input('Informe o valor da base maior: '))
basMenor = int(input('Informe o valor da base menor: '))
alturaTrapezio = int(input('Informe o valor da altura: '))

print('\nÁrea do quadrado')
lado = int(input('Informe o valor de um dos lados: '))

print('\nÁrea do retângulo')
largura = int(input('Informe o valor da largura: '))
alturaRetangulo = int(input('Informe o valor da altura: '))

print('\nÁrea do círculo')
raio = int(input('Informe o valor do raio'))

print('\nÁrea do triângulo')
baseTriangulo = int(input('Informe o valor da base: '))
alturaTriangulo = int(input('Informe o valor da altura'))

areaTrap = (basMaior+basMenor)*alturaTrapezio / 2
areaQuadr = lado*lado
areaRet = largura*alturaRetangulo
areaCirc = raio*raio*3.14
areaTri = (baseTriangulo*alturaTriangulo)/2

print(f'Área do trapézio é: {areaTrap:.2f}')
print(f'Área do Quadrado é {areaQuadr:.2f}')
print(f'A área do retângulo é: {areaRet:.2f}')
print(f'Área do círculo é: {areaCirc:.2f}')
print(f'A área do triângulo {areaTri:.2f}')

if areaTri > areaCirc and areaTri > areaTrap and areaTri > areaRet and areaTri > areaQuadr:
    print(f'O objeto com a maior área é o Triângulo com {areaTri} de area')
elif areaCirc > areaTri and areaCirc > areaTrap and areaCirc > areaRet and areaCirc > areaQuadr:
    print(f'O objeto com a maior área é o Círculo com {areaCirc} de area')
elif areaRet > areaCirc and areaRet > areaTrap and areaRet > areaRet and areaRet > areaQuadr:
    print(f'O objeto com a maior área é o Retângulo com {areaRet} de area')
elif areaTrap > areaTri and areaTrap > areaCirc and areaTrap > areaRet and areaTrap > areaQuadr:
    print(f'O objeto com a maior área é o Trapézio com {areaTrap} de area')
elif areaQuadr > areaTri and areaQuadr > areaTrap and areaQuadr > areaRet and areaQuadr > areaCirc:
    print(f'O objeto com a maior área é o Quadrado com {areaQuadr} de area')            