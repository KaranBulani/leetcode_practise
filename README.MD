# ArrHash Notes:

---

1. **Euclid's Algorithm for GCD** [LC 1071](https://github.com/KaranBulani/leetcode_practise/blob/python/ArrHash%201071%20Greatest%20Common%20Divisor%20of%20Strings/Solution.py#L7)
   * The **GCD** of two integers is the largest number that divides both of them without leaving a remainder.
   * Suppose you want the GCD of two numbers `a` and `b` (with `a > b`):
     1. Divide `a` by `b`, and get the remainder `r`.
        That is: 
        `a = b * q + r  where  0 <= r < b`
        
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
2. **Lowest Common Multiple**:
   * `LCM(a,b) * GCD(a,b) = a * b`
   * Example:`a = 12, b = 18`
   * `GCD(12, 18) = 6, LCM(12, 18) = 36`
   * `GCD(12, 18) * LCM(12, 18) = a*b`
   * `6 * 36 = 12 * 18`
   * `216 = 216`
3. **Kadane's Algorithm**: find the maximum sum of a contiguous subarray in an array of integers (which can contain both positive and negative numbers).
   * [LC 53](https://github.com/KaranBulani/leetcode_practise/blob/python/DivideAndConquer%2053%20Maximum%20Subarray/Solution.py) Normal Kadane's.
   * [LC 918](https://github.com/KaranBulani/leetcode_practise/blob/python/ArrHash%20918%20Maximum%20Sum%20Circular%20Subarray/Solution.py) Circular Kadane's Algorithm.

3. **Sieve of Eratosthenes**: — The algorithm works by **eliminating multiples** of each prime number starting from 2. [LC 204](https://github.com/KaranBulani/leetcode_practise/blob/python/ArrHash%20204%20Count%20Primes/Solution.py):
   * Create a list of boolean values `is_prime[0..n]` initialized to `True`.
   * Set `is_prime[0]` and `is_prime[1]` to `False`, because 0 and 1 are not prime.
   * For each number `i` from 2 to √n:
      * If `is_prime[i]` is `True`, mark **all multiples of `i`** (i.e., `i*i`, `i*i+i`, `i*i+2i`, ...) as `False`.
   * After the loop, all indexes `i` such that `is_prime[i]` is `True` are prime numbers.

4. **PrefixSums**: Draw the solution to understand if prefix sums would work or not
   * Like [304. Range Sum Query 2D - Immutable](https://github.com/KaranBulani/leetcode_practise/blob/python/ArrHash%20304%20Range%20Sum%20Query%202D%20-%20Immutable/Solution.py)
   * We can keep {0:1} as base case [LC 560](https://github.com/KaranBulani/leetcode_practise/blob/python/ArrHash%20560%20Subarray%20Sum%20Equals%20K/Solution.py), [LC 437](https://github.com/KaranBulani/leetcode_practise/blob/python/Tree%20437%20Path%20Sum%20III/Solution.py).
   * Might need to do some algebra instead of drawing with some base case [LC 523](https://github.com/KaranBulani/leetcode_practise/blob/python/ArrHash%20523%20Continuous%20Subarray%20Sum/Solution.py), [LC 974](https://github.com/KaranBulani/leetcode_practise/blob/python/ArrHash%20974%20Subarray%20Sums%20Divisible%20by%20K/Solution.py) or Algebra post some input manipulation [LC 1248](https://github.com/KaranBulani/leetcode_practise/blob/python/ArrHash%201248%20Count%20Number%20of%20Nice%20Subarrays/Solution.py).
   * For positive numbers, the prefix sum is always increasing, allowing binary search. [LC 2389](https://github.com/KaranBulani/leetcode_practise/blob/python/ArrHash%202389%20Longest%20Subsequence%20With%20Limited%20Sum/Solution.py)
   * Base case as {0:-1} and some input manipulation [LC 525](https://github.com/KaranBulani/leetcode_practise/blob/python/ArrHash%20525%20Contiguous%20Array/Solution.py)
   * Scanning window (`Not Expanding/Shrinking like Sliding Window`) on PrefixSum. Headache Sum [LC 1031](https://github.com/KaranBulani/leetcode_practise/blob/python/ArrHash%201031%20Maximum%20Sum%20of%20Two%20Non-Overlapping%20Subarrays/Solution.py) Can say rule of sliding window works here:
     * If a window `[a, b)` is valid, then shrinking it while maintaining non-overlap or size limits keeps it valid (until a constraint breaks).
     * Once a window violates a constraint (e.g., overlap or size), extending doesn’t make previous configurations valid again.
---

# Binary Search Notes:

---
1. Binary Search can be used to search value in a sorted array. 
2. Or to test a range of solutions where all values less than equal a number works but greater than number doesn't work or vice-versa. 

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
# 2 pointer/Sliding window:

---
Key Criteria for Two Pointers/Sliding Window:
1. Rule 1 (Validity of Wider Scope):  
   If a larger window (wider scope) is valid, all smaller sub-windows within it must also be valid.  
   - Example (Longest Substring Without Repeats):  
     If the substring `s[i...j]` is valid (no duplicates), then `s[i...k]` (where `k < j`) is also valid. This allows efficient shrinking of the window from the left (`i++`) when duplicates are found.
2. Rule 2 (Invalidity of Narrower Scope):  
   If a smaller window (narrower scope) is invalid, all larger windows containing it must also be invalid.  
   - Example:  
     If `s[i...j]` has duplicates, then `s[i...j+1]` (expanded window) will still have duplicates. This ensures we can discard invalid windows early.

Sums:
1. For [992](https://github.com/KaranBulani/leetcode_practise/blob/python/SlidingWindow%20992%20Subarrays%20with%20K%20Different%20Integers/Solution.py). `Subarrays with K Different Integers`
   * It doesn't follow any typical rules:
   * Rule 1 fails. For`nums = [1,2,1,2,3], k = 3` This`1,2,1,2,3` is valid but `1,2,1,2` is invalid.
   * Rule 2 fails. For`nums = [1,2,1,2,3], k = 3` This`1,2,1,2` is invalid but `1,2,1,2,3` is valid.
   * Reframe sum as: `exactly K distinct = at most K distinct − at most(K-1) distinct` and both follow 2 rules.
   * [LC 1248](https://github.com/KaranBulani/leetcode_practise/blob/python/ArrHash%201248%20Count%20Number%20of%20Nice%20Subarrays/Solution.py). `Count Number of Nice Subarrays` can also be same sum.
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
1. **Tree Node Structure**.
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        # Default: <__main__.TreeNode object at 0x0000020A0DB0AC50>

        # If you want to see the whole tree recursively (careful with big trees), you can do this:
        # TreeNode(val=10, left=TreeNode(val=5, left=None, right=None), right=TreeNode(val=15, left=None, right=None))
        return f"TreeNode(val={self.val}, left={repr(self.left)}, right={repr(self.right)})"

        # Show value and existence of children for debugging
        # TreeNode(val=10, left=5, right=15)
        return f"TreeNode(val={self.val}, left={self.left.val if self.left else None}, right={self.right.val if self.right else None})"
```

2. **Basic Tree Operations**
   * Insert in a BST [LC 701](https://github.com/KaranBulani/leetcode_practise/blob/python/Tree%20701%20Insert%20into%20a%20Binary%20Search%20Tree/Solution.py), Delete in a BST [LC 450](https://github.com/KaranBulani/leetcode_practise/blob/python/Tree%20450%20Delete%20Node%20in%20a%20BST/Solution.py).
   * Remember difference between `Binary Tree`[LC 236](https://github.com/KaranBulani/leetcode_practise/blob/python/Tree%20236%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree/Solution.py) vs `Binary Search Tree` [LC 235](https://github.com/KaranBulani/leetcode_practise/blob/python/Tree%20235%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Search%20Tree/Solution.py).

3. **Depth First Search**

    <img src="z_images/img.png" alt="description of your image" width="400" height="325">

   * ###### **Inorder** - [2,3,4,5,6,7]
       ```python
       def inorder(root):
           if not root:
               return
           inorder(root.left)
           print(root.val)
           inorder(root.right)
       ```
     Swap left,right calls in inorder() to print in descending/reverse order.
   * Iterative implementation
       ```python
       def inorder_iterative(root):
           stack, res = [], []
           curr = root

           while stack or curr:
               # Reach the leftmost node
               while curr:
                   stack.append(curr)
                   curr = curr.left
               
               # Backtrack and visit node
               curr = stack.pop()
               res.append(curr.val)

               # Visit right subtree
               curr = curr.right

           return res
       ```
   * ###### **Preorder** - [4,3,2,6,5,7]
       ```python
       def preorder(root):
           if not root:
               return
           print(root.val)
           preorder(root.left)
           preorder(root.right)
       ```
   * Iterative implementation
       ```python
       def preorder_iterative(root):
           if not root:
               return []
       
           stack, res = [root], []
       
           while stack:
               node = stack.pop()
               res.append(node.val)  # Visit root first
       
               # Push right first so left is processed first
               if node.right:
                   stack.append(node.right)
               if node.left:
                   stack.append(node.left)
       
           return res
       ```
   * ###### **Postorder** - [2,3,5,7,6,4]
       ```python
       def postorder(root):
           if not root:
               return
           postorder(root.left)
           postorder(root.right)
           print(root.val)
       ```
   * Iterative implementation
       ```python
       def postorder_iterative_two_stacks(root):
           if not root:
               return []
       
           stack1, stack2, res = [root], [], []
       
           while stack1:
               node = stack1.pop()
               stack2.append(node)
       
               if node.left:
                   stack1.append(node.left)
               if node.right:
                   stack1.append(node.right)
       
           while stack2:
               res.append(stack2.pop().val)
       
           return res
       ```
   * Method B: One Stack (efficient)
       ```python
       def postorder_iterative(root):
           stack, res = [], []
           last_visited = None
           curr = root
       
           while stack or curr:
               if curr:
                   stack.append(curr)
                   curr = curr.left
               else:
                   peek = stack[-1]
                   if peek.right and last_visited != peek.right:
                       curr = peek.right
                   else:
                       res.append(peek.val)
                       last_visited = stack.pop()
       
           return res
       ```
4. **Breadth First Search**
   * Level Order - [4,3,6,2,5,7]
		```python
		from collections import deque

		def bfs(root):
			# Initialize a queue to keep track of nodes during level-order traversal
			queue = deque()
			
			res = [] # final result (list of levels)
			
			# If the root is not None, add it to the queue
			if root:
				queue.append(root)
			
			# Continue until the queue is empty
			while len(queue) > 0:
				level = [] # store values of nodes at the current level
				
				# Iterate over all nodes currently in the queue (current level)
				for _ in range(len(queue)):
					# Remove node from the front 
					curr = queue.popleft()
					# Add its value to the current level
					level.append(curr.val)
					
					# If the node has a left child, add it to the queue
					if curr.left:
						queue.append(curr.left)
					# If the node has a right child, add it to the queue
					if curr.right:
						queue.append(curr.right)
				
				# Append the current level's values to the result
				res.append(level)
			
			# Return the list of levels (level-order traversal result)
			return res
		```
**DFS SUMS**
1. How inorder and preorder list relate with each other. [LC 105](https://github.com/KaranBulani/leetcode_practise/blob/python/Tree%20105%20Construct%20Binary%20Tree%20from%20Preorder%20and%20Inorder%20Traversal/Solution.py)
2. Iterate over a tree (not all at once) [LC 173](https://github.com/KaranBulani/leetcode_practise/blob/python/Tree%20173%20Binary%20Search%20Tree%20Iterator/Solution.py)
3. With DFS two separate things can be calculated `Depth` vs `Res` & how both are different. Usage of `self` vs `nonlocal`. [LC 543](https://github.com/KaranBulani/leetcode_practise/blob/python/Tree%20543%20Diameter%20of%20Binary%20Tree/Solution.py)
   1. Again two separate things can be calculated `Good Node` vs `newMax`.[LC 1448](https://github.com/KaranBulani/leetcode_practise/blob/python/Tree%201448%20Count%20Good%20Nodes%20in%20Binary%20Tree/Solution.py)
   2. Again two separate things can be calculated `MaxPathSum` vs `MaxValue` to be sent on top. [LC 124](https://github.com/KaranBulani/leetcode_practise/blob/python/Tree%20124%20Binary%20Tree%20Maximum%20Path%20Sum/Solution.py)
4. How base case can be more than `return 0/None`. [LC 110](https://github.com/KaranBulani/leetcode_practise/blob/python/Tree%20110%20Balanced%20Binary%20Tree/Solution.py)
5. Not everytime you need to create DFS function. [LC 100](https://github.com/KaranBulani/leetcode_practise/blob/python/Tree%20100%20Same%20Tree/Solution.py), [LC 572](https://github.com/KaranBulani/leetcode_practise/blob/python/Tree%20572%20Subtree%20of%20Another%20Tree/Solution.py)
6. Space, time complexity of iterative and recursive Solution can be different. [LC 235](https://github.com/KaranBulani/leetcode_practise/blob/python/Tree%20235%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Search%20Tree/Solution.py)
7. How Inorder and PreOrder solution can be different. [LC 98](https://github.com/KaranBulani/leetcode_practise/blob/python/Tree%2098%20Validate%20Binary%20Search%20Tree/Solution.py) 
8. Serialize and deserialize using preorder. Normal Tree [LC 297](https://github.com/KaranBulani/leetcode_practise/blob/python/Tree%20297%20Serialize%20and%20Deserialize%20Binary%20Tree/Solution.py) vs BST [LC 449](https://github.com/KaranBulani/leetcode_practise/blob/python/Tree%20449%20Serialize%20and%20Deserialize%20BST/Solution.py)
9. How to handle list of list in tree recursion stack. [LC 113](https://github.com/KaranBulani/leetcode_practise/blob/python/Tree%20113%20Path%20Sum%20II/Solution.py) 
10. Backtracking on Tree [LC 437](https://github.com/KaranBulani/leetcode_practise/blob/python/Tree%20437%20Path%20Sum%20III/Solution.py) 
11. Count number of nodes in tree in O(logn) not O(n) [LC 222](https://github.com/KaranBulani/leetcode_practise/blob/python/Tree%20222%20Count%20Complete%20Tree%20Nodes/Solution.py)
12. Vertical Order Traversal [LC 987](https://github.com/KaranBulani/leetcode_practise/blob/python/Tree%20987%20Vertical%20Order%20Traversal%20of%20a%20Binary%20Tree/Solution.py)

**BFS SUMS**
1. How right side view can actually be a BFS solution. [LC 199](https://github.com/KaranBulani/leetcode_practise/blob/python/Tree%20199%20Binary%20Tree%20Right%20Side%20View/Solution.py)
2. BFS solution implemented with queue and two pointers. [LC 116](https://github.com/KaranBulani/leetcode_practise/blob/python/Tree%20116%20Populating%20Next%20Right%20Pointers%20in%20Each%20Node/Solution.py)

**BOTH**
1. Use of PreOrder DFS, queue in BFS for inverting a Binary Tree. [LC 226](https://github.com/KaranBulani/leetcode_practise/blob/python/Tree%20226%20Invert%20Binary%20Tree/Solution.py)
2. Height of tree using DFS, BFS  [LC 104](https://github.com/KaranBulani/leetcode_practise/blob/python/Tree%20104%20Maximum%20Depth%20of%20Binary%20Tree/Solution.py)
---

## Fenwick Tree (Binary Indexed Tree - BIT) Notes:

---
<img src="z_images/BITSum.png" alt="description of your image" width="400" height="325">

Refer: [GFG Article](https://www.geeksforgeeks.org/dsa/binary-indexed-tree-or-fenwick-tree-2/) or [YT](https://youtu.be/CWDQJGaN1gY?si=YV3ObHkfWAcKXONh)
1. Good for Prefix Sum with regular updates. [LC 307](https://github.com/KaranBulani/leetcode_practise/blob/python/Tree%20307%20Range%20Sum%20Query%20Mutable/Solution.py)
---
# Backtracking:

---
1. Exploring all possible combinations or paths that can be formed from a given set or structure, and you accumulate a sum along the way. 
   1. The recursion (or backtracking) builds the sum incrementally, **exploring both inclusion and exclusion possibilities**. 
   2. Each “sum” corresponds to one complete path of decisions (include/exclude, go left/right, etc.). 
   3. You don’t revisit nodes or edges — it’s choice-based, not connection-based.
2. Types of Sums:

   1. Subset (`DFS - Recursive` & `BFS - Recursive`): Take or Not Take with input having duplicates or not.
   
       _A subset is any selection of elements (possibly none or all) from a set, without caring about order._
       
       * ✅ _Order doesn’t matter (so we dont include results which have same number but different order)_
       * ✅ _Can include empty set_
       * ❌ _No repetition_
       
       _Example:_
       1. Given an integer array nums of unique elements, return all possible subsets. [LC 78](https://github.com/KaranBulani/leetcode_practise/blob/python/Backtracking%2078%20Subsets/Solution.py)
       2. Given an integer array nums that may contain duplicates, return all possible subsets. [LC 90](https://github.com/KaranBulani/leetcode_practise/blob/python/Backtracking%2090%20Subsets%20II/Solution.py) 
          * **In the DFS-style implementation (first solution):** We skip **all consecutive duplicates of the current element** when exploring the *exclude* branch. This ensures that once we decide **not** to include a value, we also skip every identical value that follows at deeper recursion levels.
          * **In the BFS/for-loop-style backtracking (second solution):** We skip duplicates **only at the same recursion level** using the condition `i > start and nums[i] == nums[i - 1]`.  This prevents choosing the same number twice *within a single loop iteration level*, but still allows duplicates to be chosen in deeper levels when valid.Note: In DFS implementation we skip all dups of current element while in BFS we skip dups at same level and Additional `i > start` filter while skipping dups in `for loop` solution implementation.
   
   2. Combination (`DFS - Recursive` & `BFS - Iterative + Recursive`): Go through each nums (`For Loop`) and choose. Refer [LC 77](https://github.com/KaranBulani/leetcode_practise/blob/python/Backtracking%2077%20Combinations/Solution.py) for flowchart.

       _A combination is choosing `r` elements without caring about order, but of fixed size._
       
       * ✅ _Order doesn’t matter_
       * ❌ _No repetition_
       * ⚖️ _Fixed size (r elements)_
       
       _Example:
       Given `{1, 2, 3}`, 2-combinations are:_
       
       ```
       [1,2], [1,3], [2,3]
       ```
       
       ➡️ _Number of combinations = nCr = n! / (r!(n−r)!)_

   3. Permutation(`DFS - Recursive` & `BFS - Iterative + Recursive` & `Iterative (recursively and not recursively)`): Create permutations given distinct numbers. Refer for all four [LC 46](https://github.com/KaranBulani/leetcode_practise/blob/python/Backtracking%2046%20Permutations/Solution.py)
    
       _A permutation is choosing `r` elements where order matters._
       
       * ✅ _Order matters_
       * ❌ _No repetition_
       * ⚖️ _Fixed size (r elements)_
       
       _Example:
       Given `{1, 2, 3}`, 2-permutations are:_
       
       ```
       [1,2], [2,1], [1,3], [3,1], [2,3], [3,2]
       ```
       
       ➡️ _Number of permutations = nPr = n! / (n−r)!_


3. Think of it like this:

     | Action      | What it means                                  |
     | ----------- |------------------------------------------------|
     | Subset      | Pick any boxes you like, order doesn’t matter. |
     | Combination | Pick exactly r boxes, order doesn’t matter.    |
     | Permutation | Pick exactly r boxes, order does matter.       |


**SUMS**
1. Decision whether to take `(` or to not take `(`. [LC 22](https://github.com/KaranBulani/leetcode_practise/blob/python/Backtracking%2022%20Generate%20Parentheses/Solution.py)
3. Decision whether to include or exclude a number considering a targetSum [LC 18](https://github.com/KaranBulani/leetcode_practise/blob/python/Backtracking%2018%204Sum/Solution.py)
4. Decision whether to include or exclude a number considering limit of length. [LC 77](https://github.com/KaranBulani/leetcode_practise/blob/python/Backtracking%2077%20Combinations/Solution.py), For loop recursion rather than normal DFS.
5. Create all permutation of distinct numbers [LC 46](https://github.com/KaranBulani/leetcode_practise/blob/python/Backtracking%2046%20Permutations/Solution.py) & dups number [LC 47](https://github.com/KaranBulani/leetcode_practise/blob/python/Backtracking%2047%20Permutations%20II/Solution.py) Check comments, Didnt implement all ways to solve
6. Find word, start backtracking through each char then move ↑↓→← maintaining backtracking function. [LC 79](https://github.com/KaranBulani/leetcode_practise/blob/python/Backtracking%2079%20Word%20Search/Solution.py)
7. Use of multiple sets to backtrack [LC 51](https://github.com/KaranBulani/leetcode_practise/blob/python/Backtracking%2051%20N%20Queens/Solution.py)
8. MIND FUCK SUMS - Multiple sets with unique way to identify which set to insert to and unique way to call backtrack function. [LC 37](https://github.com/KaranBulani/leetcode_practise/blob/python/Backtracking%2037%20Sudoku%20Solver/Solution.py)
9. MIND FUCK SUMS - Converted input to a graph using BFS, then on that graph implemented DFS [LC 126](https://github.com/KaranBulani/leetcode_practise/blob/python/Backtracking%20126%20Word%20Ladder%20II/Solution.py)
10. Some good sums where preprocessing is done [LC 301](https://github.com/KaranBulani/leetcode_practise/blob/python/Backtracking%20301%20Remove%20Invalid%20Parentheses/Solution.py), [LC 980](https://github.com/KaranBulani/leetcode_practise/blob/python/Backtracking%20980%20Unique%20Paths%20III/Solution.py)
11. Stopped adding more as it felt useless.