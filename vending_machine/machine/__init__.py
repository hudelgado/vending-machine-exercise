"""Machine API module

This module has the blueprint for the machine API.

Defines a single endpoint for the product buy.

Endpoints
=========
PUT: /api/machine/buy
"""

from flask import Blueprint, request, jsonify

from vending_machine.dispenser import Dispenser
from vending_machine.exceptions import ProductNotAvailable

machine_bp = Blueprint('machine', __name__, url_prefix='/api/machine')

@machine_bp.route('/buy', methods=['PUT'])
def buy_endpoint():
  """Buy a product from the machine

  PUT:
    body: application/json
    example: {'code': '1', 'change': ['1p']}
    parameters:
      code: string
        The code of the product to buy
      change: list
        The list of coins to pay the product
    responses:
      200: If product has been sold
        example: {'product': 'Soda', 'change': ['1p']}
        schema:
          product: string
            The product name
          change: array
            Array containing the coins in the change
      402: If insuficient coins are supplied
      404: If product not available
      503: If no change is available
  """

  payload = request.json
  if not 'code' in payload:
    raise ProductNotAvailable()
  elif not 'change' in payload:
    raise NotEnoughMoney()

  return jsonify(Dispenser().buy(payload['code'], payload['change']))

