import json, pytest
from peewee import IntegrityError
from vending_machine.models import Product, Coin

def test_product_model(app):
  expected_prod = Product(id=1, code='1', name='soda', quantity=5, price=200)
  expected_dict = {'id': 1, 'code': '1', 'name': 'soda', 'price': 200, 'quantity': 5}

  with app.app_context():
    product = Product.select().where(Product.code == '1').get()
    
    assert product is not None
    assert product == expected_prod   
    assert product.to_dict() == expected_dict
    assert str(product) == json.dumps(expected_dict)

def test_product_constraints(app):
  with app.app_context():

    with pytest.raises(IntegrityError, match=r"UNIQUE.*product\.code.*") as e:
      product = Product.create(code='1', name='invalid', price=5)

    with pytest.raises(IntegrityError, match=r"CHECK.*product.*") as e:
      product = Product.create(code='new', name='invalid', price=0)

    with pytest.raises(IntegrityError, match=r"CHECK.*product.*") as e:
      product = Product.create(code='new', name='invalid', price=1, quantity=-1)

def test_coin_model(app):
  expected_coin = Coin(id=1, denomination='1p', quantity=20, value=1)
  expected_dict = {'id': 1, 'denomination': '1p', 'quantity': 20, 'value': 1}

  with app.app_context():
    coin = Coin.select().where(Coin.id == '1').get()

    assert coin is not None
    assert coin == expected_coin
    assert coin.to_dict() == expected_dict
    assert str(coin) == json.dumps(expected_dict)

def test_product_constraints(app):
  with app.app_context():

    with pytest.raises(IntegrityError, match=r"CHECK.*coin") as e:
      coin = Coin.create(denomination='1p', value=0)

    with pytest.raises(IntegrityError, match=r"CHECK.*coin") as e:
      coin = Coin.create(denomination='1c', value=1, quantity=-1)




