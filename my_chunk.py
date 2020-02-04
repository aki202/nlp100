import re
from morph import Morph

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

  # 形態素の配列を一部置換を行い文字列に変換
  def joined_replaced_morphs(self, pos: str, replacement: str, end_at_pos: bool = False, glue=''):
    surfaces = []
    for morph in self.morphs:
      if morph.pos == '記号': continue
      if morph.pos == pos:
        surfaces.append(replacement)
        if end_at_pos: break
        continue
      surfaces.append(morph.surface)
    return glue.join(surfaces)

  # 引数の形態素を持つかどうか
  def has_morph_of(self, pos):
    filtered_morphs = [m for m in self.morphs if m.pos == pos]
    return len(filtered_morphs) > 0

  # 引数の品詞リストに適合する形態素を返す
  def get_morphs_of(self, pos_list: [str]) -> [Morph]:
    return [m for m in self.morphs if m.pos in pos_list]

  # 助詞を返す。複数ある場合は一番最後の形態素
  def get_joshi(self) -> Morph:
    candidates = self.get_morphs_of(['助詞'])
    if len(candidates) == 0: return None
    return candidates[-1]
