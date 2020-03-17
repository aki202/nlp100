import numpy as np
import pickle
import utilities

features = np.array(utilities.load_features())

with open('outputs/sentiment_weight.pkl', mode='rb') as fp:
  theta = pickle.load(fp)
  theta = theta[1:,]

indexes = np.argsort(theta)
bad_indexes = indexes[0:10]
good_indexes = indexes[:-11:-1]

print('Good')
for i in good_indexes:
  print('{} ({})'.format(features[i], theta[i]))

print('')
print('Bad')
for i in bad_indexes:
  print('{} ({})'.format(features[i], theta[i]))
