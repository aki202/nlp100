import sys
import re

class Analyzer():
  def __init__(self, path):
    self.path = path
    self.words = []

  def convert(self):
    with open(self.path, 'r') as fp:
      lines = fp.readlines()

    sentences = []
    new_sentences = []

    for index, line in enumerate(lines):
      converted = self.each(line)
      if converted == None:
        if len(new_sentences) > 0: sentences.append(new_sentences)
        new_sentences = []
        continue
      new_sentences.append(converted)
      self.words.append(converted)

    return sentences

  def each(self, line):
    new_line = line.strip()
    if new_line == 'EOS': return None
    elements = re.split(r'[\t,]', new_line)
    return {
      'surface': elements[0],
      'base': elements[7],
      'pos': elements[1],
      'pos1': elements[2],
    }
