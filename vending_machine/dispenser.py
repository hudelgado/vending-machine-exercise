import json
from .models import Product, Coin
from .store import Store
from .wallet import Wallet
from .exceptions import ProductNotAvailable


class Dispenser:

  def __init__(self, wallet = None, store = None):
    self.wallet = Wallet() if not wallet else wallet
    self.store = Store() if not store else store

  def buy(self, code, coins):
    return {
      'change': self.wallet.pay(self.store.select(code).price, coins),
      'product': self.store.dispense()
    }

  def load_products(self, products):
    self.store.reacharge(products)

  def load_coins(self, changes):
    self.wallet.recharge(changes)
