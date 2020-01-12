import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from cabocha_analyzer import CabochaAnalyzer
from my_chunk import Chunk
from PIL import Image
from pydot import Dot, Node, Edge

path = 'neko.txt.cabocha'

analyzer = CabochaAnalyzer(path)
sentences = analyzer.convert()

def chunk_map(sentences: [Chunk]) -> Dot:
  graph = Dot(graph_type='graph')
  nodes = []
  for i, chunk in enumerate(sentences):
    node = Node(i, label=chunk.joined_morphs())
    graph.add_node(node)
    if chunk.dst == None: continue
    edge = Edge(i, chunk.dst)
    graph.add_edge(edge)
  return graph

graph = chunk_map(sentences[8])
#graph = chunk_map(max(sentences, key=lambda s: len(s)))
graph.write_png('outputs/044.png')
Image.open('outputs/044.png').show()
