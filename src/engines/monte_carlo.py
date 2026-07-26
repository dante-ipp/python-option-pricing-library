import numpy as np
from src.instruments import Option
from src.maths import GeometricBrownianMotion, StochasticProcess
from .base import PricingEngine

class MonteCarloEngine(PricingEngine):
  """
  A Monte-Carlo Pricing Engine
  """
  def __init__(self, process: StochasticProcess, num_paths: int=1000, num_steps: int=100):
    self.process = process
    self.num_paths = num_paths
    self.num_steps = num_steps

  def calculate_price(self, option: Option, spot: float):
    """
    Calculates the option price using a Monte-Carlo method

    Args:
      option (Option): the option to price
      spot (float): The current spot price of the underlying asset

    Returns:
      float: the current price of the option
    """
    paths = self.process.generate_paths(
      spot=spot,
      maturity=option.maturity,
      num_steps=self.num_steps,
      num_paths=self.num_paths
    )

    payoffs = option.get_payoff(paths)

    expected_payoff = np.mean(payoffs)

    discount = np.exp(-self.process.rate * option.maturity)

    return discount * expected_payoff



  