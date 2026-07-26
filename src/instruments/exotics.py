import numpy as np
from .base import Option

class AsianPutOption(Option):
  def __init__(self, strike, maturity, is_american = False):
    super().__init__(strike, maturity, is_american)

  def get_payoff(self, spot_price):
    if isinstance(spot_price, np.ndarray) and spot_price.ndim == 2:
      average_prices = np.mean(spot_price, axis=1)
      return np.maximum(self.strike - average_prices, 0.0)

    else:
      raise("get_payoff recieved unexpected type: {type(spot_price)}")


class AsianCallOption(Option):
  def __init__(self, strike, maturity, is_american = False):
    super().__init__(strike, maturity, is_american)

  def get_payoff(self, spot_price):
    if isinstance(spot_price, np.ndarray) and spot_price.ndim == 2:
      average_prices = np.mean(spot_price, axis=1)
      return np.maximum(average_prices - self.strike, 0.0)

    else:
      raise("get_payoff recieved unexpected type: {type(spot_price)}")