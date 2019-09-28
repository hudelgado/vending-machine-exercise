import sqlite3, pytest, json

from vending_machine import create_app
from vending_machine.db import init_db, load_sample
from vending_machine.models import Product, Coin
from vending_machine.exceptions import ProductNotAvailable, NotEnoughMoney

def load_coins(client, coins=[]):
  params = {
    'data': json.dumps(coins),
    'content_type': 'application/json'
  }
  return client.put('/api/service/load_coins', **params)

def load_products(client, products=[]):
  params = {
    'data': json.dumps(products),
    'content_type': 'application/json'
  }
  return client.put('/api/service/load_products', **params)

def test_get_products(client, app):
  with app.app_context():
    db_products = [p for p in Product.select()]

  request = client.get('/api/service/get_products')

  assert request.status_code == 200

  products = json.loads(request.data)

  assert len(products) == len(db_products)

def test_load_products(client, app):
  with app.app_context():
    product = Product.select().where(Product.code == '4').get()
    assert product.code == '4'

  request = load_products(client, [{'code': '4', 'quantity': 5}])

  assert request.status_code == 200
  assert json.loads(request.data) == True

  with app.app_context():
    product_after = Product.select().where(Product.code == '4').get()
    assert product_after.quantity == product.quantity + 5

def test_load_new_products(client, app):
  request = load_products(client, [{
    'code': 'NEW',
    'name': 'new product',
    'quantity': 5,
    'price': 10
  }])

  assert request.status_code == 200
  assert json.loads(request.data) == True

  with app.app_context():
    product = Product.select().where(Product.code == 'NEW').get()
    assert product.code == 'NEW'
    assert product.name == 'new product'
    assert product.quantity == 5
    assert product.price == 10

def test_get_coins(client, app):
  with app.app_context():
    db_coins = [coin for coin in Coin.select()]

  request = client.get('/api/service/get_coins')

  assert request.status_code == 200

  coins = json.loads(request.data)

  assert len(coins) == len(db_coins)

def test_load_coins(client, app):
  with app.app_context():
    coin = Coin.select().where(Coin.denomination == '1p').get()
    assert coin.denomination == '1p'

  request = load_coins(client, [{'denomination': '1p', 'quantity': 2}])

  assert request.status_code == 200
  assert json.loads(request.data) == True

  with app.app_context():
    coin_after = Coin.select().where(Coin.denomination == '1p').get()
    assert coin_after.quantity == coin.quantity + 2
