from typing import AsyncIterable, Text
from peewee import Database, datetime, ForeignKeyField, RawQuery, SqliteDatabase, Model, TextField, IntegerField, ForeignKeyAccessor, BooleanField, DateTimeField

db = SqliteDatabase("database.sqlite")


class BaseModel(Model):
    class Meta:
        database = db

class Aluno(BaseModel):
    nome = TextField(null=False)
    RA = TextField(unique=True)
    genero = TextField(null=True)
    idade = IntegerField()
    formado = BooleanField(default=False)
    nacionalidade = TextField()
    endereco = TextField()

class Disciplina(BaseModel):
    nome = TextField(null=False)
    professor = TextField(null=False)
    horario = DateTimeField()
    area = TextField()
    curso = TextField(null=False)
    ementa = TextField()
    qnt_alunos = IntegerField(default=0)

class Disciplinas_Alunos(BaseModel):
    nota = IntegerField()
    id_aluno = ForeignKeyField(Aluno, backref='disciplinas_alunos')
    id_disciplina = ForeignKeyField(Disciplina, backref='disciplinas_alunos')

''' >>>Executar o arquivo pra criar o BD.
    Aluno.create_table()
    Disciplina.create_table()
    Disciplinas_Alunos.create_table()'''    

'''>>>Input para dados do aluno
nomeAluno= input("Digite o nome do aluno: ")
raAluno= input("Digite o RA do aluno: ")
idadeAluno= int(input("Digite a idade do aluno: "))
generoAluno= input("Digite o gênero do aluno: ")
nacionalidadeAluno= input("Digite a nacionalidade do aluno: ")
enderecoAluno= input("Digite o endereço do aluno: ")

>>>Adicionar aluno na tabela
    Aluno.create(
    nome=nomeAluno,
    RA=raAluno,
    genero=generoAluno,
    nacionalidade=nacionalidadeAluno,
    idade=idadeAluno,
    endereco=enderecoAluno
)

>>>Adicionar disciplina na tabela
Disciplina.create(
    nome='POO',
    professor='Rodrigao',
    horario= datetime.datetime.now(),
    area='Exatas',
    curso='Ciências da Computação',
    ementa='Conteúdo sobre POO'
)

>>>Criar relacionamento entre aluno e disciplina.
Disciplinas_Alunos.create(
    id_aluno=1,
    id_disciplina=2
)
Disciplinas_Alunos.create(
    id_aluno=1,
    id_disciplina=1
)
Disciplinas_Alunos.create(
    id_aluno=2,
    id_disciplina=3
)
Disciplinas_Alunos.create(
    id_aluno=2,
    id_disciplina=1
)

'''
'''Filtrando querys e unindo tabelas
#result = Aluno.select().where(Aluno.nome.contains("Bruno") and Aluno.idade > 30)
#result = Aluno.select.where(Aluno.nacionalidade=="Brasileiro" or Aluno.formado == false)
#result = Aluno.select().join(Disciplinas_Alunos).where(Disciplinas_Alunos.id_disciplina == 1)
'''
'''result = Aluno.select()
a = Aluno.delete().where(Aluno.nome == "Marcela A.").execute()
aluno = Aluno.select().where(Aluno.nome == "Marcos Barbosa", Aluno.idade > 20).get()
aluno.nome = "Henrique"
aluno.save()

for aluno in result.dicts():
    print(aluno)
'''
'''for aluno in result:
    print(aluno.nome)
    print(aluno.RA)
    print(aluno.idade)'''