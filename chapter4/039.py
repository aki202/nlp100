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

sorted_words = sorted(words.items(), key=lambda word: word[1], reverse=True)
counts = [w[1] for w in sorted_words]
ranks = list(range(1, len(counts)+1))

plt.rcParams['font.family'] = 'Hiragino Maru Gothic Pro'
plt.scatter(ranks, counts)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('順番 [log]')
plt.ylabel('出現頻度 [log]')
plt.show()
