import re
path = 'hightemp.txt'
one_col_path = 'col1.txt'
two_col_path = 'col2.txt'

one_col_lines = []
two_col_lines = []

with open(path, 'r') as fp:
  lines = fp.readlines()
  for line in lines:
    items = line.split('\t')
    one_col_lines.append(items[0])
    two_col_lines.append(items[1])

with open(one_col_path, 'w') as fp:
  fp.write('\n'.join(one_col_lines))

with open(two_col_path, 'w') as fp:
  fp.write('\n'.join(two_col_lines))
