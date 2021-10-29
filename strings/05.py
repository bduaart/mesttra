import locale
from datetime import datetime as date
locale.setlocale(locale.LC_TIME, "pt_BR")

dtnascimento = input("Digite sua data de nascimento no formato dd/mm/aaaa: ")

hoje = date.strptime(dtnascimento,"%d/%m/%Y")

texto = hoje.strftime("Você nasceu %d de mes de %Y")

###Converte a primeira letra do Mes para maiuscula e realiza a substituicao da palavra mes na string acima
print(texto.replace('mes',hoje.strftime("%B").capitalize()))
