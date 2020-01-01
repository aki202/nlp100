import sys
from itertools import groupby

path = 'hightemp.txt'

with open(path, 'r') as fp:
  lines = fp.readlines()

lines = [line.strip().split() for line in lines]
lines.sort(key=lambda line: line[0])

states = []
for key, group in groupby(lines, key=lambda line: line[0]):
  states.append([key, len(list(group))])

states.sort(key=lambda state: state[1], reverse=True)
for state in states:
  print("{}, count={}".format(state[0], state[1]))
