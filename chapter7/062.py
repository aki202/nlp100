import redis
import re

r = redis.Redis(host='localhost', port=6378, db=0)

q = input('Area: ')

hits = 0
for key in r.keys('*'):
  area = r.hget(key, 'area').decode()
  if not re.match(q, area): continue

  id = int(r.hget(key, 'id').decode())
  name = r.hget(key, 'name').decode()
  print('id=%d, name=%s, area=%s'% (id, name, area))
  hits += 1

print('Matched count=%d' % hits)
