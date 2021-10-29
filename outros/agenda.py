import os
'''
Funcionalidades de uma agenda
- Menu
- Adicionar contato 
- Editar um contato     falta implementar
- Deletar um contato    falta implementar
- Procurar um contato
    - Nome
    - Telefone  falta implementar
    - Celular   falta implementar
    - Email     falta implementar
- Exibir todos os contatos  
- Transformar contato em Favorito (começo da lista)     falta implementar
- Bloquear contato
- Desbloquear contato    falta implementar
'''
def exibirMenu():
    os.system('cls')
    print("=" * 40 + " MENU " + "=" * 40)
    print("0 - Sair do sistema")
    print("1 - Adicionar contato")
    print("2 - Pesquisar contato")
    print("3 - Editar contato")
    print("4 - Excluir contato")
    print("5 - Excluir todos os contatos")
    print("6 - Imprmir Lista de contato")
    print("7 - Bloquear contato")
    print("8 - Desbloquear contato")
    print("=" * 86)

def adicionarContato(nomes,fixos,celulares,emails,status):
    os.system('cls')
    nome = input("Digite o nome do contato: ")
    nomes.append(nome)
    emails.append(input("Digite o email: "))
    fixos.append(input("Digite o telefone fixo: "))
    celulares.append(input("Digite o telefone celular: "))
    # True status ativo
    # False statu desativado
    status.append(True)

    return nomes,fixos,celulares,emails,status

def exibirContato(nomes,fixos,celulares,emails,status,posicao):
    print(posicao+1, end = " ")
    print(nomes[posicao], end=" ")
    print(emails[posicao], end=" ")
    print(celulares[posicao], end=" ")
    print(fixos[posicao], end=" ")
    if (status[posicao]):
        print("Ativo")
    else:
        print("Bloqueado")

def exibirContatos(nomes,fixos,celulares,emails,status):
    print("CodigoContato Nome Emails Celular Fixo Status")
    for posicao in range(len(status)):
        exibirContato(nomes,fixos,celulares,emails,status,posicao)

def exibirMenuPesquisa():
    os.system('cls')
    print("=" * 40 + " MENU PESQUISA " + "=" * 40)
    print("0 - Voltar para o programa principal")
    print("1 - Pesquisar por nome")
    print("2 - Pesquisar por telefone fixo")
    print("3 - Pesquisar por telefone celular")
    print("4 - Pesquisar por email")
    print("=" * 86)

def pesquisaPorNome(nomes,fixos,celulares,emails,status):
    os.system('cls')
    nome = input("Digite o nome a ser pesquisado: ")
    posicao = 0
    encontrouContato = False

    #descobre quais posicoes posuem uma parte do nome pesquisa
    print("\nNome Emails Celular Fixo Status")
    for n in nomes:
         #converte tudo para minusculo para evitar problemas com as letras Maius. e Minus.
         if(nome.lower() in n.lower()):
             #exibe um unico contato
             exibirContato(nomes, fixos, celulares, emails, status, posicao)
             encontrouContato = True
         posicao += 1

    if(not(encontrouContato)):
        print("Não foram encontrados contatos com este nome!")

def bloquearContato(nomes,fixos,celulares,emails,status):
    print("Para bloquear um contato, é necessário informar o CodigoContato.")
    resposta = input("Você sabe o CodigoContato? [s/n]: ")

    #caso o usuario digite sim ou nao ao invez de s ou n, pegamos somente a posicao 0 do texto
    if resposta.lower()[0] == "s":
        posicao = int(input("Digite o código do contato: "))
        try:
            status[posicao - 1] = False
            print("Usuário bloqueado com sucesso.", end = " ")
        except IndexError:
            print("Codigo do contato não existe!", end = " ")
    else:
        exibirContatos(nomes,fixos,celulares,emails,status)
        #print("Para descobrir o Codigo do Contato acesse a opção ")
        #print("'Imprmir Lista de contato' do menu principal")

    input("Tecle ENTER para continuar.")


nomes = ['Rogerio de Freitas Ribeiro','Maria Luiza','Rogerio Francisco' ]
fixos = ['34 3245-9098','34 3141-9194','34 3246-9878']
celulares = ['34 99878-9098','34 98878-8088','34 99171-9118']
emails = ['rogeriofr@gmail.com','maria@gmail.com','rogeriof@gmail.com']
status = [True,True,True]

while(True):
    exibirMenu()
    opcao = int(input("Digite a opção desejada: "))
    if (opcao == 0):   #sair do programa
        print("Até logo :-)")
        break
    elif(opcao == 1):  #Adicionar contato
        nomes,fixos,celulares,emails,status = adicionarContato(nomes,fixos,celulares,emails,status)
    elif(opcao == 2):  #Menu Pesquisa
        exibirMenuPesquisa()
        opcao = int(input("Digite a opção desejada: "))
        if(opcao == 1):  #Pequisa por nome
            pesquisaPorNome(nomes,fixos,celulares,emails,status)
            #colocamos este input apenas para fazer com que o sistema fique
            # parado e de tempo do usuario ler os resultados impressos
            input("\nTecle ENTER para continuar!")
        elif(opcao == 2):   #pesquisa por telefone fixo
            pass       #falta implementar
        elif(opcao == 3):   #pesquisa por telefone celular
            pass       #falta implementar
        elif(opcao == 4):   #pesquisa por email
            pass       #falta implementar

    elif(opcao == 6):  #Exibe os contatos
        os.system('cls')
        exibirContatos(nomes,fixos,celulares,emails,status)
        input("\nTecle ENTER para continuar!")
    elif(opcao == 7): #bloquear contato
        os.system('cls')
        bloquearContato(nomes,fixos,celulares,emails,status)
