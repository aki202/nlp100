import re

class Chunk():
  def __init__(self, morphs, dst, srcs):
    self.morphs = morphs
    dst = int(re.sub(r'[^\d-]', '', dst))
    self.dst = None if dst < 0 else dst
    self.srcs = srcs

  def rehresh(self):
    return

  def __repr__(self):
    return str(self.__dict__)

  # 形態素の配列を文字列に変換
  def joined_morphs(self, glue=''):
    return glue.join([m.surface for m in self.morphs if m.pos != '記号'])

  # 引数の形態素を持つかどうか
  def has_morph_of(self, pos):
    filtered_morphs = [m for m in self.morphs if m.pos == pos]
    return len(filtered_morphs) > 0
