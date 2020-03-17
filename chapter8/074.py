import numpy as np
import pickle
from logistic_regression import LogisticRegression
import utilities

features = utilities.load_features()

with open('outputs/sentiment_weight.pkl', mode='rb') as fp:
  theta = pickle.load(fp)

sentence = input('Input your review: ')
vec = utilities.sentence2vec(sentence, features)
X = np.array([vec])
X = np.insert(X, 0, 1, axis=1)

predicter = LogisticRegression(X, [0], theta, 0)
predict = predicter.hypothesis()[0]
if predict >= 0.5:
  rate = '+1'
  prob = predict
else:
  rate = '-1'
  prob = 1 - predict

print('Rate: {} ({})'.format(rate, prob))
