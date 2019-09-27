from flask import Blueprint, request, jsonify

from .dispenser import Dispenser
from .exceptions import ProductNotAvailable

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/buy', methods=['POST'])
def buy_endpoint():
  """Buy a product from the machine
  
    {'code': '1', 'change': ['1p']}
  """

  machine = Dispenser()
  if not 'code' in request.json:
    raise ProductNotAvailable()
  elif not 'change' in request.json:
    raise NotEnoughMoney()
  product = machine.buy(request.json['code'], request.json['change'])
  return jsonify(product)

@bp.route('/load_products', methods=['POST'])
def products_endpoint():
  """Load products into the machine

    [{'code': '1', 'quantity': 5}]
  """

  machine = Dispenser()
  products_loaded = machine.load_products(request.json)
  return jsonify(products_loaded)

@bp.route('/load_coins', methods=['POST'])
def coins_endpoint():
  """Load coins into the machine

    ['1p', '10p', '3p']
  """

  machine = Dispenser()
  change_loaded = machine.load_coins(request.json)
  return jsonify(change_loaded)

