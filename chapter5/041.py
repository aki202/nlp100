import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from cabocha_analyzer import CabochaAnalyzer
from pprint import pprint

path = 'neko.txt.cabocha'

analyzer = CabochaAnalyzer(path)
sentences = analyzer.convert()

for i in range(7, 8):
  for j, chunk in enumerate(sentences[i]):
    print("i:{}, dst:{}, srcs:[{}], ".format(j, chunk.dst, ','.join(map(str, chunk.srcs))), end='')
    print("{}".format( ' / '.join([morph.surface for morph in chunk.morphs]) ))
