from .config import CURRENCY, AVAILABLE_CURRENCIES
from .models import Coin
from .exceptions import NotEnoughMoney, NoChange

class Wallet:
  def __init__(self, currency=None):
    self.currency = AVAILABLE_CURRENCIES[CURRENCY] if not currency else currency

  def coins(self):
    return [coin for coin in Coin.select().order_by(Coin.value.desc())]

  def recharge(self, changes):
    for coin in changes:
      Coin.update(quantity = Coin.quantity + 1).where(Coin.denomination == coin).execute()
    return True

  def pay(self, price, coins):
    inserted_value = self._sum_coins(coins)

    if price > inserted_value:
      raise NotEnoughMoney()

    wallet = self._add_to_wallet(coins)
    change = self._change_for(inserted_value - price, wallet)

    for coin in wallet:
      coin.save(only=[Coin.quantity])

    return change

  def _change_for(self, ammount, wallet):
    change = []
    while ammount > 0:
      for coin in wallet:
        if coin.quantity > 0 and coin.value <= ammount:
          change.append(coin.denomination)
          ammount -= coin.value
          coin.quantity -= 1
          break
      else:
        raise NoChange()

    return change

  def _add_to_wallet(self, coins):
    """ Update machine wallet with received coins """
    wallet = self.coins()
    for coin in coins:
      for c in wallet:
        if (c.denomination == coin):
          c.quantity += 1
    return wallet
 
  def _sum_coins(self, coins):
    value = 0
    for coin in coins:
      try:
        value += self.currency[coin]
      except:
        pass
    return value