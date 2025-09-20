# ArrHash Notes:

---

1. **Euclid's Algorithm for GCD** [LC 1071](https://github.com/KaranBulani/leetcode_practise/blob/python/ArrHash%201071%20Greatest%20Common%20Divisor%20of%20Strings/Solution.py#L7)
   * The **GCD** of two integers is the largest number that divides both of them without leaving a remainder.
   * Suppose you want the GCD of two numbers `a` and `b` (with `a > b`):
     1. Divide `a` by `b`, and get the remainder `r`.
        That is:
        $$
        a = b \cdot q + r \quad \text{where } 0 \leq r < b
        $$
     2. Replace `a` with `b`, and `b` with `r`.
     3. Repeat until `r = 0`.
     4. When `r = 0`, the GCD is the last nonzero divisor (the current `b`). 
   * Find GCD(48, 18):
      * Step 1: $48 ÷ 18 = 2$ remainder **12**
      * Step 2: Now find GCD(18, 12)
      * Step 3: $18 ÷ 12 = 1$ remainder **6**
      * Step 4: Now find GCD(12, 6)
      * Step 5: $12 ÷ 6 = 2$ remainder **0**
        
      ✅ Last nonzero divisor is 6 → **GCD(48, 18) = 6**

---

# Binary Search Notes:

---

### 🔑 Notes for **162. Find Peak Element**

1. **Binary search intuition**

   * On an **uphill** (`nums[mid] < nums[mid+1]`) → a peak must exist on the **right side** (or the boundary).
   * On a **downhill** (`nums[mid] > nums[mid+1]`) → a peak must exist at `mid` or on the **left side**.
   * Each step halves the search space → **O(log n)** time, **O(1)** space.

2. **Loop condition**

   * Use `while low < high` (not `low <= high`)
   * Because we always compare `nums[mid]` and `nums[mid+1]` → both indices must be **in-bounds**.

3. **Comparison strategy**

   * Now as loop won't run when both low high are equal. 
   * We should increment decrement low high such that no value gets skipped.
   * So it would be `low = mid + 1` and `high = mid`, rather than `low = mid + 1` and `high = mid - 1`.
---
# Linked List Notes:

---
1. **\_\_repr\_\_**
   * The \_\_repr\_\_ method defines how an object is represented when you print it or look at it in the Python REPL (interactive shell, debugger, etc.).
      ```python
      # Definition for singly-linked list
      class ListNode:
          def __init__(self, val=0, next=None):
              self.val = val
              self.next = next
          def __repr__(self):
              return f"{self.val}->{self.next}" if self.next else f"{self.val}"
      ```
   * Without `__repr__`
   * If you didn’t define `__repr__`, printing a `ListNode` object would show something like below which isn’t human-readable.
      ```python
      <__main__.ListNode object at 0x7f123abc4560>
      ```
   * With your `__repr__`
   * If the node has a `.next`, it prints:
     ```
     val->next
     ```
     where `next` is also a `ListNode`, so it recursively calls `__repr__` again.

   * If it’s the last node (`next=None`), it just prints:

     ```
     val
     ```

2. **dummy node purpose**
   * Read [comment](https://github.com/KaranBulani/leetcode_practise/blob/python/LinkedList%2019%20Remove%20Nth%20Node%20From%20End%20of%20List/Solution.py#L18) to understand purpose of dummy node & also [here](https://github.com/KaranBulani/leetcode_practise/blob/python/LinkedList%202%20Add%20Two%20Numbers/Solution.py).


3. **Cut list when [needed](https://github.com/KaranBulani/leetcode_practise/blob/python/LinkedList%20143%20Reorder%20List/Solution.py#L55)** and also [here](https://github.com/KaranBulani/leetcode_practise/blob/python/LinkedList%202130%20Maximum%20Twin%20Sum%20of%20a%20Linked%20List/Solution.py#L23).

4. Slow and fast pointer like [here](https://github.com/KaranBulani/leetcode_practise/blob/python/LinkedList%20141%20Linked%20List%20Cycle/Solution.py), [here](https://github.com/KaranBulani/leetcode_practise/blob/python/LinkedList%20142%20Linked%20List%20Cycle%20II/Solution.py) and in [MergeSort](https://github.com/KaranBulani/leetcode_practise/blob/python/LinkedList%20148%20Sort%20List/Solution.py). 2pointer technique like [here](https://github.com/KaranBulani/leetcode_practise/blob/python/LinkedList%2082%20Remove%20Duplicates%20from%20Sorted%20List%20II/Solution.py)

5. **Doubly LinkedList usage of head and tail [LC 707](https://github.com/KaranBulani/leetcode_practise/blob/python/LinkedList%20707%20Design%20Linked%20List/Solution.py)** without head tail **[LC 1472](https://github.com/KaranBulani/leetcode_practise/blob/python/LinkedList%201472%20Design%20Browser%20History/Solution.py).** 

6. How [287. Find the Duplicate Number](https://github.com/KaranBulani/leetcode_practise/blob/python/LinkedList%20287%20Find%20the%20Duplicate%20Number/Solution.py) can be considered a LL problem. 

7. Usage of dictionary in [LC 138](https://github.com/KaranBulani/leetcode_practise/blob/python/LinkedList%20138%20Copy%20List%20with%20Random%20Pointer/Solution.py), Doubly LinkedList ( [LC 146](https://github.com/KaranBulani/leetcode_practise/blob/python/LinkedList%20146%20LRU%20Cache/Solution.py), [LC 432](https://github.com/KaranBulani/leetcode_practise/blob/python/LinkedList%20432.%20All%20O%60one%20Data%20Structure/Solution.py) ) & dict + prefix sum in [LC 1171](https://github.com/KaranBulani/leetcode_practise/blob/python/LinkedList%201171%20Remove%20Zero%20Sum%20Consecutive%20Nodes%20from%20Linked%20List/Solution.py).

8. Unique way to solve [LC 160](https://github.com/KaranBulani/leetcode_practise/blob/python/LinkedList%20160%20Intersection%20of%20Two%20Linked%20Lists/Solution.py).


---

# Tree Notes:

---

1. **Basic Tree Operations**

   * Insert in a BST [LC 701](https://github.com/KaranBulani/leetcode_practise/blob/python/Tree%20701%20Insert%20into%20a%20Binary%20Search%20Tree/Solution.py), Delete in a BST [LC 450](https://github.com/KaranBulani/leetcode_practise/blob/python/Tree%20450%20Delete%20Node%20in%20a%20BST/Solution.py).


---