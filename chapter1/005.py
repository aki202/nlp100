def n_gram(s, n):
  return [ s[index:index+n] for index in range(len(s)-n+1) ]

string = 'I am an NLPer'
print(string)

print(n_gram(string, 1))
print(n_gram(string, 2))
print(n_gram(string, 3))

words = 'I am an NLPer'.split(' ')
print(n_gram(words, 1))
print(n_gram(words, 2))
print(n_gram(words, 3))
