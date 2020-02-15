from xml.etree import ElementTree

tree = ElementTree.parse('./nlp.txt.xml')
root = tree.getroot()
for token in root.iter('token'):
  word  = token.find('word').text
  lemma = token.find('lemma').text
  pos   = token.find('POS').text
  print('%s\t%s\t%s' % (word, lemma, pos))
