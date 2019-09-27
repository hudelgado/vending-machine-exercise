import json
from .models import Product, Coin
from .store import Store
from .wallet import Wallet
from .exceptions import ProductNotAvailable


class Dispenser:
  """Products dispenser

  Can be loaded with products and coins.
  
  It allows to sell a product allowing it's payment
  and return the change for the transaction.

  Attributes
  ----------
  wallet : Wallet
    a wallet to keep the coins for change
  store : Store
    the store with all the products

  Methods
  -------
  buy(code, coins)
    Buy a product from the dispenser and return change
  load_products(products)
    Restock the dispenser with products
  load_coins(coins)
    Restock the dispenser with coins
  """

  def __init__(self, wallet = None, store = None):
    """
    Parameters
    ----------
    wallet : Wallet, optional
      a wallet to keep the coins for change
    store : Store, optional
      the store with all the products
    """

    self.wallet = Wallet() if not wallet else wallet
    self.store = Store() if not store else store

  def buy(self, code, coins):
    """ Buy a product from the store and return change

    Parameters
    ----------
    code : str
      The code for the product to buy
    coins : list
      List of strings of the coins denominations for the payment

    Raises
    ------
    ProductNotAvailable
      If the product isn't available to buy or it doesn't have stock.
    NotEnoughMoney
      If the introduced coins aren't enough to pay for the product.
    NoChange
      If there is no coins available for the change to be returned.
    """

    return {
      'change': self.wallet.pay(self.store.select(code).price, coins),
      'product': self.store.dispense()
    }

  def load_products(self, products):
    """Restock the dispenser with products

    Parameters
    ----------
    products : list
      List of dictionaries of the products to to restock
    """

    return self.store.recharge(products)

  def load_coins(self, coins):
    """Restock the dispenser with coins

    Parameters
    ----------
    coins : list
      List of strings of the coins denominations to restock
    """

    return self.wallet.recharge(coins)
