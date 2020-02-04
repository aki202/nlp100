import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from cabocha_analyzer import CabochaAnalyzer
from morph import Morph
from my_chunk import Chunk
from utilities import extracter

path = 'neko.txt.cabocha'

analyzer = CabochaAnalyzer(path)
sentences = analyzer.convert()

def get_list_to_end(sentence: [Chunk], start: int) -> [Chunk]:
  if start == None: return []
  result = [sentence[start]]
  result.extend(get_list_to_end(sentence, sentence[start].dst))
  return result

line = 5
for sentence in sentences[line: line+1]:
  #extracter.inspect_sentence(sentence)
  for index, chunk in enumerate(sentence):
    nouns = chunk.get_morphs_of(['名詞'])
    if len(nouns) == 0: continue

    chunks = get_list_to_end(sentence, index)
    print(' -> '.join([chunk.joined_morphs() for chunk in chunks]))
