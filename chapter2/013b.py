import re

path = 'outputs/col1_col2.txt'
one_col_path = 'col1.txt'
two_col_path = 'col2.txt'

with open(one_col_path, 'r') as col1_fp, \
     open(two_col_path, 'r') as col2_fp, \
     open(path, 'w') as out_fp:
  for (col1_line, col2_line) in zip(col1_fp, col2_fp):
    out_fp.write(col1_line.rstrip() + '\t' + col2_line.rstrip() + '\n')
