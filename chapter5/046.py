import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from cabocha_analyzer import CabochaAnalyzer
from morph import Morph

path = 'neko.txt.cabocha'

analyzer = CabochaAnalyzer(path)
sentences = analyzer.convert()

def extract_morphs(morphs:[Morph], pos:str) -> [Morph]:
  return [m for m in morphs if m.pos == pos]

for sentence in sentences:
#for sentence in sentences[5:6]:
  for chunk in sentence:
    verbs = extract_morphs(chunk.morphs, '動詞')
    if len(verbs) == 0: continue

    src_particles = []
    src_chunks = [c for i, c in enumerate(sentence) if i in chunk.srcs]
    for src_chunk in src_chunks:
      particles = extract_morphs(src_chunk.morphs, '助詞')
      src_particles.extend([(src_chunk, m) for m in particles])
    if len(src_particles) == 0: continue

    src_particles.sort(key=lambda src_particle : src_particle[1].base)
    src_particle_bases = [src_particle[1].base for src_particle in src_particles]
    src_particle_phrases = [src_particle[0].joined_morphs() for src_particle in src_particles]
    verb_base = verbs[0].base
    print('{}\t{}\t{}'.format( \
      verb_base, \
      ' '.join(src_particle_bases), \
      ' '.join(src_particle_phrases) \
    ))
