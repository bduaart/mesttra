print('Área do Trapézio')
basMaior = int(input('Informe o valor da base maior: '))
basMenor = int(input('Informe o valor da base menor: '))
alturaTrapezio = int(input('Informe o valor da altura: '))
print(f'Área do trapézio é: {((basMaior+basMenor)*alturaTrapezio) / 2:.2f}')

print('\nÁrea do quadrado')
lado = int(input('Informe o valor de um dos lados: '))
print(f'Área do Quadrado é {4*lado:.2f}')

print('\nÁrea do retângulo')
largura = int(input('Informe o valor da largura: '))
alturaRetangulo = int(input('Informe o valor da altura: '))
print(f'A área do retângulo é: {largura*alturaRetangulo:.2f}')

print('\nÁrea do círculo')
raio = int(input('Informe o valor do raio'))
print(f'Área do círculo é: {raio*raio*3.14:.2f}')

print('\nÁrea do triângulo')
baseTriangulo = int(input('Informe o valor da base: '))
alturaTriangulo = int(input('Informe o valor da altura'))
print(f'A área do triângulo {(baseTriangulo*alturaTriangulo)/2:.2f}')