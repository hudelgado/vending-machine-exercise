from peewee import CharField, IntegerField, Check

from .db import db_wrapper

class BaseModel(db_wrapper.Model):
  pass

class Product(BaseModel):
  code = CharField(unique=True)
  name = CharField()
  price = IntegerField(constraints=[Check('quantity > 0')])
  quantity = IntegerField(default=0, constraints=[Check('quantity >= 0')])

  def __str__(self):
    return '{} of \'{}\' with code \'{}\' each costs {}'.format(self.quantity, self.name, self.code, self.value)

class Coin(BaseModel):
  denomination = CharField()
  quantity = IntegerField(default=0, constraints=[Check('quantity >= 0')])
  value = IntegerField(default=0, constraints=[Check('quantity >= 0')])

  def __str__(self):
    return '{} of \'{}\' each worth {}'.format(self.quantity, self.denomination, self.value)