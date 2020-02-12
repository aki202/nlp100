import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import re

path = 'nlp.txt'

def sentences():
  with open(path, 'r') as fp:
    for line in fp.readlines():
      line = line.strip()
      while len(line) > 0:
        line = line.strip()
        match = re.match(r'(.+?[.;:?!]) ([A-Z\d].*)', line)
        if match == None:
          yield line
          break
        else:
          yield match[1]
          line = match[2]

def words():
  for sentence in sentences():
    for word in re.split(' ', sentence):
      word = re.sub('[^\w]', '', word)
      if len(word) == 0: next
      yield word
    yield "\n"
