def removeEspacos(frase):
    ###Transforma a string em uma lista
    fraseTemp = ""

    for item in frase.split():
        fraseTemp += item + " "

    return fraseTemp.strip()

def numeroCaracteres(frase):
    frase = removeEspacos(frase)
    return len(frase)

def numeroPalavras(frase):
    frase = removeEspacos(frase)
    lista = frase.split(" ")
    return len(lista)

print(numeroCaracteres("    Bruno     Duarte "))
print(numeroPalavras("    Bruno     Duarte "))
