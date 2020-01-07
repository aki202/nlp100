import re

class Morph():
  def __init__(self, surface, base, pos, pos1):
    self.surface = surface
    self.base = base
    self.pos = pos
    self.pos1 = pos1

    #self.surface = elements[0]
    #self.base = elements[7]
    #self.pos = elements[1]
    #self.pos1 = elements[2]

  def __repr__(self):
    return str(self.__dict__)
