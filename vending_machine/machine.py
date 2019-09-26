import json
from .models import Product, Coin
from .dispenser import ChangeDispenser
from .exceptions import ProductNotAvailable


class VendingMachine:

  def __init__(self, dispenser=None):
    self.dispenser = ChangeDispenser() if not dispenser else dispenser

  def buy(self, code, coins):
    try:
      product = Product.select().where(Product.code == code, Product.quantity > 0).get()
    except:
      raise ProductNotAvailable('Product not available', status_code=410)

    response = {
      'change': self.dispenser.get_change_for(product.price, coins),
      'product': product.name
    }

    product.quantity -= 1
    product.save()

    return response

  def load_products(self, products):
    for product in products:
      Product.update(quantity = Product.quantity + product['quantity']).where(Product.code == product['code']).execute()
    return True

  def load_coins(self, changes):
    for coin in changes:
      Coin.update(quantity = Coin.quantity + 1).where(Coin.denomination == coin).execute()
    return True
