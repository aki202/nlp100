import reader

for index, word in enumerate(reader.words()):
  print('[%d] %s' % (index, word))
