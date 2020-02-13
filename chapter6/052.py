import reader
from stemming.porter2 import stem

for word in reader.words():
  if word == None:
    print('')
    continue

  stem_word = stem(word)
  print('%s\t%s' % (word, stem_word))
