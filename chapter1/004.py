import re

string = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
string = re.sub('[^a-z ]', '', string, 0, re.IGNORECASE)
words = string.split(' ')

one_selections = [0, 4, 5, 6, 7, 8, 14, 15, 18]
extractions = []
for index, word in enumerate(words):
  selection = 1 if index in one_selections else 2
  extractions.append(word[0:selection])

print(extractions)
