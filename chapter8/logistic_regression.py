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

  # Accuracy, Precision, Recall, F1値を返す
  def benchmark(self, threshold: float = 0.5):
    hyp = (self.hypothesis() >= threshold).astype(np.int)
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    for i, predict in enumerate(hyp):
      label = self.y[i]
      if predict == label:
        if predict == 1:
          TP += 1
        else:
          TN += 1
      else:
        if predict == 1:
          FP += 1
        else:
          FN += 1

    accuracy = (TP + TN) / (TP + TN + FP + FN) # 正解率
    precision = TP / (TP + FP) # 適合率、予測の中に正解がどれだけ含まれているか
    recall = TP / (TP + FN) # 再現率、正解全体がどれだけ予測されているか
    f1 = (2 * precision * recall) / (precision + recall)
    return [accuracy, precision, recall, f1]
