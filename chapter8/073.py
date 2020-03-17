import numpy as np
import pickle
from logistic_regression import LogisticRegression
import utilities

features = utilities.load_features()
X, y = utilities.load_samples(features)
X = np.insert(X, 0, 1, axis=1)
m = len(features)
initial_theta = np.zeros(m+1)

print('features={}'.format(len(features)))
print('X={}'.format(X.shape))
print('y={}'.format(y.shape))
print('initial_theta={}'.format(initial_theta.shape))

learner = LogisticRegression(X, y, initial_theta, 10.0)
learner.learn(count=2000)

with open('outputs/sentiment_weight.pkl', mode='wb') as fp:
  pickle.dump(learner.theta, fp)
