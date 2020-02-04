import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from cabocha_analyzer import CabochaAnalyzer
from morph import Morph
from my_chunk import Chunk

path = 'neko.txt.cabocha'

analyzer = CabochaAnalyzer(path)
sentences = analyzer.convert()

def get_sahen_wo_indexes(sentence: [Chunk]) -> [int]:
  indexes = []
  for i, chunk in enumerate(sentence):
    for j, morph in enumerate(chunk.morphs):
      if morph.pos != '名詞': continue
      if morph.pos1 != 'サ変接続': continue
      if j+1 >= len(chunk.morphs): continue
      if chunk.morphs[j+1].pos != '助詞': continue
      if chunk.morphs[j+1].surface != 'を': continue
      indexes.append(i)
  return indexes

def get_target_verb(sahen_wo: Chunk, sentence: [Chunk]) -> (Morph, Chunk):
  if sahen_wo.dst == None: return None
  dst_chunk = sentence[sahen_wo.dst]
  verbs = dst_chunk.get_morphs_of(['動詞'])
  if len(verbs) == 0: return None
  return (verbs[0], dst_chunk)

for sentence in sentences:
  sahen_wo_indexes = get_sahen_wo_indexes(sentence)
  for sahen_wo_index in sahen_wo_indexes:
    sahen_wo = sentence[sahen_wo_index]
    target_verb = get_target_verb(sahen_wo, sentence)
    if target_verb == None: continue
    target_morph = target_verb[0]
    target_chunk = target_verb[1]

    src_particles = []
    src_chunks = [c for i, c in enumerate(sentence) \
      if i in target_chunk.srcs and i != sahen_wo_index ]
    for src_chunk in src_chunks:
      particle = src_chunk.get_joshi()
      if particle == None: continue
      src_particles.append((src_chunk, particle))
    if len(src_particles) == 0: continue

    src_particles.sort(key=lambda src_particle : src_particle[1].base)
    src_particle_bases = [src_particle[1].base for src_particle in src_particles]
    src_particle_phrases = [src_particle[0].joined_morphs() for src_particle in src_particles]
    print('{}{}\t{}\t{}'.format( \
      sahen_wo.joined_morphs(), \
      target_morph.base, \
      ' '.join(src_particle_bases), \
      ' '.join(src_particle_phrases) \
    ))
