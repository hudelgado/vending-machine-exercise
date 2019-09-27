from vending_machine.dispenser import Dispenser

def test_dispenser_init(app):
  with app.app_context():
    machine = Dispenser()
    assert machine.wallet is not None
    assert machine.store is not None

def test_dispenser_buy(app):
  with app.app_context():
    machine = Dispenser()
    result = machine.buy('2', ['50p'])
    assert result['product'] == 'juice'
    assert result['change'] == ['2p']



def test_dispenser_load_products(app, client):
  pass

def test_dispenser_load_coins(app, client):
  pass
