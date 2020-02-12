import reader

for index, sentence in enumerate(reader.sentences()):
  print('[%d] %s' % (index, sentence))
