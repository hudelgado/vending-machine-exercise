from flask.cli import with_appcontext
from playhouse.flask_utils import FlaskDB
import click, os

db_wrapper = FlaskDB()

from .models import Product, Coin

def init_app(app):
  """Initialize a new application
  
  Does the following task:
    - Creates the data folder
    - Initialize the database
    - Register close_db on teardown
    - Register the cli commands
  """

  init_db_folder(app)
  db_wrapper.init_app(app)
  app.teardown_appcontext(close_db)
  app.cli.add_command(init_db_command)
  app.cli.add_command(load_sample_command)

def init_db_folder(app):
  """Initialize database folder
  
  Create the folder to store the database
  if it didn't exist yet
  """

  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass

def get_db():
  """Retrieve the current database"""

  return db_wrapper.database

def close_db(e=None):
  """Closes the database"""
  
  get_db().close()

def init_db():
  """Initialize the database

  Create the tables in the database
  """

  get_db().create_tables([Product, Coin])

def load_sample():
  """Load the sample data into the database"""

  from .config import INITIAL_CHANGES, INITIAL_PRODUCTS, CURRENCY, AVAILABLE_CURRENCIES
  currency = AVAILABLE_CURRENCIES[CURRENCY]
  for (desc, qtd) in INITIAL_CHANGES:
    Coin.create(denomination=desc, quantity=qtd, value=currency[desc])
  for product in INITIAL_PRODUCTS:
    Product.create(**product)

@click.command('init-db')
@with_appcontext
def init_db_command():
  """Create new tables"""
  init_db()
  click.echo('Initialized the database.')

@click.command('load-sample')
@with_appcontext
def load_sample_command():
  """Load initial products and coins sample data"""
  load_sample()
  click.echo('Loaded sample data')
