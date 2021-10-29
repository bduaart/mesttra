texto = "a ligeira raposa marrom saltou 3 vezes sobre o cachorro cansado que estrava entre ()".upper()
textocifrado = ""
###Utilizaremos uma string do alfabeto com suas respectivas posicoes dentro da lista para realizar a substituicao
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCD"

for letra in texto:
    localizacao = alfabeto.find(letra)
    if localizacao >= 0:
        novaLocalizacao = localizacao + 3
        if novaLocalizacao > 26:
            ###realiza o enquadramento do caractere criptografado no inicio da lista
            ###uma vez que so temos 26 caracteres
            novaLocalizacao = novaLocalizacao % 26
        ###novaLocalizacao = localizacao + 3
        textocifrado += alfabeto[novaLocalizacao]
    else:
        textocifrado += letra

print(textocifrado)