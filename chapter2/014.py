import sys

path = 'hightemp.txt'
max_count = int(sys.argv[1])

with open(path, 'r') as fp:
  for index, line in enumerate(fp):
    if index == max_count: break
    print(line.rstrip())
