import sys
import math

path = 'hightemp.txt'
divider = int(sys.argv[1])

with open(path, 'r') as fp:
  lines = fp.readlines()

each_max = math.ceil(len(lines) / divider)
for i in range(divider):
  begin = i * each_max
  end = each_max + begin
  print("-----block={} begin={}, end={}-----".format(i, begin, end))
  for line in lines[begin:end]:
    print(line.rstrip())
