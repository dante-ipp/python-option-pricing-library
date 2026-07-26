from .base import Option
import numpy as np

class EuropeanCallOption(Option):
  def __init__(self, strike: float, maturity: float):
    """
    European call class
    """
    super().__init__(strike, maturity)

  def get_payoff(self, spot_price: float):
    if isinstance(spot_price, (int, float)) or (isinstance(spot_price, np.ndarray) and spot_price.ndim == 1):
      return max(spot_price - self.strike, 0.0)

    elif isinstance(spot_price, np.ndarray) and spot_price.ndim == 2:
      return np.maximum(spot_price[:,-1] - self.strike, 0.0)

    else:
      raise("get_payoff recieved unexpected type: {type(spot_price)}")

class EuropeanPutOption(Option):
  def __init__(self, strike: float, maturity: float):
    """
    European put class
    """
    super().__init__(strike, maturity)

  def get_payoff(self, spot_price: float):
    if isinstance(spot_price, (int, float)) or (isinstance(spot_price, np.ndarray) and spot_price.ndim == 1):
      return max(self.strike - spot_price, 0.0)

    elif isinstance(spot_price, np.ndarray) and spot_price.ndim == 2:
      return np.maximum(self.strike - spot_price[:,-1], 0.0)

    else:
      raise("get_payoff recieved unexpected type: {type(spot_price)}")