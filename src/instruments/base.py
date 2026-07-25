class Option:
  def __init__(self, strike: float, maturity: float, is_american: bool = False):
    """
    A base option class

    Args:
      strike (float): The strike price of the option
      maturity (float): The time until expiration in years
    """
    self.strike = strike
    self.maturity = maturity
    self.is_american = is_american

  def get_payoff(self, spot_price: float) -> float:
      """
      Calculates the payoff of the option at expiration

      Args:
        spot_price (float): The current price of the underlying asset
        
      Returns:
        float: the payoff of the contingency claim
      """
      raise NotImplementedError("This method should be overridden by subclasses.")

  