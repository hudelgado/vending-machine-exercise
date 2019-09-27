import json
from peewee import CharField, IntegerField, Check
from playhouse.shortcuts import model_to_dict

from .db import db_wrapper

class BaseModel(db_wrapper.Model):
  def __str__(self):
    return json.dumps(self.to_dict())

  def to_dict(self):
    return model_to_dict(self)

class Product(BaseModel):
  code = CharField(unique=True)
  name = CharField()
  price = IntegerField(constraints=[Check('price > 0')])
  quantity = IntegerField(default=0, constraints=[Check('quantity >= 0')])

class Coin(BaseModel):
  denomination = CharField()
  quantity = IntegerField(default=0, constraints=[Check('quantity >= 0')])
  value = IntegerField(constraints=[Check('value > 0')])
