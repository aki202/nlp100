import sys
import math

path = 'hightemp.txt'
all_kinds = []

with open(path, 'r') as fp:
  for line in fp.readlines():
    all_kinds.append(line.split()[0])

kinds = list(set(all_kinds))
for kind in kinds:
  print(kind)
