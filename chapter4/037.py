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
x = [sorted_word[0] for sorted_word in sorted_words[0:50]]
y = [sorted_word[1] for sorted_word in sorted_words[0:50]]

x.reverse()
y.reverse()

plt.figure(figsize=(9, 10))
plt.rcParams['font.family'] = 'Hiragino Maru Gothic Pro'
plt.barh(x, y)
plt.xlabel('頻度 [回]')
plt.ylabel('単語')
plt.show()
