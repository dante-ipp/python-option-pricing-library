import pytest
from src import AmericanPutOption, EuropeanPutOption, BlackScholesEngine

def test_black_scholes_european_put_pricing():
  """
  Tests the binomial pricing engine on a european put
  """
  put = EuropeanPutOption(strike=100.0, maturity=1.0)
  engine = BlackScholesEngine()

  price = engine.calculate_price(
    option=put,
    spot=100.0,
    rate=0.05,
    vol=0.2,
  )

  assert price > 0.0
  assert price == pytest.approx(5.57, rel=1e-2)

def test_black_scholes_american_error():
  """
  Tests the Black-Scholes error with an American put option
  """
  put = AmericanPutOption(strike=100.0, maturity=1.0)
  engine = BlackScholesEngine()

  price = engine.calculate_price(
    option=put,
    spot=100.0,
    rate=0.05,
    vol=0.2,
  )

  error_message = "Black-Scholes pricer only accepts EuropeanCallOption and EuropeanPutOption"

  with pytest.raises(TypeError, error_message):
    price