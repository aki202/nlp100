import numpy as np

class LogisticRegression:
  def __init__(self, X, y, initial_theta, alpha):
    self.X = X
    self.y = y
    self.theta = initial_theta
    self.alpha = alpha
    self.m = X.shape[0]

  def hypothesis(self) -> []:
    z = np.dot(self.X, self.theta)
    return 1 / (1 + np.exp(-z))

  def cost(self) -> int:
    h = self.hypothesis()
    return 1/self.m * (-np.dot(self.y, np.log(h)) - np.dot(1-self.y, np.log(1-h)))

  def update_theta(self) -> []:
    h = self.hypothesis()
    self.theta -= self.alpha/self.m * np.dot(h-self.y, self.X)
    return self.theta

  def learn(self, count = 1000):
    for i in range(count+1):
      if i % 100 == 0: print('Iter={}, Cost={}'.format(i, self.cost()))
      self.update_theta()
