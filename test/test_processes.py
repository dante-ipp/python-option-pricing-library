import pytest
import numpy as np
from src import GeometricBrownianMotion

def test_gbm_shape_and_spot():
  """
  Make sure the path matrix is the right shape and has the right first column
  """
  spot = 100.0
  num_paths = 500
  num_steps = 100

  gbm = GeometricBrownianMotion(rate=0.05, vol=0.2)
  paths = gbm.generate_paths(spot=spot, maturity=1.0, num_steps=num_steps, num_paths=num_paths)

  assert paths.shape == (num_paths, num_steps + 1)

  assert np.all(paths[:,0] == spot)

def test_gbm_positivity():
  """
  Test the positivity of the terms
  """
  spot = 100.0
  num_paths = 1000
  num_steps = 1000

  gbm = GeometricBrownianMotion(rate=0.05, vol=0.2)
  paths = gbm.generate_paths(spot=spot, maturity=1.0, num_steps=num_steps, num_paths=num_paths)

  assert np.all(paths > 0)