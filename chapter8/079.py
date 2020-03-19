import numpy as np
import pickle
from logistic_regression import LogisticRegression
import utilities
import matplotlib.pyplot as plt

with open('outputs/sentiment_weight.pkl', mode='rb') as fp:
  theta = pickle.load(fp)

features = utilities.load_features()
X, y = utilities.load_samples(features)
X = np.insert(X, 0, 1, axis=1)

learner = LogisticRegression(X, y, theta, 0)

thresholds = np.arange(0, 1, 0.05)
accuracies = []
precisions = []
recalls = []
f1s = []

for threshold in thresholds:
  result = learner.benchmark(threshold)
  print('accuracy={}, precision={}, recall={}, f1={}'.format(
    result[0], result[1], result[2], result[3]))
  accuracies.append(result[0])
  precisions.append(result[1])
  recalls.append(result[2])
  f1s.append(result[3])

#plt.figure(figsize=(9, 10))
plt.rcParams['font.family'] = 'Hiragino Maru Gothic Pro'
plt.plot(thresholds, accuracies, label="Accuracy")
plt.plot(thresholds, precisions, label="Precision")
plt.plot(thresholds, recalls, label="Recall")
plt.plot(thresholds, f1s, label="F1")
plt.xlabel('閾値')
plt.ylabel('制度')
plt.legend()
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.show()
