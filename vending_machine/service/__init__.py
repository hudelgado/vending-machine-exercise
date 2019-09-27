from flask import Blueprint, request, jsonify

from vending_machine.dispenser import Dispenser

service_bp = Blueprint('service', __name__, url_prefix='/api/service')

@service_bp.route('/load_products', methods=['POST'])
def load_products_endpoint():
  """Load products into the machine

    [{'code': '1', 'quantity': 5}]
  """

  machine = Dispenser()
  products_loaded = machine.load_products(request.json)
  return jsonify(products_loaded)

@service_bp.route('/load_coins', methods=['POST'])
def load_coins_endpoint():
  """Load coins into the machine

    ['1p', '10p', '3p']
  """

  machine = Dispenser()
  change_loaded = machine.load_coins(request.json)
  return jsonify(change_loaded)

