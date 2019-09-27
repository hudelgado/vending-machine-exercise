from .models import Product
from .exceptions import ProductNotAvailable

class Store:
  selected = None

  def select(self, code):
    try:
      self.selected = Product.select().where(Product.code == code, Product.quantity > 0).get()
      return self.selected
    except:
      raise ProductNotAvailable()
    
  def dispense(self):
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
    for product in products:
      Product.update(quantity = Product.quantity + product['quantity']).where(Product.code == product['code']).execute()
    return True