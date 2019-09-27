
class BaseException(Exception):
  """Base class for machine exceptions

  Attributes
  ----------
  status_code : int
    The status code to return
  """

  status_code = 400

  def __init__(self, message, status_code=None, payload=None):
    """
    Parameters
    ----------
    message : string
      The message to return
    status_code : int, optional
      The status code to return (default 400)
    payload : dict, optional
      Dictionary aditional details
    """

    Exception.__init__(self)
    self.message = message
    if status_code is not None:
      self.status_code = status_code
    self.payload = payload

  def to_dict(self):
    """Convert the exception to a dict"""

    rv = dict(self.payload or ())
    rv['message'] = self.message
    return rv

class ProductNotAvailable(BaseException):
  """Product not available machine exception"""

  def __init__(self, message=None, status_code=None, payload=None):
    """
    Parameters
    ----------
    message : string, optional
      The message to return (default 'Product not available')
    status_code : int, optional
      The status code to return (default 404)
    payload : dict, optional
      Dictionary aditional details
    """

    msg = 'Product not available' if message is None else message
    BaseException.__init__(self, msg, 404, payload)

class NotEnoughMoney(BaseException):
  """Not enough money machine exception"""

  def __init__(self, message=None, status_code=None, payload=None):
    """
    Parameters
    ----------
    message : string, optional
      The message to return (default 'Please insert more money')
    status_code : int, optional
      The status code to return (default 402)
    payload : dict, optional
      Dictionary aditional details
    """

    msg = 'Please insert more money' if message is None else message
    BaseException.__init__(self, msg, 402, payload)

class NoChange(BaseException):
  """No change machine exception"""

  def __init__(self, message=None, status_code=None, payload=None):
    """
    Parameters
    ----------
    message : string, optional
      The message to return (default 'No available change')
    status_code : int, optional
      The status code to return (default 503)
    payload : dict, optional
      Dictionary aditional details
    """

    msg = 'No available change' if message is None else message
    BaseException.__init__(self, msg, 503, payload)