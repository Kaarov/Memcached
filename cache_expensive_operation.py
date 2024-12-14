import time
from pymemcache.client import base

client = base.Client(('localhost', 11211))

key = "expensive_operation_result"

# Checking if the result is in the cache
cached_result = client.get(key)

if cached_result:
    print("Result from the cache:", cached_result.decode('utf-8'))
else:
    print("We are performing a long operation...")
    result = "The result of the operation"
    time.sleep(5)  # Simulation of a long calculation

    # We save the result in the cache for 10 seconds
    client.set(key, result, expire=10)
    print("Saved to the cache:", result)
