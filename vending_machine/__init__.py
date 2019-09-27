"""Vending Machine module

This module contains the functionality for the vending machine.
It contains application factory to create a Flask application.

"""

import os
from flask import Flask, jsonify

from .exceptions import NotEnoughMoney, ProductNotAvailable, NoChange

def handle_api_exception(error):
  """Helper to handle api exceptions"""

  response = jsonify(error.to_dict())
  response.status_code = error.status_code
  return response

def create_app(test_config=None):
  """Create a flask application

  Parameters
  ----------
  test_config : dict, optional
    Dictionary with a configuration to use
  """

  app = Flask(__name__)

  app.config.from_mapping(
    DATABASE='sqlite:///%s' % os.path.join(app.instance_path, 'vending_machine.db')
  )

  if test_config is None:
    app.config.from_pyfile('config.py', silent=False)
  else:
    app.config.from_mapping(test_config)

  from .db import init_app
  init_app(app)

  from vending_machine.machine import machine_bp
  from vending_machine.service import service_bp
  app.register_blueprint(machine_bp)
  app.register_blueprint(service_bp)

  @app.errorhandler(NotEnoughMoney)
  def handle_not_enough_money(error):
    return handle_api_exception(error)

  @app.errorhandler(ProductNotAvailable)
  def handle_product_not_available(error):
    return handle_api_exception(error)

  @app.errorhandler(NoChange)
  def handle_no_change(error):
    return handle_api_exception(error)

  return app
