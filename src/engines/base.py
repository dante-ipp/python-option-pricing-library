from abc import ABC, abstractmethod
from src.instruments import Option

class PricingEngine(ABC):
  """
  Abstract base pricing engine class
  """

  def calculate_price(self, option: Option, spot: float, rate: float, vol: float) -> float:
    """
    Calculates the current price of an option
    """
    pass
