import sqlite3, pytest, tempfile, os, json

from vending_machine import create_app
from vending_machine.db import init_db, load_sample
from vending_machine.models import Product
from vending_machine.exceptions import ProductNotAvailable, NotEnoughMoney

def buy_product(client, code, change=[]):
  params = {
    'data': json.dumps({
      'code': code,
      'change': change
    }),
    'content_type': 'application/json'
  }
  return client.put('/api/machine/buy', **params)

def test_buy(client, app):
  with app.app_context():
    product = Product.select().where(Product.code == '4').get()
    assert product.code == '4'

  request = buy_product(client, product.code, ['50p', '£1', '50p'])
  assert request.status_code == 200
  reply = json.loads(request.data)
  assert reply['product'] == 'milk'

  with app.app_context():
    product_after_buy = Product.select().where(Product.code == '4').get()
    assert product_after_buy.quantity + 1 == product.quantity

def test_buy_product_not_available(client):
  request = buy_product(client, 'missing')
  assert request.status_code == 404
  reply = json.loads(request.data)
  assert reply['message'] == 'Product not available'

def test_buy_product_no_change(client):
  request = buy_product(client, '1')
  assert request.status_code == 402
  print(request.data)
  reply = json.loads(request.data)
  assert reply['message'] == 'Please insert more money'
