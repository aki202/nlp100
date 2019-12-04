import re

string = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
string = re.sub('[^a-z ]', '', string, 0, re.IGNORECASE)
words = string.split(' ')
characters = [len(word) for word in words]
print(words)
print(characters)
