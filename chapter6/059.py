from xml.etree import ElementTree
import re

tree = ElementTree.parse('./nlp.txt.xml')
root = tree.getroot()

pattern = re.compile(r'\((.+) (.+)\)')

def extract_sentence(parse: str, np_list: list):
  m = re.match(r'^\(([a-zA-Z,\.\d-]+?) +(.+)\)$', parse)
  if m == None: return parse
  tag = m[1]
  rest = m[2]

  if not rest[0] == '(': return rest

  depth = 0
  tmp = ''
  parts = []
  for c in rest:
    if depth == 0 and c == ' ': continue
    tmp += c
    if c == '(':
      depth += 1
      continue
    if c == ')':
      depth -= 1
      if depth == 0:
        parts.append(extract_sentence(tmp, np_list))
        tmp = ''
      continue

  word = ' '.join(parts)
  if tag == 'NP': np_list.append(word)
  return word

for parse in root.iter('parse'):
  np_list = []
  extract_sentence(parse.text.strip(), np_list)
  print('\n'.join(np_list))
