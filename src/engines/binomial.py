from .base import PricingEngine
from src.instruments import Option
import numpy as np

class BinomialEngine(PricingEngine):
  """
  A binomial pricing engine using the CRR parameterisation
  """
  def __init__(self, num_steps: int = 100):
    self.num_steps = num_steps

  def calculate_price(self, option: Option, spot: float, rate: float, vol: float) -> float:
    """
    Calculates the current option price of a contingency claim using the CRR (or Binomial) model

    Args:
      option (Option): The option to be priced (accepts European or American)
      spot (float): The current spot price of the underlying asset
      rate (float): The annual risk free rate
      vol (float): The annual volatility of the underlying asset 
    
    Returns:
      float: The caluculated present price
    """
    # setup CRR parameters
    dt = option.maturity / self.num_steps

    up = np.exp(vol * np.sqrt(dt))
    down = 1 / up

    p = (np.exp(rate * dt) - down) / (up - down) 

    # Discount per time step
    discount = np.exp(-rate * dt)

    # Initialise empty np.vectors
    prices_at_maturity = np.zeros(self.num_steps + 1)
    option_values = np.zeros(self.num_steps + 1)

    # Compute option values at maturity
    for i in range(self.num_steps + 1):
      prices_at_maturity[i] = (up ** i) * (down ** (self.num_steps - i)) * spot

    # Compute the value of the options at maturity
    for i in range(self.num_steps + 1):
      option_values[i] = option.get_payoff(prices_at_maturity[i])

    # Backwards induction
    for step in range(self.num_steps - 1, -1, -1):
      for i in range(step + 1):
        expected_value = p * option_values[i + 1] + (1 - p) * option_values[i]
        continuation_value = discount * expected_value

        if getattr(option, 'is_american', False):
          current_spot = (up ** i) * (down ** (step - i)) * spot
          intrinsic_value = option.get_payoff(current_spot)

          option_values[i] = max(intrinsic_value, continuation_value)

        else:
          option_values[i] = continuation_value

    return option_values[0]