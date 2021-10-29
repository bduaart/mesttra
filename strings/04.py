nome = input("Digite o nome: ").upper()

###Vai gerar uma lista de numeros com o maior numero igual ao tamanho da string
for i in range(len(nome)+1):
    ###Faz fatiamento sempre da posicao zero com o numero do for
    print(nome[0:i])