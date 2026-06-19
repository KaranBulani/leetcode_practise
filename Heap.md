# Heap (Priority Queue)

A heap (often used as a priority queue) is a special tree-based data structure that allows you to efficiently:

* Insert an element
* Remove the highest-priority element
* Peek at the highest-priority element

---

## What is a Heap?

A heap is a **complete binary tree** that satisfies the **heap property**.

A complete binary tree means:

* Every level is completely filled except possibly the last level.
* The last level is filled from left to right.

---

## Min Heap

Every parent is **less than or equal to** its children.

Example:

```text
        1
      /   \
     3     5
    / \   / \
   7  8  6  9
```

The smallest element is always at the root.

---

## Max Heap

Every parent is **greater than or equal to** its children.

```text
        9
      /   \
     7     8
    / \   / \
   3   2 5   1
```

The largest element is always at the root.

---

## Why Not Use a Sorted List?

Suppose we need:

```python
insert(5)
insert(2)
insert(8)
remove_min()
```

### Sorted List

Insertion requires shifting elements.

**Time Complexity:** `O(n)`

### Heap

* Insert → `O(log n)`
* Remove Min → `O(log n)`
* Peek Min → `O(1)`

Heaps provide much better performance when frequent insertions and removals are required.

---

## How is a Heap Stored?

A heap is usually stored in an array.

Example:

```text
        1
      /   \
     3     5
    / \   /
   7   8 6
```

Array representation:

```python
[1, 3, 5, 7, 8, 6]
```

Notice that no pointers are required.

The parent-child relationships can be calculated using indices.

---

## Index Relationships (0-Based Indexing)

For a node at index `i`:

```text
Parent      = (i - 1) // 2
Left Child  = 2*i + 1
Right Child = 2*i + 2
```

Example:

```python
heap = [1, 3, 5, 7, 8, 6]
```

Node at index `1` has value `3`.

```text
Left Child Index  = 2*1 + 1 = 3
Right Child Index = 2*1 + 2 = 4
```

Values:

```text
heap[3] = 7
heap[4] = 8
```

---

## Index Relationships (1-Based Indexing)

For a node at index `i`:

```text
Parent      = i // 2
Left Child  = 2*i
Right Child = 2*i + 1
```

---

## Insert Operation

Suppose we have:

```python
[1, 3, 5, 7, 8, 6]
```

Insert:

```python
2
```

### Step 1: Add to End

```python
[1, 3, 5, 7, 8, 6, 2]
```

Tree:

```text
        1
      /   \
     3     5
    / \   / \
   7  8  6   2
```

Heap property is violated because:

```text
2 < 5
```

---

### Step 2: Bubble Up

Swap with parent:

```python
[1, 3, 2, 7, 8, 6, 5]
```

Now compare:

```text
2 > 1
```

Heap property is satisfied.

Final Heap:

```python
[1, 3, 2, 7, 8, 6, 5]
```

### Time Complexity

```text
O(log n)
```

Reason:

A complete binary tree with `n` nodes has height `log n`, and the inserted element can move at most that many levels.

---

## Remove Min Operation

Suppose:

```python
[1, 3, 2, 7, 8, 6, 5]
```

Remove the root.

---

### Step 1: Move Last Element to Root

```python
[5, 3, 2, 7, 8, 6]
```

---

### Step 2: Bubble Down

Current Tree:

```text
    5
   / \
  3   2
```

Smallest child is `2`.

Swap:

```python
[2, 3, 5, 7, 8, 6]
```

Tree becomes:

```text
      2
    /   \
   3     5
        /
       6
```

Heap property is now satisfied.

Final Heap:

```python
[2, 3, 5, 7, 8, 6]
```

### Time Complexity

```text
O(log n)
```

---

## Implementing a Min Heap From Scratch

