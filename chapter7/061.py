import redis

r = redis.Redis(host='localhost', port=6378, db=0)

q = input('Artist name: ')

hits = 0
for key in r.keys('%s*' % q):
  id = int(r.hget(key, 'id').decode())
  name = r.hget(key, 'name').decode()
  area = r.hget(key, 'area').decode()
  print('id=%d, name=%s, area=%s'% (id, name, area))
  hits += 1

if hits == 0: print('No artists for "%s"' % q)
