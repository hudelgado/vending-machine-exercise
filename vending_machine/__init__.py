import os
from flask import Flask, jsonify

from .exceptions import NotEnoughMoney, ProductNotAvailable, NoChange
from .common import handle_api_exception

def create_app(test_config=None):
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

  from .api import bp
  app.register_blueprint(bp)

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
