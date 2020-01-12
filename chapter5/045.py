import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from cabocha_analyzer import CabochaAnalyzer
from morph import Morph
from pprint import pprint

path = 'neko.txt.cabocha'

analyzer = CabochaAnalyzer(path)
sentences = analyzer.convert()
pairs = {str: [str]}

def extract_morphs(morphs:[Morph], pos:str) -> [Morph]:
  return [m for m in morphs if m.pos == pos]

for sentence in sentences:
#for sentence in sentences[0:10]:
  for chunk in sentence:
    verbs = extract_morphs(chunk.morphs, '動詞')
    if len(verbs) == 0: continue

    src_particles = []
    src_chunks = [c for i, c in enumerate(sentence) if i in chunk.srcs]
    for src_chunk in src_chunks:
      particles = extract_morphs(src_chunk.morphs, '助詞')
      src_particles.extend([p.base for p in particles])
    if len(src_particles) == 0: continue

    src_particles.sort()
    verb_base = verbs[0].base
    if not verb_base in pairs: pairs[verb_base] = []
    pairs[verb_base].extend(src_particles)
    print('{}\t{}'.format(verb_base, ' '.join(src_particles)))
