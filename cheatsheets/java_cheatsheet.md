# Java Cheatsheet for LeetCode

## Data Structures

### Array
```java
int[] arr = new int[n];
int[] arr = {1, 2, 3};
arr.length                      // not a method, field
Arrays.sort(arr);               // O(n log n) in-place
Arrays.fill(arr, 0);            // fill with value
Arrays.copyOf(arr, n);          // copy first n elements
Arrays.copyOfRange(arr, l, r);  // arr[l..r-1]
Arrays.toString(arr);           // for printing
```

### ArrayList (Dynamic Array)
```java
import java.util.ArrayList;
List<Integer> list = new ArrayList<>();
list.add(val);                  // O(1) amortized
list.add(i, val);               // O(n)
list.get(i);                    // O(1)
list.set(i, val);               // O(1)
list.remove(i);                 // O(n) - by index
list.remove(Integer.valueOf(x));// O(n) - by value
list.size();
list.contains(val);             // O(n)
list.indexOf(val);              // O(n)
Collections.sort(list);
Collections.reverse(list);
Collections.sort(list, (a, b) -> a - b);   // ascending
Collections.sort(list, (a, b) -> b - a);   // descending
```

### HashMap
```java
import java.util.HashMap;
Map<String, Integer> map = new HashMap<>();
map.put(key, val);
map.get(key);                           // null if missing
map.getOrDefault(key, 0);              // safe get
map.containsKey(key);
map.containsValue(val);
map.remove(key);
map.size();
map.keySet();
map.values();
map.entrySet();                         // Set<Map.Entry<K,V>>
map.putIfAbsent(key, val);
map.getOrDefault(key, defaultVal);

// Iterate
for (Map.Entry<String, Integer> e : map.entrySet()) {
    String k = e.getKey();
    int v = e.getValue();
}
```

### HashSet
```java
import java.util.HashSet;
Set<Integer> set = new HashSet<>();
set.add(val);
set.remove(val);
set.contains(val);                      // O(1)
set.size();
```

### LinkedList / Deque (Queue & Stack)
```java
import java.util.ArrayDeque;
Deque<Integer> queue = new ArrayDeque<>();  // use as queue
queue.offer(val);       // add to back
queue.poll();           // remove from front (null if empty)
queue.peek();           // front element

Deque<Integer> stack = new ArrayDeque<>();  // use as stack
stack.push(val);        // add to front
stack.pop();            // remove from front
stack.peek();           // front element

// Avoid Stack<> class - use ArrayDeque instead
```

### PriorityQueue (Min-Heap)
```java
import java.util.PriorityQueue;
PriorityQueue<Integer> minHeap = new PriorityQueue<>();
PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

minHeap.offer(val);     // add O(log n)
minHeap.poll();         // remove min O(log n)
minHeap.peek();         // min O(1)
minHeap.size();

// Custom comparator (e.g. sort by second element of int[])
PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
```

### TreeMap / TreeSet (Sorted)
```java
TreeMap<Integer, Integer> map = new TreeMap<>();
map.firstKey();
map.lastKey();
map.floorKey(k);        // largest key <= k
map.ceilingKey(k);      // smallest key >= k

TreeSet<Integer> set = new TreeSet<>();
set.first();
set.last();
set.floor(k);
set.ceiling(k);
set.lower(k);           // strictly less than k
set.higher(k);          // strictly greater than k
```

---

## String

```java
String s = "hello";
s.length();
s.charAt(i);
s.substring(i, j);              // s[i..j-1]
s.indexOf('c');
s.contains("sub");
s.startsWith("pre");
s.endsWith("suf");
s.toLowerCase() / s.toUpperCase();
s.trim();                       // strip whitespace
s.replace('a', 'b');
s.split(" ");                   // returns String[]
String.join(", ", list);        // join with delimiter
s.toCharArray();                // String -> char[]
String.valueOf(charArray);      // char[] -> String
s.equals(other);                // NEVER use == for strings
s.compareTo(other);             // lexicographic compare

// Build strings efficiently
StringBuilder sb = new StringBuilder();
sb.append("hello");
sb.append(42);
sb.reverse();
sb.toString();
sb.length();
sb.charAt(i);
sb.deleteCharAt(i);

// char utilities
Character.isLetterOrDigit(c);
Character.isDigit(c);
Character.isLetter(c);
Character.toLowerCase(c);
(int) c                         // char to ASCII
(char) (int)                    // int to char
```

---

## Sorting

```java
// Arrays
Arrays.sort(arr);
Arrays.sort(arr, (a, b) -> a[0] - b[0]);   // 2D array by first col

// List
Collections.sort(list);
list.sort((a, b) -> a - b);

// Reverse sort
Arrays.sort(arr, Collections.reverseOrder()); // only for Integer[], not int[]
```

---

## Math / Misc

```java
Math.max(a, b);
Math.min(a, b);
Math.abs(x);
Math.pow(x, n);             // returns double
Math.sqrt(x);               // returns double
Math.floor(x);
Math.ceil(x);
(int) Math.pow(x, n);       // cast to int

Integer.MAX_VALUE           // 2^31 - 1
Integer.MIN_VALUE           // -2^31
Integer.parseInt("42");     // String -> int
String.valueOf(42);         // int -> String
Integer.toBinaryString(n);  // int -> binary string

// Bit operations
n & 1                       // last bit (odd/even)
n >> 1                      // divide by 2
n << 1                      // multiply by 2
n & (n - 1)                 // clear last set bit
Integer.bitCount(n);        // count set bits
```

---

## Common Patterns

### Binary Search
```java
int l = 0, r = nums.length - 1;
while (l <= r) {
    int mid = l + (r - l) / 2;  // avoid overflow
    if (nums[mid] == target) return mid;
    else if (nums[mid] < target) l = mid + 1;
    else r = mid - 1;
}
```

### BFS
```java
Queue<Integer> q = new ArrayDeque<>();
Set<Integer> visited = new HashSet<>();
q.offer(start);
visited.add(start);
while (!q.isEmpty()) {
    int node = q.poll();
    for (int neighbor : graph.get(node)) {
        if (!visited.contains(neighbor)) {
            visited.add(neighbor);
            q.offer(neighbor);
        }
    }
}
```

### DFS (Recursive)
```java
void dfs(int node, Set<Integer> visited, Map<Integer, List<Integer>> graph) {
    visited.add(node);
    for (int neighbor : graph.get(node)) {
        if (!visited.contains(neighbor)) {
            dfs(neighbor, visited, graph);
        }
    }
}
```

### Memoization (DP)
```java
Map<Integer, Integer> memo = new HashMap<>();
int dp(int i) {
    if (memo.containsKey(i)) return memo.get(i);
    int result = dp(i - 1) + dp(i - 2); // example
    memo.put(i, result);
    return result;
}
```
