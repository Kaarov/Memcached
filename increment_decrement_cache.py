from pymemcache.client import base

client = base.Client(('localhost', 11211))

# Setting the initial value
client.set('counter', 0)

# Increasing the value
client.incr('counter', 5)
print("After the increment:", client.get('counter').decode('utf-8'))  # 5

# Reducing the value
client.decr('counter', 2)
print("After the decrement:", client.get('counter').decode('utf-8'))  # 3
