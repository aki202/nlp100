from analyzer import Analyzer

path = 'neko.txt.mecab'

analyzer = Analyzer(path)
sentences = analyzer.convert()

verb_bases = []
for word in analyzer.words:
  if word['pos'] != '動詞': continue
  verb_bases.append(word['base'])

print(list(set(verb_bases)))
