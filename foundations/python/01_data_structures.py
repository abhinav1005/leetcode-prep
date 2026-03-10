# ============================================================
# Python Data Structures - Foundations
# ============================================================

# ---- LIST ----
nums = [3, 1, 4, 1, 5]
nums.append(9)
nums.pop()              # removes last
nums.sort()
nums.sort(reverse=True)
print(nums)

# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]

# Slicing
nums = [0, 1, 2, 3, 4]
print(nums[1:3])        # [1, 2]
print(nums[::-1])       # reversed


# ---- DICT ----
from collections import defaultdict, Counter

d = {}
d['a'] = 1
print(d.get('b', 0))    # 0 (safe get)

# defaultdict
dd = defaultdict(int)
dd['x'] += 1            # no KeyError

# Counter
c = Counter([1, 1, 2, 3, 3, 3])
print(c)                # Counter({3: 3, 1: 2, 2: 1})
print(c.most_common(2)) # [(3, 3), (1, 2)]


# ---- SET ----
s = {1, 2, 3}
s.add(4)
s.discard(10)           # no error if not present
print(2 in s)           # True

a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)            # {2, 3}
print(a | b)            # {1, 2, 3, 4}
print(a - b)            # {1}


# ---- DEQUE ----
from collections import deque

q = deque()
q.append(1)
q.append(2)
q.appendleft(0)
print(q.popleft())      # 0 - use as queue (FIFO)
print(q.pop())          # 2 - use as stack (LIFO)


# ---- HEAP ----
import heapq

# Min-heap
h = [3, 1, 4, 1, 5]
heapq.heapify(h)        # in-place, O(n)
heapq.heappush(h, 2)
print(heapq.heappop(h)) # 1 (minimum)

# Max-heap (negate values)
max_h = []
for val in [3, 1, 4]:
    heapq.heappush(max_h, -val)
print(-heapq.heappop(max_h))  # 4 (maximum)

# Heap with tuples
pq = []
heapq.heappush(pq, (2, 'b'))
heapq.heappush(pq, (1, 'a'))
print(heapq.heappop(pq))  # (1, 'a')
