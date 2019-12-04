import re

path = 'outputs/col1_col2.txt'
one_col_path = 'col1.txt'
two_col_path = 'col2.txt'
lines = []
one_col_lines = []
two_col_lines = []

with open(one_col_path, 'r') as fp:
  one_col_lines = fp.readlines()

with open(two_col_path, 'r') as fp:
  two_col_lines = fp.readlines()

for index in range(len(one_col_lines)):
  lines.append("{0}\t{1}".format(
    re.sub('[\r\n]', '', one_col_lines[index]),
    re.sub('[\r\n]', '', two_col_lines[index])
  ))

with open(path, 'w') as fp:
  fp.write('\n'.join(lines))
  fp.write('\n')
