import sys

path = 'hightemp.txt'
max_count = int(sys.argv[1])

with open(path, 'r') as fp:
  lines = fp.readlines()
  for line in lines[-max_count:]:
    print(line.rstrip())
