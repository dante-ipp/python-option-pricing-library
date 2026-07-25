from src import AmericanCallOption, AmericanPutOption

def test_american_call_in_the_money():
  """
  Tests the AmericanCallOption when in the money. 
  (strike < 100)
  """
  call = AmericanCallOption(strike=100, maturity=1.0)

  payoff = call.get_payoff(spot_price=110.0) 

  assert payoff == 10.0

def test_american_call_out_of_the_money():
  """
  Tests the AmericanCallOption when out of the money
  (strike > spot)
  """
  call = AmericanCallOption(strike=100, maturity=1.0)

  payoff = call.get_payoff(spot_price=90.0) 

  assert payoff == 0.0

def test_american_put_in_the_money():
  """
  Tests the AmericanPutOption when in the money
  (strike > spot)
  """
  put = AmericanPutOption(strike=100, maturity=1.0)

  payoff = put.get_payoff(spot_price=90.0) 

  assert payoff == 10.0

def test_american_put_out_of_the_money():
  """
  Tests the AmericanPutOption when out of the money
  (strike < spot)
  """
  put = AmericanPutOption(strike=100, maturity=1.0)

  payoff = put.get_payoff(spot_price=110.0) 

  assert payoff == 0

  def test_option_at_price():
    """
    Test both the American put and call at price
    (spot = stike)
    """
    call = AmericanCallOption(strike=100, maturity=1.0)
    put = AmericanPutOption(strike=100, maturity=1.0)

    assert call.get_payoff(spot_price=100.0) == 0.0
    assert put.get_payoff(spot_price=100.0) == 0.0