```python
class MinHeap:
    def __init__(self):
        self.heap = []
        self.heapify()
        
    def heapify(self):
        n = len(self.heap)
        # we want to skip leaf nodes from heapify
        # so we start from last node's parent which would be the 1st node which is not leaf
        # last node's index is n-1 where n = len(nums), parent would be (i - 1) // 2
        # (n-1 - 1) // 2    ->      n//2 - 1
        # this "n//2 - 1" assumes n = len(nums) not len(nums) - 1

        for i in range((n // 2) - 1, -1, -1):
            self._bubble_down(i)
        
    def push(self, val):
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        minimum = self.heap[0]

        self.heap[0] = self.heap.pop()
        self._bubble_down(0)

        return minimum

    def peek(self):
        return self.heap[0] if self.heap else None

    def _bubble_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2

            if self.heap[idx] < self.heap[parent]:
                self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
                idx = parent
            else:
                break

    def _bubble_down(self, idx):
        n = len(self.heap)

        while True:
            smallest = idx

            left = 2 * idx + 1
            right = 2 * idx + 2

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == idx:
                break

            self.heap[idx], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[idx]
            )

            idx = smallest
```

---

## Usage Example

```python
h = MinHeap()

h.push(5)
h.push(2)
h.push(8)
h.push(1)

print(h.pop())   # 1
print(h.pop())   # 2
print(h.pop())   # 5
```

---

## Complexity Summary

| Operation              | Time Complexity |
| ---------------------- | --------------- |
| Peek                   | O(1)            |
| Insert                 | O(log n)        |
| Remove Min             | O(log n)        |
| Build Heap             | O(n)            |
| Search Arbitrary Value | O(n)            |

---

## Why is Build Heap O(n)?

A common misconception is that building a heap by heapifying an array should be `O(n log n)` 

## Method 1
- which it would be if we build the heap by repeatedly inserting elements
```python
heappush(5)
heappush(2)
heappush(8)
heappush(1)
heappush(7)
```
Each insertion may bubble up through the height of the heap: `O(log n)`. Doing this for all n elements gives: `n × O(log n) = O(n log n)`

## **Method 2** - Bottom-Up Heapify

Instead of inserting one by one, start with the entire array: `[5, 2, 8, 1, 7]`. 

Treat it as a binary tree:
```text
        5
      /   \
     2     8
    / \
   1   7
```
Now heapify from the bottom upward.

1. Start from the last non-leaf node.
2. Perform bubble-down (heapify).
3. Move upward toward the root.

---
### Detailed Explanation

Instead of inserting one by one, start with the entire array:

```python
[5, 2, 8, 1, 7]
```

Treat it as a binary tree:

```text
        5
      /   \
     2     8
    / \
   1   7
```

Now heapify from the bottom upward.

---
#### Key Observation

* Most nodes are already near the bottom of the tree. 
* Nodes near the bottom can move only a tiny distance. 
* Only a few nodes near the top can move many levels. 
* So not every node costs `O(log n)`.

---

#### Example

Consider a complete tree with 15 nodes:

```text
               *
          /         \
        *             *
      /   \         /   \
     *     *       *     *
    / \   / \     / \   / \
   *  *  *  *    *  *  *  *
```

Height of tree:
`log₂(15) ≈ 4`


Let's count work by level.

---

##### Leaf Nodes

There are 8 leaves.

```text
*
*
*
*
*
*
*
*
```

They require: `0 swaps`

Cost: ` 8 × 0 = 0`

---

##### One Level Above Leaves

There are 4 nodes.

Each can move at most:` 1 level `

Cost: `4 × 1 = 4`

---

##### Next Level

There are 2 nodes.

Each can move at most: `2 levels`

Cost:`2 × 2 = 4`

---

##### Root

There is 1 node.

It can move: `3 levels`

Cost: `1 × 3 = 3`

---

Total work: `0 + 4 + 4 + 3 = 11`

For 15 nodes.

Notice: `11 < 15 log₂(15)`

by a large margin.

---

## Important Interview Notes

#### Heap ≠ Sorted Tree

Only parent-child relationships are guaranteed.

