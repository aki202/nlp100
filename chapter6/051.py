import reader

for index, word in enumerate(reader.words()):
  if word == None:
    print('')
  else:
    print(word)
    #print('[%d] %s' % (index, word))
