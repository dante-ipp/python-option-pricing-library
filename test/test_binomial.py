import pytest
from src import EuropeanPutOption, BinomialEngine

def test_binomial_put_pricing():
  """
  Tests the binomial pricing engine on a european put
  """
  put = EuropeanPutOption(strike=100.0, maturity=1.0)
  engine = BinomialEngine(num_steps=100)

  price = engine.calculate_price(
    option=put,
    spot=100.0,
    rate=0.05,
    vol=0.2,
  )

  # price must be positive
  assert price > 0.0

  assert price == pytest.approx(5.57, rel=1e-2)
