"""Machine Service API module

This module has the blueprint for the service API.

It exposes the functionality for the products and 
coins rechargment.

Endpoints
=========
PUT: /api/service/load_products
PUT: /api/service/load_coins

"""

from flask import Blueprint, request, jsonify

from vending_machine.dispenser import Dispenser

service_bp = Blueprint('service', __name__, url_prefix='/api/service')

@service_bp.route('/get_products', methods=['GET'])
def get_products_endpoint():
  """ Return the current machine products

  response:
    body: application/json
    example: [{
      "code": "1",
      "name: "Soda",
      "quantity": 5,
      "price": 10
    }]
  """

  machine = Dispenser()
  return jsonify(machine.get_products())

@service_bp.route('/load_products', methods=['PUT'])
def load_products_endpoint():
  """Load products into the machine

  PUT:
    body: application/json
    example: [{"code": "1", "quantity": 5}]
    parameters:
      products : array
        An array of product dictionaries
        product : dict
          code : string
            The code of the product
          quantity : int
            The quantity of the product to recharge
    responses:
      200 : True
        If products has been loaded
  """

  machine = Dispenser()
  products_loaded = machine.load_products(request.json)
  return jsonify(products_loaded)

@service_bp.route('/get_coins', methods=['GET'])
def get_coins_endpoint():
  """ Return the current machine coins

  response:
    body: application/json
    example: [{
      "denomination": "1p",
      "quantity": 5
    }]
  """

  machine = Dispenser()
  return jsonify(machine.get_coins())

@service_bp.route('/load_coins', methods=['PUT'])
def load_coins_endpoint():
  """Load coins into the machine

  PUT:
    body: application/json
    example: [{
      "denomination": "1p",
      "quantity": 5
    }, {
      "denomination": "5p", "quantity": 10
    }]
    parameters: array
      An array of coin denominations and quantities
    responses:
      200 : True
        If coins has been loaded
  """

  machine = Dispenser()
  change_loaded = machine.load_coins(request.json)
  return jsonify(change_loaded)

