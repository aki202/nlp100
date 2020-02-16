from xml.etree import ElementTree
from pydot import Dot, Node, Edge
from PIL import Image

graph = Dot(graph_type='digraph')
tree = ElementTree.parse('./nlp.txt.xml')
root = tree.getroot()
sentence = root.find('.//sentence[@id="3"]')
nodes = {int: Node}

def add_node(id, element, nodes, graph):
  if id in nodes: return
  node = Node(id, label=' %s ' % element.text)
  nodes[id] = node
  graph.add_node(node)

for dep in sentence.iterfind('.//dependencies[@type="collapsed-dependencies"]/dep'):
  governor = dep.find('governor')
  dependent = dep.find('dependent')
  governor_id = int(governor.get('idx'))
  dependent_id = int(dependent.get('idx'))
  graph.add_edge(Edge(governor_id, dependent_id))
  add_node(governor_id, governor, nodes, graph)
  add_node(dependent_id, dependent, nodes, graph)
graph.write_png('outputs/057.png')
Image.open('outputs/057.png').show()
