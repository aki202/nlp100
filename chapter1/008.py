import re

def cipher(s):
  result = ''
  for c in s:
    if re.match('[a-z]', c):
      result += chr(219 - ord(c))
    else:
      result += c
  return result

#string = input('Enter phrase: ')
string = '姓はIcebahn、名はForkだ。'
print('Raw:', string)
encoded = cipher(string)
print('Encoded: ', encoded)
decoded = cipher(encoded)
print('Decoded: ', decoded)
