from peewee import *
from database.database import db
import datetime

class Cliente(Model):
    nome = CharField()
    email = CharField()
    quantidade = IntegerField()
    data_registro = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db # This model uses the "people.db" database.