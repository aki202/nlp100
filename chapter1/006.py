def n_gram(s, n):
  return [ s[index:index+n] for index in range(len(s)-n+1) ]

x_str = 'paraparaparadise'
y_str = 'paragraph'
x = set(n_gram(x_str, 2))
y = set(n_gram(y_str, 2))

print('x', x)
print('y', y)
print('x | y', x | y)
print('x & y', x & y)
print('x - y', x - y)
print('y - x', y - x)
print('x includes "se?"', {'se'} <= x)
print('y includes "se?"', {'se'} <= y)
