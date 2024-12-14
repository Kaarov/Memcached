import json
from pymemcache.client import base

client = base.Client(('localhost', 11211))

user_data = {
    "id": 123,
    "name": "John",
    "email": "john@example.com"
}

# We save the data in JSON format
key = f"user:{user_data['id']}"
client.set(key, json.dumps(user_data), expire=60)

# Getting data from the cache
cached_user = client.get(key)

if cached_user:
    user = json.loads(cached_user.decode('utf-8'))
    print("User data from the cache:", user)
else:
    print("The user was not found in the cache.")
