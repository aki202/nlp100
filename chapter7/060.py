import redis
import json

r = redis.Redis(host='localhost', port=6378, db=0)

with open('artist.json', 'r') as fp:
  i = 1
  for line in fp:
    artist = json.loads(line)
    key = '%s-%d' % (artist['name'], artist['id'])
    r.hset(key, 'id', artist['id'])
    r.hset(key, 'name', artist['name'])
    r.hset(key, 'area', artist.get('area', ''))
    print('[%d] %s Inserted' % (i, artist['name']))
    i += 1
