from .config import CURRENCY, AVAILABLE_CURRENCIES
from .models import Coin
from .exceptions import NotEnoughMoney

class BaseChangeDispenser:

  def __init__(self, currency=None):
    self.currency = AVAILABLE_CURRENCIES[CURRENCY] if not currency else currency

  def get_change_value(self, coins):
    value = 0
    for coin in coins:
      try:
        value += self.currency[coin]
      except:
        pass
    return value
  
  def get_change_for(self, price, coins):
    pass

class ChangeDispenser(BaseChangeDispenser):

  def get_change_for(self, price, coins):
    inserted_value = self.get_change_value(coins)

    if price > inserted_value:
      raise NotEnoughMoney('Please insert more money', status_code=410)

    wallet = [c for c in Coin.select().where(Coin.quantity > 0).order_by(Coin.value.desc())]

    # update machine wallet with received coins
    for coin in coins:
      for c in wallet:
        if (c.denomination == coin):
          c.quantity += 1

    change = []
    remaining_money = inserted_value - price

    while remaining_money > 0:
      for coin in wallet:
        if coin.quantity > 0 and coin.value <= remaining_money:
          change.append(coin.denomination)
          remaining_money -= coin.value
          coin.quantity -= 1

    # update the coins in the machine wallet
    for coin in wallet:
      coin.save()

    return change