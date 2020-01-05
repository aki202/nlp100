from analyzer import Analyzer
from pprint import pprint

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
pprint(sorted_words[0:50])
