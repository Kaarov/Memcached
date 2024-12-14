from pymemcache.client import base

client = base.Client(('localhost', 11211))

# Saving the value in the cache
client.set('temp_key', 'Temporary Data')

# Deleting the value
client.delete('temp_key')

# Checking if it has been deleted
value = client.get('temp_key')
if not value:
    print("The key has been successfully deleted.")
else:
    print("The key still exists.")

# Delete all cache
client.flush_all()
print(client.get('temp_key'))  # Result: None
