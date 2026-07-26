from .base import PricingEngine
from src.instruments import Option, EuropeanCallOption, EuropeanPutOption
import numpy as np
from scipy.stats import norm

class BlackScholesEngine(PricingEngine):
  """
  A Black-Scholes Pricing engine for European Options 
  """
  def __init__(self):
    super().__init__()

  def calculate_price(self, option: Option, spot: float, rate: float, vol: float):
    """
    Calculates the current price of the European option. 

    Args:
      option (Option): The option to be priced (accepts European or American)
      spot (float): The current spot price of the underlying asset
      rate (float): The annual risk free rate
      vol (float): The annual volatility of the underlying asset 
    
    Returns:
      float: the current price
    """
    # for clean maths
    S = spot
    K = option.strike
    T = option.maturity
    r = rate

    d1 = (np.log(S / K) + (r + (vol ** 2) / 2) * T) / (vol * np.sqrt(T))
    d2 = (np.log(S / K) + (r - (vol ** 2) / 2) * T) / (vol * np.sqrt(T))

    if isinstance(option, EuropeanCallOption):
      return S * norm.cdf(d1) - K * norm.cdf(d2) * np.exp(-r * T)

    elif isinstance(option, EuropeanPutOption):
      return K * norm.cdf(-d2) * np.exp(-r * T) - S * norm.cdf(-d1) 

    else:
      raise TypeError(
        f"Black-Scholes pricer only accepts EuropeanCallOption and EuropeanPutOption"
        f"\nInput: {type(option).__name__}"
      )
    


