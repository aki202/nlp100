import re
path = 'hightemp.txt'

with open(path, 'r') as fp:
  body = re.sub('\t', ' ', fp.read())
  print(body)
