from analyzer import Analyzer

path = 'neko.txt.mecab'

analyzer = Analyzer(path)
analyzer.convert()
rentaishi_list = []

for index, word in enumerate(analyzer.words):
  if word['surface'] != 'の': continue
  if analyzer.words[index-1]['pos'] != '名詞': continue
  if analyzer.words[index+1]['pos'] != '名詞': continue
  rentaishi_list.append(analyzer.words[index-1]['surface'] + \
                        'の' + \
                        analyzer.words[index+1]['surface'])

rentaishi_list = list(set(rentaishi_list))
print(rentaishi_list)
print(len(rentaishi_list))
