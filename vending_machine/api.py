from flask import Blueprint, request, jsonify

from .machine import VendingMachine

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/buy', methods=['POST'])
def buy_endpoint():
  """
    {'code': '1', 'change': ['1p']}
  """
  machine = VendingMachine()
  product = machine.buy(request.json['code'], request.json['change'])
  return jsonify(product)

@bp.route('/products', methods=['POST'])
def products_endpoint():
  """
    [{'code': '1', 'quantity': 5}]
  """
  machine = VendingMachine()
  products_loaded = machine.load_products(request.json)
  return jsonify(products_loaded)

@bp.route('/coins', methods=['POST'])
def coins_endpoint():
  """
    ['1p', '10p', '3p']
  """
  change_loaded = machine.load_coins(request.json)
  return jsonify(change_loaded)

