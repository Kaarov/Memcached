from pymemcache.client import base

client = base.Client(('localhost', 11211))

# We save several values
values = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}
client.set_many(values)

# We get several values at once
result = client.get_many(["key1", "key2", "key3"])
print(result)  # {'key1': b'value1', 'key2': b'value2', 'key3': b'value3'}