This is a valid min heap:

```text
        1
      /   \
     3     2
    / \   / \
   8  9  7   5
```

Notice: `8 > 2` which is perfectly fine.

---

#### Heap is Great For

* Priority Queues
* Top K Problems
* Dijkstra's Algorithm
* A* Search
* Heap Sort
* Streaming Median Problems
* Scheduling Systems

---

#### Heap is Bad For

Searching arbitrary values: `find(17)` may require scanning every element.

Time Complexity: `O(n)` A heap is optimized only for quickly accessing the minimum (or maximum) element.

---

## Key Takeaway

A heap is a complete binary tree stored efficiently in an array that provides:

* Peek → `O(1)`
* Insert → `O(log n)`
* Remove Min / Max → `O(log n)`

It is the most commonly used implementation of a priority queue and appears frequently in coding interviews and real-world systems.

---

# Python heapq Module

---
Python provides a built-in heap implementation through the `heapq` module.

Important:

* `heapq` implements a **Min Heap**
  * or **Max Heap** but taking `values * -1` or If you are running **Python 3.14 or newer**, the `heapq` module includes official, public max-heap counterparts suffixed with `_max` .
* The smallest element is always at index `0`.
* Internally it uses a list.

```python
import heapq
```

---

### Creating a Heap

```python
import heapq

heap = []

heapq.heappush(heap, 5) # For Max Heap - heapq.heappush_max(data, 10)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
heapq.heappush(heap, 1)

print(heap)
```

Possible output:

```python
[1, 2, 8, 5]
```

The list representation may not be sorted, but it satisfies the heap property.

---

### Peek Minimum Element

```python
print(heap[0])
```

Output: `1`

Time Complexity: `O(1)`

---

### Remove Minimum Element

```python
minimum = heapq.heappop(heap) # heapq.heappop_max(data) 

print(minimum)
print(heap)
```

Output:

```python
1
[2, 5, 8]
```

Time Complexity: `O(log n)`

---

### Convert Existing List Into Heap

Suppose: `nums = [5, 2, 8, 1, 7]`

Convert into a heap:
```python
heapq.heapify(nums) # heapq.heapify_max(data)
print(nums)
```

Possible output: `[1, 2, 8, 5, 7]`

Time Complexity:`O(n)`

---

### Push and Pop in One Operation

```python
heap = [2, 5, 8]

result = heapq.heappushpop(heap, 1) # heapq.heappushpop_max(max_heap, 8)

print(result)
print(heap)
```

Output:

```python
1
[2, 5, 8]
```

This operation is more efficient than performing:

```python
heappush()
heappop()
```

separately.

---

### Replace Root in One Operation

```python
heap = [2, 5, 8]

result = heapq.heapreplace(heap, 10) # heapq.heapreplace_max(max_heap, 12)

print(result)
print(heap)
```

Output:

```python
2
[5, 10, 8]
```

This removes the smallest element first and then inserts the new value.

---

### Max Heap Using heapq

`heapq` only supports Min Heap directly.

To simulate a Max Heap, store negative values.

```python
import heapq

heap = []

heapq.heappush(heap, -5)
heapq.heappush(heap, -2)
heapq.heappush(heap, -8)
heapq.heappush(heap, -1)

largest = -heapq.heappop(heap)

print(largest)
```

Output: `8`

---

### Example

```python
import heapq

heap = []

heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
heapq.heappush(heap, 1)

print(heap[0])          # 1

print(heapq.heappop(heap))  # 1
print(heapq.heappop(heap))  # 2
print(heapq.heappop(heap))  # 5
print(heapq.heappop(heap))  # 8
```

---

### heapq Complexity Summary

| Operation      | Time     |
| -------------- | -------- |
| heap[0] (Peek) | O(1)     |
| heappush()     | O(log n) |
| heappop()      | O(log n) |
| heapify()      | O(n)     |
| heappushpop()  | O(log n) |
| heapreplace()  | O(log n) |
