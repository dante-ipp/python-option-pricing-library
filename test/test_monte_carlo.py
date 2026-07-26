import pytest
from src import EuropeanPutOption, AsianCallOption, MonteCarloEngine, GeometricBrownianMotion

def test_monte_carlo_european_put_pricing():
  """
  Tests the Monte-Carlo pricing engine on a european put
  """
  put = EuropeanPutOption(strike=100.0, maturity=1.0)
  gbm=GeometricBrownianMotion(rate=0.05, vol=0.2)
  engine = MonteCarloEngine(process=gbm, num_paths=100000, num_steps=1000)

  price = engine.calculate_price(
    option=put,
    spot=100.0,
  )

  assert price > 0.0
  assert price == pytest.approx(5.57, rel=1e-2)


def test_asian_call_benchmark():
    gbm = GeometricBrownianMotion(rate=0.05, vol=0.2)
    engine = MonteCarloEngine(process=gbm, num_paths=100000, num_steps=1000)
    
    asian_call = AsianCallOption(strike=100.0, maturity=1.0)
    asian_price = engine.calculate_price(asian_call, spot=100.0)
    
    assert asian_price == pytest.approx(5.76, rel=0.01)
