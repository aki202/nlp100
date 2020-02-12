import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import re

path = 'nlp.txt'

def sentences():
  with open(path, 'r') as fp:
    for line in fp.readlines():
      for match in re.findall('[A-Z\d].*?[.;:?!\n]', line):
        yield match.strip()

for index, sentence in enumerate(sentences()):
  print('[%d] %s' % (index, sentence))
