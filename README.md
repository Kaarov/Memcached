# 1. Running Memcached via Docker

```shell
docker run -d --name memcached -p 11211:11211 memcached
```

### Description of parameters:

* `-d:` Starts the container in the background.
* `--name memcached:` Container name.
* `-p 11211:11211:` Throws port 11211 (Memcached by default).
* `memcached:` The official image of Memcached from Docker Hub is used.

After execution, Memcached will be available on `localhost:11211`.

---

# 2. Installing a Python library
```shell
pip install pymemcache
```

---

# 3. An example of working with Memcached from Python

```python
from pymemcache.client import base

# Connection to Memcached (local host and port)
client = base.Client(('localhost', 11211))

# Saving data in Memcached
client.set('key', 'value')

# Obtaining data from Memcached
value = client.get('key')
print(value.decode('utf-8'))  # Result: value
```

---

# 4. Launch with custom settings via Docker

```shell
docker run -d --name memcached -p 11211:11211 memcached memcached -m 128 -vv
```

### Description of parameters:

* `-m 128`: Tells Memcached to use 128 MB of RAM.
* `-vv`: Includes detailed log output.

---

# 5. Checking the operation of Memcached inside the container

```shell
docker exec -it -u root memcached bash
apt-get update
apt-get install telnet
telnet localhost 11211
```

### An example of verification via `telnet`:

```shell
set mykey 0 900 5
hello
STORED
get mykey
VALUE mykey 0 5
hello
END
```

---

# 6. Example of working with Python and caching

```python
import time
from pymemcache.client import base

client = base.Client(('localhost', 11211))

# Key and Value
key = "expensive_calculation"
cached_result = client.get(key)

if cached_result:
    print("From cache:", cached_result.decode('utf-8'))
else:
    print("Running...")
    result = "42"  # The result of a long operation
    time.sleep(2)  # Duration simulation
    client.set(key, result, expire=10)  # Caching for 10 seconds
    print("Saved to the cache:", result)
```

---

# 7. Removing the Memcached container

```shell
docker stop memcached
docker rm memcached
```
