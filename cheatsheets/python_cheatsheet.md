# Python Cheatsheet for LeetCode

## Built-in Data Structures

### List (Dynamic Array)
```python
nums = [1, 2, 3]
nums.append(4)          # O(1)
nums.pop()              # O(1) - remove last
nums.pop(i)             # O(n) - remove at index
nums.insert(i, val)     # O(n)
nums.remove(val)        # O(n) - removes first occurrence
nums.reverse()          # O(n) in-place
nums[::-1]              # O(n) reversed copy
nums.sort()             # O(n log n) in-place
sorted(nums)            # O(n log n) returns new list
nums.index(val)         # O(n)
val in nums             # O(n)
len(nums)               # O(1)
```

### Dictionary (Hash Map)
```python
d = {}
d = {'a': 1}
d['key'] = val          # set
d.get('key', default)   # safe get
d.pop('key', None)      # safe remove
'key' in d              # O(1)
d.keys()
d.values()
d.items()               # (key, val) pairs

# defaultdict - no KeyError on missing keys
from collections import defaultdict
d = defaultdict(int)        # default 0
d = defaultdict(list)       # default []
d = defaultdict(set)        # default set()

# Counter
from collections import Counter
c = Counter([1,1,2,3])      # {1:2, 2:1, 3:1}
c.most_common(k)            # top k by count
```

### Set (Hash Set)
```python
s = set()
s = {1, 2, 3}
s.add(val)              # O(1)
s.remove(val)           # O(1) - KeyError if missing
s.discard(val)          # O(1) - safe remove
val in s                # O(1)
s1 & s2                 # intersection
s1 | s2                 # union
s1 - s2                 # difference
```

### Deque (Double-ended Queue)
```python
from collections import deque
q = deque()
q.append(val)           # add right O(1)
q.appendleft(val)       # add left O(1)
q.pop()                 # remove right O(1)
q.popleft()             # remove left O(1)
q[0]                    # peek left
q[-1]                   # peek right
```

### Heap (Min-Heap)
```python
import heapq
h = []
heapq.heappush(h, val)      # O(log n)
heapq.heappop(h)            # O(log n) - returns min
h[0]                        # peek min O(1)
heapq.heapify(list)         # O(n) in-place

# Max-heap: negate values
heapq.heappush(h, -val)
-heapq.heappop(h)

# Heap with tuples - sorts by first element
heapq.heappush(h, (priority, val))
```

### String
```python
s = "hello"
s[i]                    # O(1) access
s[i:j]                  # O(k) slice
s[::-1]                 # reverse
s.lower() / s.upper()
s.strip()               # remove whitespace
s.split(' ')            # split by delimiter
' '.join(list)          # join list into string
s.startswith('pre')
s.endswith('suf')
s.replace('a', 'b')
s.count('x')
ord('a')                # char to ASCII int
chr(97)                 # int to char
s.isalpha() / s.isdigit() / s.isalnum()

# Build string efficiently
''.join(['a', 'b', 'c'])    # don't use += in loop
```

---

## Sorting

```python
# Sort by key
nums.sort(key=lambda x: x[1])          # by second element
nums.sort(key=lambda x: -x)            # descending
nums.sort(key=lambda x: (x[0], x[1]))  # multi-key

# sorted() returns new list
sorted(d.items(), key=lambda x: x[1])
```

---

## Common Patterns

### Two Pointers
```python
l, r = 0, len(nums) - 1
while l < r:
    # do something
    l += 1
    r -= 1
```

### Sliding Window
```python
l = 0
for r in range(len(nums)):
    # expand window with nums[r]
    while <window invalid>:
        # shrink from left
        l += 1
    # update answer
```

### Binary Search
```python
l, r = 0, len(nums) - 1
while l <= r:
    mid = (l + r) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        l = mid + 1
    else:
        r = mid - 1
```

### BFS
```python
from collections import deque
q = deque([start])
visited = {start}
while q:
    node = q.popleft()
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            q.append(neighbor)
```

### DFS (Iterative)
```python
stack = [start]
visited = {start}
while stack:
    node = stack.pop()
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            stack.append(neighbor)
```

### DFS (Recursive)
```python
def dfs(node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)
```

---

## Math / Misc

```python
float('inf')            # infinity
float('-inf')           # negative infinity
abs(x)
x ** 2                  # power
x ** 0.5                # square root
x % 2 == 0              # even check
x // 2                  # floor division
divmod(a, b)            # returns (quotient, remainder)

# Bit operations
x & 1                   # check last bit (odd/even)
x >> 1                  # divide by 2
x << 1                  # multiply by 2
x & (x - 1)             # clear last set bit
x ^ x == 0              # XOR with itself = 0
```

---

## itertools / functools

```python
from itertools import combinations, permutations, product
combinations([1,2,3], 2)    # (1,2), (1,3), (2,3)
permutations([1,2,3], 2)    # all ordered pairs
product([1,2], repeat=2)    # cartesian product

from functools import lru_cache
@lru_cache(maxsize=None)
def dp(i):
    ...
```
