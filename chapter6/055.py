from xml.etree import ElementTree

tree = ElementTree.parse('./nlp.txt.xml')
root = tree.getroot()
for token in root.iterfind('.//sentences//token[NER="PERSON"]'):
  word  = token.find('word').text
  print('%s' % word)
