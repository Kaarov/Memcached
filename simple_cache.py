from pymemcache.client import base

# Connecting to the Memcached server
client = base.Client(('localhost', 11211))

# Saving the value to the cache
client.set('greeting', 'Hello, Memcached!')

# Extracting a value from the cache
value = client.get('greeting')
print(value.decode('utf-8'))  # Result: Hello, Memcached!
