from analyzer import Analyzer

path = 'neko.txt.mecab'

sentences = Analyzer(path).convert()

print(sentences[0])
print(sentences[1])
print(sentences[2])
