from analyzer import Analyzer

path = 'neko.txt.mecab'

analyzer = Analyzer(path)
analyzer.convert()
rensetsu_list = []
new_rensetsu_list = []

for index, word in enumerate(analyzer.words):
  if word['pos'] != '名詞':
    if len(new_rensetsu_list) > 1:
      rensetsu = ''.join([word['surface'] for word in new_rensetsu_list])
      rensetsu_list.append(rensetsu)
    new_rensetsu_list = []
    continue
  new_rensetsu_list.append(word)

rensetsu_list = list(set(rensetsu_list))
print(rensetsu_list[0:40])
print(len(rensetsu_list))
