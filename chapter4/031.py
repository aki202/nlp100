from analyzer import Analyzer

path = 'neko.txt.mecab'

analyzer = Analyzer(path)
sentences = analyzer.convert()

verb_surfaces = []
for word in analyzer.words:
  if word['pos'] != '動詞': continue
  verb_surfaces.append(word['surface'])

print(list(set(verb_surfaces)))
