from analyzer import Analyzer

path = 'neko.txt.mecab'

analyzer = Analyzer(path)
analyzer.convert()
sahen_nouns = []

for word in analyzer.words:
  if 'サ変' not in word['pos1']: continue
  sahen_nouns.append(word)

print(sahen_nouns)
print(len(sahen_nouns))
