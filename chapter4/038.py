import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from analyzer import Analyzer
from pprint import pprint
import matplotlib.pyplot as plt

path = 'neko.txt.mecab'

analyzer = Analyzer(path)
analyzer.convert()
words = {}

for index, word in enumerate(analyzer.words):
  key = '{}-{}'.format(word['surface'], word['pos'])
  if key in words:
    words[key] += 1
  else:
    words[key] = 1

plt.figure(figsize=(8, 10))
plt.rcParams['font.family'] = 'Hiragino Maru Gothic Pro'
plt.hist(words.values(), bins=30, range=(1, 30))
plt.xlabel('単語の種類数')
plt.ylabel('出現頻度')
plt.show()
