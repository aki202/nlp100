from morph import Morph
from my_chunk import Chunk

# Morphの配列から特定の品詞を抽出
def morphs(morphs:[Morph], pos:str) -> [Morph]:
  return [m for m in morphs if m.pos == pos]

# Sentence(Chunkの配列)の詳細を表示
def inspect_sentence(sentence: [Chunk]):
  for i, chunk in enumerate(sentence):
    print('{} {}\t{}\t{}\t{}:'.format(i,
      chunk.joined_morphs(),
      '\t'.join(["{} {} {}".format(m.surface, m.pos, m.pos1) for m in chunk.morphs]), \
      chunk.dst, \
      chunk.srcs
    ))

# ２つのChunkから共通のChunkの文節番号を見つける
def get_common_chunk_idx(sentence: [Chunk], index_a: int, index_b: int) -> int:
  while True:
    index_a = sentence[index_a].dst
    if index_a == None: break
    while True:
      index_b = sentence[index_b].dst
      if index_b == None: return None
      if index_a == index_b: return index_a
  return None

# Sentence(Chunkの配列)よりstartからendまで、dstを辿ってChunkの連なりを取得
def get_chunks_from_start_to_end(sentence: [Chunk], start: int, end: int = None) -> [Chunk]:
  if start == None: return []
  if start == end: return []
  result = [sentence[start]]
  result.extend(get_chunks_from_start_to_end(sentence, sentence[start].dst, end))
  return result
