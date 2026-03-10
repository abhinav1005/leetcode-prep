import java.util.*;

/**
 * Java Data Structures - Foundations
 * Run individual methods in main() to experiment.
 */
public class DataStructures {

    public static void main(String[] args) {
        listExamples();
        mapExamples();
        setExamples();
        dequeExamples();
        heapExamples();
    }

    // ---- LIST (ArrayList) ----
    static void listExamples() {
        List<Integer> list = new ArrayList<>(Arrays.asList(3, 1, 4, 1, 5));

        list.add(9);                    // append
        list.add(0, 0);                 // insert at index
        list.get(0);                    // access
        list.set(0, 99);                // update
        list.remove(0);                 // remove by index
        list.remove(Integer.valueOf(9));// remove by value
        list.contains(5);               // true
        list.size();

        Collections.sort(list);
        Collections.sort(list, (a, b) -> b - a); // descending
        list.sort((a, b) -> a - b);              // ascending

        System.out.println(list);
    }

    // ---- MAP (HashMap) ----
    static void mapExamples() {
        Map<String, Integer> map = new HashMap<>();
        map.put("a", 1);
        map.put("b", 2);
        map.getOrDefault("c", 0);      // safe get
        map.containsKey("a");
        map.remove("b");

        // increment count pattern
        Map<Character, Integer> freq = new HashMap<>();
        for (char c : "hello".toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }

        // iterate
        for (Map.Entry<String, Integer> e : map.entrySet()) {
            System.out.println(e.getKey() + " -> " + e.getValue());
        }

        // sorted map
        Map<Integer, Integer> sorted = new TreeMap<>();
    }

    // ---- SET ----
    static void setExamples() {
        Set<Integer> set = new HashSet<>(Arrays.asList(1, 2, 3));
        set.add(4);
        set.remove(1);
        set.contains(2);

        // sorted set
        TreeSet<Integer> tset = new TreeSet<>(Arrays.asList(5, 3, 1, 4));
        tset.first();       // 1
        tset.last();        // 5
        tset.floor(3);      // 3 (largest <= 3)
        tset.ceiling(4);    // 4 (smallest >= 4)
    }

    // ---- DEQUE (Queue + Stack) ----
    static void dequeExamples() {
        // Queue (FIFO)
        Deque<Integer> queue = new ArrayDeque<>();
        queue.offer(1);
        queue.offer(2);
        queue.peek();       // front, no remove
        queue.poll();       // remove front

        // Stack (LIFO)
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(1);
        stack.push(2);
        stack.peek();       // top, no remove
        stack.pop();        // remove top
    }

    // ---- PRIORITY QUEUE (Heap) ----
    static void heapExamples() {
        // Min-heap
        PriorityQueue<Integer> minH = new PriorityQueue<>();
        minH.offer(3);
        minH.offer(1);
        minH.offer(4);
        System.out.println(minH.poll()); // 1

        // Max-heap
        PriorityQueue<Integer> maxH = new PriorityQueue<>(Collections.reverseOrder());
        maxH.offer(3);
        maxH.offer(1);
        maxH.offer(4);
        System.out.println(maxH.poll()); // 4

        // Heap with custom comparator (sort int[] by second element)
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        pq.offer(new int[]{1, 3});
        pq.offer(new int[]{2, 1});
        System.out.println(Arrays.toString(pq.poll())); // [2, 1]
    }
}
