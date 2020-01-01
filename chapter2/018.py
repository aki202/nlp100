import sys
import math

path = 'hightemp.txt'

with open(path, 'r') as fp:
  lines = fp.readlines()

sorted_lines = sorted(lines, reverse=True, key=lambda line : float(line.split()[2].rstrip()))

for line in sorted_lines:
  print(line.rstrip())
