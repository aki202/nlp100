from xml.etree import ElementTree

tree = ElementTree.parse('./nlp.txt.xml')
root = tree.getroot()
for word in root.iter('word'):
  print(word.text)
