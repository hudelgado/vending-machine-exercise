from .config import CURRENCY, AVAILABLE_CURRENCIES
from .models import Coin
from .exceptions import NotEnoughMoney, NoChange

class Wallet:
  """A coins wallet

  This wallet allows for the payment for a price with a list of coins,
  returning the remaining change if any.

  It keep track of available coins and can be recharged with more.

  Attributes
  ----------
  currency : dict
    Dictionary with coin value for each coin denomination

  Methods
  -------
  coins()
    Retrieve the current coins in the wallet
  recharge(changes)
    Recharge the wallet with more coins
  pay(price, coins)
    Update the wallet with the coins and obtain a change for the price
  """

  def __init__(self, currency=None):
    """
    Parameters
    ----------
    currency : dict, optional
      Dictionary with coin value for each coin denomination
    """

    self.currency = AVAILABLE_CURRENCIES[CURRENCY] if not currency else currency

  def coins(self):
    """Get a list of the current coins in the wallet"""

    return [coin for coin in Coin.select().order_by(Coin.value.desc())]

  def recharge(self, coins):
    """Recharge the wallet with coins

    Parameters
    ----------
    coins : list
      A strings list with the denominations of coins to add.
    """

    for coin in coins:
      Coin.update(quantity = Coin.quantity + 1).where(Coin.denomination == coin).execute()
    return True

  def pay(self, price, coins):
    """Pay the specified amount with the given coins

    Parameters
    ----------
    price : int
      The price to pay for
    coins : list
      The list of coins to update the wallet

    Raises
    ------
    NotEnoughMoney
      If the coins values aren't enough to pay the price.
    NoChange
      If the wallet don't have coins to return the change.
    """

    inserted_value = self._sum_coins(coins)

    if price > inserted_value:
      raise NotEnoughMoney()

    wallet = self._add_to_wallet(coins)
    change = self._change_for(inserted_value - price, wallet)

    for coin in wallet:
      coin.save(only=[Coin.quantity])

    return change

  def _change_for(self, ammount, wallet):
    """Compute the change for a specific ammount on a wallet
    """

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
    """Get an updated wallet with received coins"""

    wallet = self.coins()
    for coin in coins:
      for c in wallet:
        if (c.denomination == coin):
          c.quantity += 1
    return wallet
 
  def _sum_coins(self, coins):
    """Get the total value of the given coins"""

    value = 0
    for coin in coins:
      try:
        value += self.currency[coin]
      except:
        pass
    return value