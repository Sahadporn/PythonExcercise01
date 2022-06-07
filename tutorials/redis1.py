import redis
import arrow

redis_uri = 'redis://:localhost@root:6379/0'

client = redis.StrictRedis(host='localhost', port=6379, password='root')

client.set('color', 'black')
client.set('time', str(arrow.utcnow()))

print(client.get('color'))
print(client.get('time'))

s = client.get('time').decode('utf-8')
print(arrow.get(s))

print(client.get('fruit'))
