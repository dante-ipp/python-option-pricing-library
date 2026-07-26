import numpy as np

class StochasticProcess:
  def generate_paths(self, spot: float, maturity: float, num_steps: int, num_paths: int) -> np.ndarray:
    raise NotImplementedError("Subclasses will implement the path generation")

class GeometricBrownianMotion(StochasticProcess):
  def __init__(self, rate: float, vol: float):
    self.rate = rate
    self.vol = vol

  def generate_paths(self, spot: float, maturity: float, num_steps: int, num_paths: float):
    dt = maturity / num_steps
    paths = np.zeros((num_paths, num_steps + 1))
    paths[:,0] = spot

    Z = np.random.standard_normal((num_paths, num_steps))

    drift = (self.rate - 0.5 * (self.vol ** 2)) * dt

    for i in range(1, num_steps + 1):
      diffusion = self.vol * np.sqrt(dt) * Z[:,i - 1]

      paths[:, i] = paths[:, i - 1] * np.exp(drift + diffusion)

    return paths

    
    
    