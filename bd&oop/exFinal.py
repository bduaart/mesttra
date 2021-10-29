from peewee import Database, datetime, ForeignKeyField, RawQuery, SqliteDatabase, Model, TextField, IntegerField, ForeignKeyAccessor, BooleanField, DateTimeField
import os
from exemploAlunos import *

class System:

    def menu(self):
        os.system('clear')
        print("=" * 40 + " MENU " + "=" * 40)
        print("0 - Sair do sistema")
        print("1 - Adicionar aluno")
        print("2 - Buscas Aluno")
        print("3 - Editar Aluno")
        print("4 - Excluir Aluno")
        print("5 - Listar Alunos")
        print("6 - Formar Aluno")
        print("7 - Inserir Disciplina")
        print("8 - Alterar Disciplina")
        print("9 - Mostrar Matriculados")
        print("10 - Mostrar Formados")
        print("11 - Listar disciplinas")
        print("12 - Mostrar Disciplinas por area")
        print("13 - Mostrar aprovados")
        print("=" * 86)

    def insertAluno(self):
        nome = input("Digite o nome do aluno: ")
        ra = input("Digite o RA do aluno: ")
        idade = input("Digite a idade do aluno: ")
        genero = input("Digite o gênero do aluno: ")
        form = input("O aluno está formado? (s/n): ")
        nacionalidade = input("Digite a nacionalidade do aluno: ")
        endereco = input("Digite o endereço do aluno: ")

        Aluno.create(
            nome=nome,
            RA=ra,
            idade=idade,
            genero=genero,
            formado= True if form=='s' else False,
            nacionalidade=nacionalidade,
            endereco = endereco
        )

    def insertDisciplina(self):
        nome = input("Digite o nome da Disciplina: ")
        professor = input("Digite o nome do professor: ")
        area = input("Digite a área: ")
        curso = input("Digite o Curso da Disciplina: ")
        ementa = input("Digite a ementa da disciplina: ")
        qnt_alunos = int(input("Digite a quantidade de alunos: "))

        Disciplina.create(
            nome=nome,
            professor=professor,
            area=area,
            curso=curso,
            ementa=ementa,
            qnt_alunos=qnt_alunos
        )                

    def alterAluno(self):
        ra=(input("Digite o RA do aluno: "))
        aluno = Aluno.select().where(Aluno.RA == ra)

        if(len(aluno) == 0):
            print("Aluno não encontrado... tente novamente..")
        else:
            aluno[0].nome = input("Digite o novo nome do aluno")
            aluno[0].idade = int(input("Digite a nova idade do aluno"))
            aluno[0].genero = input("Digite o novo gênero do Aluno: ")
            form = input("O aluno está formado? (s/n): ")
            aluno[0].formado = True if form == 's' else False
            aluno[0].nacionalidade = input("Digite a nova nacionalidade do Aluno: ")
            aluno[0].endereco = input("Digite o novo endereço do Aluno: ")

            aluno[0].save()

    def alterDisciplina(self):
        id=(input("Digite o id da disciplina: "))
        disciplinas = Disciplina.select().where(Disciplina.id == id)

        if(len(disciplinas) == 0):
            print("Disciplina não encontrado... tente novamente..")
        else:
            disciplinas[0].nome = input("Digite o novo nome do disciplina")
            disciplinas[0].professor = int(input("Digite o novo professor da disciplina"))
            disciplinas[0].area = input("Digite a área da disciplina: ")
            disciplinas[0].curso = input("Digite o curso da disciplina: ")

            disciplinas[0].save()

    def deleteAluno(self):
        ra=input("Digite o RA do aluno: ")
        alunos = Aluno.select().where(Aluno.RA==ra).execute()
        if(len(alunos) == 0):
            print("Aluno não encontrado, tente novamente..")
            return
        else:
            res = Aluno.delete().where(Aluno.RA == ra).execute()

    def formAluno(self):
        ra = input("Digite o RA do aluno: ")

        aluno = Aluno.select().where(Aluno.RA == ra)

        if(len(aluno) == 0):
            print("Aluno não encontrado..")
        else:
            aluno[0].formado = True
            aluno[0].save()
            print(f'O aluno {aluno[0].nome} acabou de formar, parabéns!')


    def findAluno(self):
            ra = input("Digite o RA do aluno: ")

            aluno = Aluno.select().where(Aluno.RA == ra)

            if(len(aluno)== 0):
                print("Aluno não encontrado")
            else:
                print("="*86)
                print(f'Nome = {aluno[0].nome}')
                print(f'RA = {aluno[0].RA}')
                print(f'Idade = {aluno[0].idade}')
                print(f'Genero = {aluno[0].genero}')
                print(f'Endereço = {aluno[0].endereco}')
                print(f'Nacionalidade = {aluno[0].nacionalidade}')
                print(f'Formado = {aluno[0].formado}')

    def listAlunos(self):
        alunos = Aluno.select()
        for aluno in alunos:
                print("="*86)
                print(f'Nome = {aluno.nome}')
                print(f'RA = {aluno.RA}')
                print(f'Idade = {aluno.idade}')
                print(f'Genero = {aluno.genero}')
                print(f'Endereço = {aluno.endereco}')
                print(f'Nacionalidade = {aluno.nacionalidade}')
                print(f'Formado = {"Sim" if aluno.formado==True else "Não"}')
                print("="*86)

    def mostrarMatriculados(self, nome_disciplina):
        alunos = Aluno.select().join(Disciplinas_Alunos).join(Disciplina).where(Disciplina.nome == nome_disciplina
        and Disciplina.id == Disciplinas_Alunos.id_disciplina)
        for aluno in alunos:
            print(f'{aluno.nome} está matriculado em {nome_disciplina}')

    def mostrarFormados(self):
        alunos = Aluno.select().where(Aluno.formado ==True)
        print('Alunos formados!')
        for aluno in alunos:
            print('='*86)
            print(f'Nome = {aluno.nome}')
            print(f'RA = {aluno.RA}')
            print('='*86)

    def listarDisciplinas(self):
        disciplinas = Disciplina.select()
        print('Disciplinas: ')
        for disciplina in disciplinas:
            print(f'Nome: {disciplina.nome}             |   Professor: {disciplina.professor}               '
            + '|   Area:{disciplina.area}')

    def mostrarDisciplinasPorArea(self, area):
        disciplinas = Disciplina.select().where(Disciplina.area.contains(area))

        print(f'Disciplinas da area {area}')
        for disciplina in disciplinas:
            print(disciplinas.nome)

    def mostrarAprovados(self, nomeDisciplina):
        alunos = Aluno.select().join(Disciplinas_Alunos).join(Disciplina).where(Disciplinas_Alunos.nota >=6, Disciplina.nome == nomeDisciplina)

        print(f'Alunos aprovados em {nomeDisciplina}')
        for aluno in alunos:
            print(aluno.nome)

sys = System()

while(1):
    input("Digite enter para continuar...")
    sys.menu()
    op = int(input("Digite a opção desejada: "))

    if(op == 1):
        sys.insertAluno()
    elif(op == 2):
        sys.findAluno()
    elif(op == 3):
        sys.alterAluno()
    elif(op == 4):
        sys.deleteAluno()
    elif(op == 5):
        sys.listAlunos()
    elif(op == 6):
        sys.formAluno()
    elif(op == 7):
        sys.insertDisciplina()
    elif(op == 8):
        sys.alterDisciplina()
    elif(op == 9):
        nomeDisciplina = input('Digite o nome da disciplina: ')
        sys.mostrarMatriculados(nomeDisciplina)
    elif(op == 10):
        sys.mostrarFormados()
    elif(op == 11):
        sys.listarDisciplinas()
    elif(op == 12):
        area = input('Digite o nome da area: ')
        sys.mostrarDisciplinasPorArea(area)
    elif(op == 13):
        nomeDisciplina = input('Digite o nome da disciplina: ')
        sys.mostrarAprovados(nomeDisciplina)
    elif(op == 0):
        break
    else:
        print("Opção inválida, tente novamente...")