nome = input("Digite o seu nome: ").split()
nomeConvertido = ""
for i in nome:
    if len(i) <= 3:
        nomeConvertido += i.lower() + " "
    elif len(i) > 3:
        nomeConvertido += i.title() + " "
print(nomeConvertido)
