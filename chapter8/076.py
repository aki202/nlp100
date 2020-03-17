import numpy as np
import pickle
from logistic_regression import LogisticRegression
import utilities

features = utilities.load_features()
X, y = utilities.load_samples(features)
X = np.insert(X, 0, 1, axis=1)

with open('outputs/sentiment_weight.pkl', mode='rb') as fp:
  theta = pickle.load(fp)

learner = LogisticRegression(X, y, theta, 0)

with open('outputs/sentiment_result.txt', 'w') as fp:
  for i, hy in enumerate(learner.hypothesis()):
    ans = '+1' if y[i] == 1 else '-1'
    if hy >= 0.5:
      line = "+1\t{}\t{}\n".format(ans, hy)
    else:
      line = "-1\t{}\t{}\n".format(ans, 1 - hy)
    fp.write(line)
    print(line, end='')

