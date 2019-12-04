import random

#string = 'The best way to predict the future is to invent it .'
string = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

words = string.split(' ')
for index, word in enumerate(words):
  if len(word) <= 4: continue
  chars = list(word[1:-1])
  random.shuffle(chars)
  words[index] = word[0] + ''.join(chars) + word[-1]

print(' '.join(words))
