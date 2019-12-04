path = 'hightemp.txt'

with open(path, 'r') as fp:
  lines = fp.readlines()
  print(len(lines))
