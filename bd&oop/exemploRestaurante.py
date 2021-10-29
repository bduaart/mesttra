from typing import AsyncIterable, Text
from peewee import Database, FloatField, datetime, ForeignKeyField, RawQuery, SqliteDatabase, Model, TextField, IntegerField, ForeignKeyAccessor, BooleanField, DateTimeField

db = SqliteDatabase("database.sqlite")

class BaseModel(Model):
    class Meta:
        database = db

class Restaurante(BaseModel):
    nome = TextField(null=False)
    classificacao = IntegerField(null=True)
    endereco = TextField(null=False)
    estilo = TextField(null=True)

class Prato(BaseModel):
    nome = TextField(null=False)
    preco = FloatField(null=False)
    descricao = TextField(null=False)

class Pratos_Restaurantes(BaseModel):
    id_restaurante = ForeignKeyField(Restaurante, backref='pratos_restaurantes')
    id_prato = ForeignKeyField(Prato, backref='pratos_restaurantes')

Restaurante.create_table()
Prato.create_table()
Pratos_Restaurantes.create_table()

'''Restaurante.create_table()
Prato.create_table()
Pratos_Restaurantes.create_table()
Restaurante.drop_table()'''

'''Restaurante.create(
    nome='Burger King',
    classificacao=8,    
    endereco='Rua 13 de Maio, 256',
    estilo='Hamburgueria'
)

Prato.create(
    nome='X-Tudo',
    preco=24.50,
    descricao="Sanduiche recheado com tudo"
)'''

Pratos_Restaurantes.create(
    id_restaurante = 1,
    id_prato = 1
)