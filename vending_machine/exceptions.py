
class BaseException(Exception):
  status_code = 400

  def __init__(self, message, status_code=None, payload=None):
    Exception.__init__(self)
    self.message = message
    if status_code is not None:
      self.status_code = status_code
    self.payload = payload

  def to_dict(self):
    rv = dict(self.payload or ())
    rv['message'] = self.message
    return rv

class ProductNotAvailable(BaseException):
  def __init__(self, message=None, status_code=None, payload=None):
    msg = 'Product not available' if message is None else message
    BaseException.__init__(self, msg, 404, payload)

class NotEnoughMoney(BaseException):
  def __init__(self, message=None, status_code=None, payload=None):
    msg = 'Please insert more money' if message is None else message
    BaseException.__init__(self, msg, 402, payload)

class NoChange(BaseException):
  def __init__(self, message=None, status_code=None, payload=None):
    msg = 'No available change' if message is None else message
    BaseException.__init__(self, msg, 503, payload)