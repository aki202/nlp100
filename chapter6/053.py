from xml.etree import ElementTree

# corenlp.sh -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -file nlp.txt

tree = ElementTree.parse('./nlp.txt.xml')
root = tree.getroot()
for word in root.iter('word'):
  print(word.text)
