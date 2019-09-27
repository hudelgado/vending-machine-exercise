import pytest
from vending_machine.wallet import Wallet
from vending_machine.exceptions import NoChange, NotEnoughMoney

def test_wallet_init(app):
  with app.app_context():
    wallet = Wallet()
    assert wallet.currency is not None
    assert len(wallet.coins()) == 8

def test_wallet_recharge(app):
  with app.app_context():
    wallet = Wallet()
    prev_qtd = wallet.coins()[-1].quantity
    assert wallet.recharge(['1p'])
    final_qtd = wallet.coins()[-1].quantity
    assert prev_qtd + 1 == final_qtd

def test_wallet_no_change(app):
  with app.app_context():
    wallet = Wallet()

  with pytest.raises(NoChange) as e:
    wallet._change_for(1, [])
  assert e.value.status_code == 503
  assert 'No available change' in e.value.message

def test_wallet_not_enough_money(app):
  with app.app_context():
    wallet = Wallet()

    with pytest.raises(NotEnoughMoney) as e:
      wallet.pay(5, ['1p'])
    assert e.value.status_code == 402
    assert 'Please insert more money' in e.value.message