nome = input("Digite o nome: ").lower()

reverso = ""

###Acessa individualmente cada posicao da string de forma inversa
for i in range(len(nome)-1,-1,-1):
    reverso += nome[i]
