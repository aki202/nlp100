import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from cabocha_analyzer import CabochaAnalyzer
from pprint import pprint

path = 'neko.txt.cabocha'

analyzer = CabochaAnalyzer(path)
sentences = analyzer.convert()

for i in range(0, 5):
  for chunk in sentences[i]:
    if chunk.dst == None: continue
    target_chunk = sentences[i][chunk.dst]
    print("{}\t{}".format(chunk.joined_morphs(), target_chunk.joined_morphs()))
