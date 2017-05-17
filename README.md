

### Simple Implementation of LRU cache in python

Requirements: python 3

### Usage (example):

```python
from LRU import LRU
import random

random_cache_size = random.randrange(10)
print("Initiaizing cache of size", random_cache_size)
cache_obj = LRU(random_cache_size)

# returns None as cache is empty
print("1 ->", cache_obj.get(1))

# returns "not found" as it is the default argument
print("1 ->", cache_obj.get(1,"not found"))

cache_obj.put(1,2)

# prints 2
print("1 ->", cache_obj.get(1))
```


### Testing:
To run tests, run `python test.py`

If something is not clear please contact me.