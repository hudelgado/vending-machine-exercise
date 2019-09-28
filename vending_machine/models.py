import json
from peewee import CharField, IntegerField, Check
from playhouse.shortcuts import model_to_dict

from .db import db_wrapper

class BaseModel(db_wrapper.Model):
  """Base model to all models
  
  Knows how to convert to a dictionary and string.
  """

  def __str__(self):
    """Get the string representation of the model"""
    return json.dumps(self.to_dict())

  def to_dict(self):
    return model_to_dict(self)

class Product(BaseModel):
  """Data model of a product

  Attributes
  ----------
  code : CharField
    A code to identify the product
  name : CharField
    The name of a product
  price : IntegerField
    The price of product, must be greater than 0
  quantity : IntegerField
    The available quantity of a product, must be equal or
    greater than 0
  """

  code = CharField(unique=True)
  name = CharField(unique=True)
  price = IntegerField(constraints=[Check('price > 0')])
  quantity = IntegerField(default=0, constraints=[Check('quantity >= 0')])

class Coin(BaseModel):
  """Data model of a Coin

  Attributes
  ----------
  denomination : CharField
    The denomination of a coin
  quantity : IntegerField
    The available quantity of a coin, must be equal or
    greater than 0
  value : IntegerField
    The value of a coin, must be greater than 0
  """
  denomination = CharField(unique=True)
  quantity = IntegerField(default=0, constraints=[Check('quantity >= 0')])
  value = IntegerField(constraints=[Check('value > 0')])
