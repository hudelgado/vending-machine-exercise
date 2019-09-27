from flask import Blueprint, request, jsonify

from vending_machine.dispenser import Dispenser
from vending_machine.exceptions import ProductNotAvailable

machine_bp = Blueprint('machine', __name__, url_prefix='/api/machine')

@machine_bp.route('/buy', methods=['POST'])
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

