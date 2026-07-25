import pytest
import numpy as np
from src import EuropeanPutOption, EuropeanCallOption, BinomialEngine

def test_binomial_european_put_call_parity():
  """
  Test the european put/call parity using the binomial engine 
  """
  strike_price = 100
  maturity_years = 1.0
  spot = 100
  rate = 0.05
  vol = 0.2

  put = EuropeanPutOption(strike=strike_price, maturity=maturity_years)
  call = EuropeanCallOption(strike=strike_price, maturity=maturity_years)
  engine = BinomialEngine(num_steps=100)

  put_price = engine.calculate_price(put, spot, rate, vol)
  call_price = engine.calculate_price(call, spot, rate, vol)

  parity_difference = strike_price * np.exp(-rate * maturity_years)
  expected_difference = spot - parity_difference

  assert call_price - put_price == pytest.approx(expected_difference, 1e-2)
