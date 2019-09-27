from .models import Product
from .exceptions import ProductNotAvailable

class Store:
  """A products store

  The store allows to select and retrieve products.

  It keep track of available products and can be
  recharged with more.

  Attributes
  ----------
  selected : Product
    the currently selected product in the store

  Methods
  -------
  select(code)
    Select a product in the store
  dispense()
    Return the currently selected product in the store
  recharge(products)
    Restock the store with products
  """

  selected = None

  def select(self, code):
    """Select a product in the store

    Parameters
    ----------
    code : str
      The code for the product to select

    Raises
    ------
    ProductNotAvailable
      If the product doesn't exist or doesn't have stock.
    """

    try:
      self.selected = Product.select().where(Product.code == code, Product.quantity > 0).get()
      return self.selected
    except:
      raise ProductNotAvailable()
    
  def dispense(self):
    """Retrieve the selected product from the store

    Raises
    ------
    ProductNotAvailable
      If the product ran out of stock.
    """
    if not self.selected:
      return None

    try:
      product = self.selected
      product.quantity -= 1
      product.save(only=[Product.quantity])
    except peewee.IntegrityError as e:
      raise ProductNotAvailable()
    finally:
      self.selected = None

    return product.name

  def recharge(self, products):
    """Recharge the store with products

    Parameters
    ----------
    products : list
      List of dictionaries of the products to to restock
    """
    for product in products:
      Product.update(quantity = Product.quantity + product['quantity']).where(Product.code == product['code']).execute()
    return True