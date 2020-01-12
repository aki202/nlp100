from morph import Morph
from my_chunk import Chunk
from pprint import pprint
import re

class CabochaAnalyzer():
  def __init__(self, path):
    self.path = path

  def convert_to_sentences(self, lines):
    sentences = []
    new_chunks = []
    new_chunk = None
    for line in lines:
      line = line.rstrip()
      elements = re.split(r'[\t, ]', line)
      # 終端記号
      if elements[0] == 'EOS':
        if len(new_chunks) == 0: continue
        for index, chunk in enumerate(new_chunks):
          if chunk.dst == None: continue
          new_chunks[chunk.dst].srcs.append(index)
        sentences.append(new_chunks)
        new_chunks = []
      # 文節
      elif elements[0] == '*':
        new_chunk = Chunk([], elements[2], [])
        new_chunks.append(new_chunk)
      # 形態素
      else:
        new_morph = Morph(
          surface = elements[0],
          base    = elements[7],
          pos     = elements[1],
          pos1    = elements[2],
        )
        new_chunk.morphs.append(new_morph)
    return sentences

  def convert(self):
    with open(self.path, 'r') as fp:
      lines = fp.readlines()

    senteces = self.convert_to_sentences(lines)
    return senteces
