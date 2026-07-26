from .base import Option

class AmericanPutOption(Option):
  def __init__(self, strike: float, maturity: float, is_american: bool=True):
    """
    American Put Class
    """
    super().__init__(strike, maturity, is_american=True)

  def get_payoff(self, spot_price):
    return max(self.strike - spot_price, 0.0)

  
class AmericanCallOption(Option):
  def __init__(self, strike: float, maturity: float, is_american: bool=True):
    """
    American Call Option
    """
    super().__init__(strike, maturity, is_american=True)

  def get_payoff(self, spot_price):
    return max(spot_price - self.strike, 0.0)



    