import numpy as np
import pickle
from logistic_regression import LogisticRegression
import utilities

features = utilities.load_features()
X_raw, y_raw = utilities.load_samples(features)
iter_count = 2000
alpha = 10.0
cross_division = 5
m = len(features)

def cross_validation(n: int = 0):
  X_set = np.array_split(X_raw, n)
  y_set = np.array_split(y_raw, n)
  results = []

  for i in range(n):
    # 学習データ、学習ラベル
    X_train = np.empty((0, m))
    y_train = np.array([])
    for j, X in enumerate(X_set):
      if j == i: continue
      X_train = np.vstack([X_train, X])
      y_train = np.hstack([y_train, y_set[j]])
    X_train = np.insert(X_train, 0, 1, axis=1)
    # テストデータ、テストラベル
    X_test = X_set[i]
    X_test = np.insert(X_test, 0, 1, axis=1)
    y_test = y_set[i]

    initial_theta = np.zeros(m+1)

    print('Cross={}/{}'.format(i+1, cross_division))
    print('X_train={}, X_test={}, y_train={}, y_test={}'.format(
      X_train.shape, X_test.shape, y_train.shape, y_test.shape))

    learner = LogisticRegression(X_train, y_train, initial_theta, alpha)
    learner.learn(count=iter_count)
    learner.X = X_test
    learner.y = y_test
    result = learner.benchmark()
    print('accuracy={}, precision={}, recall={}, f1={}'.format(
      result[0], result[1], result[2], result[3]))
    results.append(result)
    print('')

  return results

results = cross_validation(cross_division)
results = np.array(results).mean(axis=0)

accuracy = results[0]
precision = results[1]
recall = results[2]
f1 = results[3]

print('Learning rate={}, iteration={}, cross division={}'.format(alpha, iter_count, cross_division))
print('accuracy avg\t{}'.format(accuracy))
print('precision avg\t{}'.format(precision))
print('recall avg\t{}'.format(recall))
print('f1 avg\t{}'.format(f1))
