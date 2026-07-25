from .base import Option

class EuropeanCallOption(Option):
  def __init__(self, strike: float, maturity: float):
    """
    European call class
    """
    super().__init__(strike, maturity)

  def get_payoff(self, spot_price: float):
    return max(spot_price - self.strike, 0.0)

class EuropeanPutOption(Option):
  def __init__(self, strike: float, maturity: float):
    """
    European put class
    """
    super().__init__(strike, maturity)

  def get_payoff(self, spot_price: float):
    return max(self.strike - spot_price, 0.0)