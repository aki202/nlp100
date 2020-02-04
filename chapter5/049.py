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

def replace_surfaces(chunks: [Chunk], pos: str, replacement: str) -> [str]:
  surfaces = []

  if morph.pos != pos: return morph.surface
  return surfaces

line = 5
for sentence in sentences[line: line+1]:
  #extracter.inspect_sentence(sentence)
  for index_x, chunk_x in enumerate(sentence):
    nouns_x = chunk_x.get_morphs_of(['名詞'])
    if len(nouns_x) == 0: continue

    for index_y in range(index_x+1, len(sentence)):
      chunk_y = sentence[index_y]
      nouns_y = chunk_y.get_morphs_of(['名詞'])
      if len(nouns_y) == 0: continue

      common_idx = extracter.get_common_chunk_idx(sentence, index_x, index_y)

      # 共通文節がある場合
      if common_idx != None:
        chunks_x = extracter.get_chunks_from_start_to_end(sentence, index_x, common_idx)
        chunks_y = extracter.get_chunks_from_start_to_end(sentence, index_y, common_idx)

        surfaces_x = [chunks_x[0].joined_replaced_morphs(pos='名詞', replacement='X')]
        surfaces_x.extend([chunk.joined_morphs() for chunk in chunks_x[1:]])
        print(' -> '.join(surfaces_x), end=' | ')

        surfaces_y = [chunks_y[0].joined_replaced_morphs(pos='名詞', replacement='Y')]
        surfaces_y.extend([chunk.joined_morphs() for chunk in chunks_y[1:]])
        print(' -> '.join(surfaces_y), end=' | ')

        print(sentence[common_idx].joined_morphs())

      # 共通文節がない場合
      else:
        chunks = extracter.get_chunks_from_start_to_end(sentence, index_x, index_y)
        surfaces = [chunks[0].joined_replaced_morphs(pos='名詞', replacement='X')]
        surfaces.extend([chunk.joined_morphs() for chunk in chunks[1:]])
        surfaces.append(sentence[index_y].joined_replaced_morphs(pos='名詞', replacement='Y', end_at_pos=True))
        print(' -> '.join(surfaces))
