def validaComprimento(senha):
    '''
    :param senha: Recebe como parametro a senha do usuário
    :return: retorna dois parametros:
             Primeiro Parametro: retorna True se a senha tiver a quantidade mínima de caracteres
                                 e False se não tiver a quantidade mínima de caracters
             Segundo Parametro: uma string contendo a mensagem de resultado customizada
    '''
    if(len(senha) < 8):
        mensagem = "Critério mínimo de comprimento de 8 caracteres não atendido."
        return False, mensagem
    else:
        mensagem = "Critério mínimo de comprimento de 8 caracteres atendido."
        return True, mensagem

def validaMaiusculo(senha):
    '''
    :param senha: recebe a senha do usuario como parametro
    :return: retorna dois parametros:
             Primeiro Parametro: retorna True se a senha tiver ao menos um caractere maiúsculo
                                 e False se não tiver nenhum
             Segundo Parametro: uma string contendo a mensagem de resultado customizada

    Esta função verifica se a senha atende a quantidade mínima de caracteres maiusculos digitados em uma senha.
    '''
    for caractere in senha:
        #https://www.techtudo.com.br/noticias/noticia/2015/02/o-que-e-o-codigo-ascii-e-para-que-serve-descubra.html
        #usa a função ord para converter o caractere analisado para o código inteiro ASCII e verifica se o código
        #esta entre 65 e 90 que são os caracteres maiúsculos. Ver link da tabela ASCII acima

        if (ord(caractere) in range(65,91)):
            return True, "Critério de quantidade mínima de caracteres maiúsculo atendido."
    return False, "Critério de quantidade mínima de caracteres maiúsculo não atendido."

def validaMinusculo(senha):
    for caractere in senha:
        if (ord(caractere) in range(97, 123)):
            return True, "Critério de quantidade mínima de caracteres minúsculo atendido."
    return False, "Critério de quantidade mínima de caracteres minúsculo não atendido."

def validaNumerico(senha):
    for caractere in senha:
        #aqui optamos por criar uma lista com os valores ao invés de utilizar o artifício da tabela ascii
        if (caractere in ["0","1","2","3","4","5","6","7","8","9"]):
            return True, "Critério de quantidade mínima de caracteres numéricos atendido."
    return False, "Critério de quantidade mínima de caracteres numéricos não atendido."

def validaEspecial(senha):
    for caractere in senha:
        asciicode = ord(caractere)
        if (asciicode in range(32,48) or asciicode in range(58,65) \
                                       or asciicode in range(91,97) \
                                       or asciicode in range(123,127)):
            return True, "Critério de quantidade mínima de caracteres especiais atendido."
    return False, "Critério de quantidade mínima de caracteres especiais não atendido."

mensagemFinal = ""
falhaValidacao = False

senha = input("Digite uma senha: ")

resultado, mensagem = validaComprimento(senha)

if (resultado == False):
    mensagemFinal = mensagem + "\n"
    falhaValidacao = True

resultado, mensagem = validaMaiusculo(senha)
if (resultado == False):
    mensagemFinal = mensagemFinal + mensagem + "\n"
    falhaValidacao = True

resultado, mensagem = validaMinusculo(senha)
if(resultado == False):
    mensagemFinal = mensagemFinal + mensagem + "\n"
    falhaValidacao = True

resultado, mensagem = validaNumerico(senha)
if(resultado == False):
    mensagemFinal = mensagemFinal + mensagem + "\n"
    falhaValidacao = True

resultado, mensagem = validaEspecial(senha)
if(resultado == False):
    mensagemFinal = mensagemFinal + mensagem + "\n"
    falhaValidacao = True

if(falhaValidacao):
    print('Senha não atende aos critérios abaixo: ')
    print(mensagemFinal)
else:
    print('Senha aceita!')

