import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from cabocha_analyzer import CabochaAnalyzer
from pprint import pprint

path = 'neko.txt.cabocha'

analyzer = CabochaAnalyzer(path)
sentences = analyzer.convert()

for i in range(0, 20):
  for chunk in sentences[i]:
    if not chunk.has_morph_of('名詞'): continue
    if chunk.dst == None: continue
    target_chunk = sentences[i][chunk.dst]
    if not target_chunk.has_morph_of('動詞'): continue
    print("{}\t{}".format(chunk.joined_morphs(), target_chunk.joined_morphs()))
