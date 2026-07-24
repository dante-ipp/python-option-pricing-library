from src import EuropeanCallOption, EuropeanPutOption

def test_european_call_in_the_money():
  """
  Tests the EuropeanCallOption when in the money. 
  (strike < 100)
  """
  call = EuropeanCallOption(strike=100, maturity=1.0)

  payoff = call.get_payoff(spot_price=110.0) 

  assert payoff == 10.0

def test_european_call_out_of_the_money():
  """
  Tests the EuropeaCallOption when out of the money
  (strike > spot)
  """
  call = EuropeanCallOption(strike=100, maturity=1.0)

  payoff = call.get_payoff(spot_price=90.0) 

  assert payoff == 0.0

def test_european_put_in_the_money():
  """
  Tests the EuropeanPutOption when in the money
  (strike > spot)
  """
  put = EuropeanPutOption(strike=100, maturity=1.0)

  payoff = put.get_payoff(spot_price=90.0) 

  assert payoff == 10.0

def test_european_put_out_of_the_money():
  """
  Tests the EuropeanPutOption when out of the money
  (strike < spot)
  """
  put = EuropeanPutOption(strike=100, maturity=1.0)

  payoff = put.get_payoff(spot_price=110.0) 

  assert payoff == 0

  def test_option_at_price():
    """
    Test both the european put and call at price
    (spot = stike)
    """
    call = EuropeanCallOption(strike=100, maturity=1.0)
    put = EuropeanPutOption(strike=100, maturity=1.0)

    assert call.get_payoff(spot_price=100.0) == 0.0
    assert put.get_payoff(spot_price=100.0) == 0.0