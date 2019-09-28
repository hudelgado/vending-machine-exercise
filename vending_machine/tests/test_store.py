import pytest
from vending_machine.store import Store
from vending_machine.models import Product
from vending_machine.exceptions import ProductNotAvailable

def test_store_init(app):
  with app.app_context():
    store = Store()

    assert store.selected == None

def test_select_product_in_stock(app):
  with app.app_context():
    store = Store()
    product = store.select('1')

    assert store.selected == product
    assert product.code == '1'

def test_select_product_out_of_stock(app):
  with app.app_context():
    store = Store()
    product = store.select('1')
    product.quantity = 0
    product.save(only=[Product.quantity])

    with pytest.raises(ProductNotAvailable) as e:
      product = store.select('1')

    assert e.value.status_code == 404
    assert e.value.message == 'Product not available'

def test_select_non_existing_product(app):
  with app.app_context():
    store = Store()
    with pytest.raises(ProductNotAvailable) as e:
      product = store.select('missing')

    assert e.value.status_code == 404
    assert e.value.message == 'Product not available'

def test_dispense_product_in_stock(app):
  with app.app_context():
    store = Store()
    product = store.select('1')
    name = store.dispense()

    assert product.name == name
    assert store.selected is None

def test_dispense_without_select_product(app):
  with app.app_context():
    store = Store()
    name = store.dispense()

    assert name is None
    assert store.selected is None

def test_dispense_without_selecting_product(app):
  with app.app_context():
    store = Store()
    name = store.dispense()

    assert name is None
    assert store.selected is None

def test_recharge(app):
  with app.app_context():
    store = Store()
    prev_qtd = store.select('1').quantity

    assert store.recharge([{'quantity': 5, 'code': '1'}])
    assert store.select('1').quantity == prev_qtd + 5

def test_recharge_new_products(app):
  with app.app_context():
    store = Store()
    payload = [
      {'quantity': 5, 'code': 'first', 'name': 'First', 'price': 10},
      {'quantity': 10, 'code': 'second', 'name': 'Second', 'price': 8},
    ]

    assert store.recharge(payload)
    assert store.select('first').quantity == 5
    assert store.select('second').quantity == 10

def test_recharge_invalid_quantity(app):
  with app.app_context():
    store = Store()
    res = store.recharge([{'quantity': -50, 'code': '1'}])

    assert res == True