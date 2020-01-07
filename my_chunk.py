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
