"""
1. Understanding the problem

You are given an (n x n) binary matrix.

Each Quad Tree node has:

- val: True if the represented region contains 1, otherwise False.
- isLeaf: True if the node represents a uniform region.
- topLeft, topRight, bottomLeft, bottomRight: Four child nodes.

There are two possible situations:

Case 1: All elements are identical
    If a region contains only 0s or only 1s, create a leaf node.

Case 2: Elements are different
    Divide the region into four equal quadrants and recursively construct a Quad Tree for each quadrant.

######################################################################################################################################################################
                                                                            Solution 1
######################################################################################################################################################################
2. Python solution

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # r, c of topLeft corner
        def dfs(r, c, size):

            # Check whether the current region is uniform
            first = grid[r][c]
            uniform = True

            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != first:
                        uniform = False
                        break
                if not uniform:
                    break

            # If uniform, create a leaf node
            if uniform:
                return Node(first == 1, True, None, None, None, None)

            # Divide into four quadrants
            half = size // 2

            topLeft = dfs(r, c, half)
            topRight = dfs(r, c + half, half)
            bottomLeft = dfs(r + half, c, half)
            bottomRight = dfs(r + half, c + half, half)

            # Create an internal node
            return Node( True, False, topLeft, topRight, bottomLeft, bottomRight )

        return dfs(0, 0, len(grid))


######################################################################################################################################################################
3. Dry run

Consider this grid:

    grid = [
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [1, 0, 1, 1],
            [0, 1, 1, 1]
        ]

First, examine the entire 4 × 4 grid.
It contains both 0 and 1, so divide it into four 2 × 2 quadrants.
Notice that the bottom-left quadrant is also non-uniform, so it gets divided into four 1 × 1 quadrants.
Each of those becomes a leaf node.
The final tree structure is:

                 Root
                  |
        -----------------------
       |      |        |       |
      TL      TR       BL      BR
       1       0       |       1
                       |
                  -----------
                 |   |   |   |
                 1   0   0   1

######################################################################################################################################################################
4. Complexity analysis

Let (N) be the dimension of the grid.

| Complexity | Value               | Explanation                                                                                |
| ---------- | ------------------- | ------------------------------------------------------------------------------------------ |
| Time       | (O(N^2 x log N))    | Each level examines regions covering at most (N^2) cells, with (O(\log N)) levels.         |
| Space      | (O(N^2))            | Worst-case Quad Tree nodes, plus recursion stack.                                          |

######################################################################################################################################################################
Time complexity explanation

Let (N) be the dimension of the grid. The input contains (N × N) elements.

1. Time complexity derivation

    There are two operations happening in every recursive call:
    1. Checking whether the current region is uniform.
    2. Recursively dividing the region into four quadrants if it isn't uniform.

    Let's analyse them separately.

Step 1: Cost of checking uniformity

    Consider a region of size (N × N).

        for i in range(r, r + size):
            for j in range(c, c + size):
                if grid[i][j] != first:
                    uniform = False
                    break

    In the worst case, we examine every element.
    Therefore:    T(N) = O(N^2)

    But this is just the cost of one recursive call, not the entire algorithm.

Step 2: Recursive calls

    If the region is not uniform, we divide it into four quadrants.
    Each quadrant has dimensions:     N/2 * N/2

    Therefore, we make four recursive calls, each with input size (N/2).
    The recurrence becomes:     T(N) = 4T(N/2) + O(N^2)

    This is where the Master Theorem comes in.

Step 3: Apply Master Theorem

    The general Master Theorem recurrence is:     T(N) = aT(N/b) + O(N^d)

    Now compare both equations "T(N) = 4T(N/2) + O(N^2)" with "T(N) = aT(N/b) + O(N^d)",
    
    For our problem it becomes:
    | Variable | Value | Meaning                          |
    | -------- | ----- | -------------------------------- |
    | (a)      | 4     | Four recursive calls             |
    | (b)      | 2     | Each dimension is halved         |
    | (d)      | 2     | Uniformity check takes (N^2)     |
    
    The Master Theorem uses the expression:     N^{log_b a}
    It represents the growth of the total work contributed by the recursive calls at the bottom of the recursion tree.
    

    Let's derive it.

    At each recursive level:
    - Number of subproblems increases by (a).
    - Input size of each subproblem decreases by a factor of (b).

    After (k) levels:
    Number of subproblems:       a^k 
    Size of each subproblem:    N / b^k

    We continue until each subproblem reaches size 1.

    Therefore:                  N / b^k = 1
    Rearranging:                N = b^k

    Taking logarithm base (b):            k = log_b N
    Now substitute this into the number of subproblems:               a^k = a^(log_b N)
    Using the logarithm identity:                                           a^(log_b N) = N^(log_b a)
    And that's where the expression comes from!

    Now calculate:     N^{log_b a} = N^{log_2 4}           = N^2
    Compare this with the non-recursive work:         f(N) = N^2
    Both are equal.

    So, (N^2) is the work at each recursion level, not the total work across all levels.

    How many levels do we have?
    At every level, the dimension is halved:     N  ➜  N/2 ➜ N/4 ➜ .... ➜ 1

    Therefore: N/(2^k) = 1 
            2^k = N
            k = log_2 N

    Total work: N^2 × log_2 N

Step 4: Understand it using recursion levels

This is perhaps the easiest way to understand why we get (N^2 . log N).

Recursion tree

    Level 0
        1 region of N × N
        Work = N²
      ⇩

    Level 1
        4 regions of N/2 × N/2
        Work = 4 × (N/2)² = N²
      ⇩

    Level 2
        16 regions of N/4 × N/4
        Work = 16 × (N/4)² = N²
      ⇩

    Continue dividing...
      ⇩

    Last level
        N² regions of 1 × 1
        Work = N² × 1 = N²

Notice something interesting:

At every level, the total number of elements examined in the worst case is (N^2).

Why?

| Level | Number of regions | Size of each region | Total work |
| ----- | ----------------- | ------------------- | ---------- |
| 0     | 1                 | N²                  | N²         |
| 1     | 4                 | N²/4                | N²         |
| 2     | 16                | N²/16               | N²         |
| 3     | 64                | N²/64               | N²         |
| k     | 4ᵏ                | N²/4ᵏ               | N²         |

How many levels do we have?

At every level, the dimension is halved:     N  ➜  N/2 ➜ N/4 ➜ .... ➜ 1

Therefore: N/(2^k) = 1 
           2^k = N
           k = log_2 N

Total work: N^2 × log_2 N

Time complexity                             O(N^2 × log N)
######################################################################################################################################################################

2. Space complexity derivation

    There are two things to consider:
    1. Recursion stack space.
    2. Quad Tree nodes created.

Step 1: Recursion stack

    Consider the deepest recursive path.
    Every recursive call divides the region into four, but we execute these calls sequentially.

        topLeft = dfs(...)
        topRight = dfs(...)
        bottomLeft = dfs(...)
        bottomRight = dfs(...)

    We finish the top-left subtree before moving to top-right.
    Therefore, we don't have all four recursive calls active simultaneously.

    The maximum recursion depth is:      N ➜ N/2 ➜ N/4 ➜ .... ➜ 1
    So:                                  O(log N)

    This is the auxiliary recursion stack space.

Step 2: Quad Tree nodes

    Now consider how many nodes we create.
    In the worst case, every region is divided until we reach individual cells.
    The tree becomes a full 4-ary tree.

    | Level | Number of nodes |
    | ----- | --------------- |
    | 0     | 1               |
    | 1     | 4               |
    | 2     | 16              |
    | 3     | 64              |
    | k     | 4ᵏ              |

    At the last level i.e. k = log N:                   4^(log_2 N) ➜  N^(log_2 4) ➜ N^2 are total the number of nodes

    Total nodes:                                        1 + 4 + 16 + .... + N^2

    This is a geometric series:
                                                        S = 4^(k + 1) - 1 / 4 - 1

    Therefore:                                          S = O(N^2)

    So the Quad Tree itself requires:                   O(N^2)

Step 3: Total space complexity

    | Component       | Space                   |
    | --------------- | ----------------------- |
    | Recursion stack | O(log N)                |
    | Quad Tree nodes | O(N²)                   |
    | Input grid      | O(N²), already provided |

    If we count only the additional space used by the algorithm: O(N^2) + O(log N)
                                                                 O(N^2)

Space complexity                                        O(N^2)

######################################################################################################################################################################
                                                                            Solution 2
######################################################################################################################################################################
Our objective is to efficiently determine whether a given region contains all 0s, all 1s, or a mixture.
This is where Prefix Sum comes in.

######################################################################################################################################################################
2. Prefix Sum Approach

    Instead of iterating over every cell in a region to determine whether it contains all 0s or all 1s, we can use a 2D Prefix Sum matrix.
    The idea is to preprocess the matrix so that we can calculate the sum of any rectangular region in O(1) time.

    Since our matrix contains only 0s and 1s:
    - If the sum of a region is 0, the entire region contains 0s.
    - If the sum equals the total number of cells in the region, the entire region contains 1s.
    - Otherwise, the region contains a mixture of 0s and 1s.

2.1 Construct the Prefix Sum Matrix

    Let:        prefix[i][j] represent the sum of all elements from (0, 0) to (i-1, j-1) in the original grid.

    We use an additional row and column of zeros to simplify boundary handling.
    The dimensions of the prefix matrix will be:            (n + 1) x (n + 1)

    Formula:
        prefix[i][j] = (
            grid[i-1][j-1]
            + prefix[i-1][j]
            + prefix[i][j-1]
            - prefix[i-1][j-1]
        )

    Why do we subtract prefix[i-1][j-1]?
        Because the top-left region gets counted twice when we add the top and left prefix sums.
        Therefore, we subtract it once.

2.2 Example

    Consider this grid:
        1 1 0 0
        1 1 0 0
        0 0 1 1
        0 0 1 1


    Its prefix sum matrix becomes:
        0 0 0 0 0
        0 1 2 2 2
        0 2 4 4 4
        0 2 4 5 6
        0 2 4 6 8

    Notice that we have an extra row and column containing zeros.

######################################################################################################################################################################
3. Calculate Sum of Any Region in O(1)

    Suppose we want to calculate the sum of a rectangular region.

    We define the region using four boundaries:

    - r1: Starting row (inclusive)
    - c1: Starting column (inclusive)
    - r2: Ending row (exclusive)
    - c2: Ending column (exclusive)

    The formula is:         total = (    prefix[r2][c2]    - prefix[r1][c2]    - prefix[r2][c1]    + prefix[r1][c1])

    Why does this work?
        We start with the prefix sum from (0, 0) to (r2-1, c2-1).

    Then:
        1. Subtract the region above our required rectangle.
        2. Subtract the region to the left.
        3. Add back the top-left overlapping region because it was subtracted twice.

    This gives us the sum of only the required rectangle.
    Time Complexity: O(1)
    No matter how large the rectangle is, we only perform four prefix sum lookups.

######################################################################################################################################################################
4. Recursive Quad Tree Construction

Now that we can calculate the sum of any region in O(1), constructing the Quad Tree becomes straightforward.

We maintain four boundaries:
    r1, c1, r2, c2

Initially:
    r1 = 0
    c1 = 0
    r2 = n
    c2 = n


Here, r2 and c2 are exclusive boundaries.

Step 1: Calculate the region sum
    total = get_sum(r1, c1, r2, c2)

Step 2: Check whether the region is uniform

Calculate the number of cells:
    area = (r2 - r1) * (c2 - c1)

There are three possibilities:

    Case 1: All elements are 0
    if total == 0:
    Create a leaf node:     Node(False, True)

    Case 2: All elements are 1
    elif total == area:
    Create a leaf node:     Node(True, True)

    Case 3: Mixture of 0s and 1s
    We need to divide the current region into four quadrants.
    Calculate the middle positions:     mid_r = (r1 + r2) // 2mid_c = (c1 + c2) // 2


The four recursive calls will be:
Top Left:     (r1,    c1,    mid_r, mid_c)
Top Right:    (r1,    mid_c, mid_r, c2)
Bottom Left:  (mid_r, c1,    r2,    mid_c)
Bottom Right: (mid_r, mid_c, r2,    c2)

Create a non-leaf node and attach the four children.

######################################################################################################################################################################
5. Complete Python Solution

below in code

######################################################################################################################################################################
6. Dry Run

Consider the following input:
    1 1 0 0
    1 1 0 0
    0 0 1 1
    0 0 1 1

Initially, we call: build(0, 0, 4, 4)

Level 0: Entire grid
- Area = 4 * 4 = 16
- Sum = 8
- Since sum is neither 0 nor 16, divide into four quadrants.

Level 1: Four quadrants
| Quadrant     | Sum | Area | Result       |
| ------------ | --- | ---- | ------------ |
| Top Left     | 4   | 4    | Leaf (True)  |
| Top Right    | 0   | 4    | Leaf (False) |
| Bottom Left  | 0   | 4    | Leaf (False) |
| Bottom Right | 4   | 4    | Leaf (True)  |

All four quadrants are uniform.
Therefore, we do not need any further recursion.
The resulting Quad Tree has:

                    Root
                (False, False)
                /   |    \    \
               /    |     \    \
              TL   TR     BL    BR
             True False  False  True
             Leaf Leaf   Leaf   Leaf

Notice that the root has val = False because it is not a leaf node. Its value does not represent the entire grid.

######################################################################################################################################################################

7. Time Complexity Analysis

Let N be the dimension of the grid.
The grid contains N² elements.

A. Building the Prefix Sum Matrix
    We iterate over every element exactly once.
    Time Complexity:             O(N^2)

B. Recursive Quad Tree Construction

For every recursive call:
- We calculate the region sum in O(1).
- We calculate the area in O(1).
- We either return a leaf or make four recursive calls.

The maximum recursion depth is:          log_2 N
    
    Why?
    Every time we divide a region, its side length becomes half.
    After k divisions:                      N / (2^k) = 1
    Therefore:                              2^k = N 
                                            k = log_2 N

At each level, the total area covered by all regions is at most N².

For example:

| Level | Number of regions | Area per region | Total area |
| ----- | ----------------- | --------------- | ---------- |
| 0     | 1                 | N²              | N²         |
| 1     | 4                 | N²/4            | N²         |
| 2     | 16                | N²/16           | N²         |
| 3     | 64                | N²/64           | N²         |
| k     | 4^k               | N²/4^k          | N²         |

Since each region requires only O(1) work, the total work per level is proportional to the number of regions at that level.
The maximum number of levels is log N.
Therefore, the worst-case recursive time complexity is:         O(N^2 log N)

C. Overall Time Complexity

Prefix Sum construction:                                        O(N^2)
Recursive construction:                                         O(N^2 × log N)
Combining:                                                      O(N^2) + O(N^2 × log N)
Final Time Complexity                                           O(N^2 × log N)

######################################################################################################################################################################
8. Space Complexity Analysis

There are three major contributors.

| Component         | Space            |
| ----------------- | ---------------- |
| Prefix Sum Matrix | O(N²)            |
| Quad Tree Nodes   | O(N²) worst case |
| Recursion Stack   | O(log N)         |

Why are Quad Tree nodes O(N²) in the worst case?

In the worst case, the grid keeps dividing until every individual cell becomes a leaf.
There are N² leaf nodes.
A full Quad Tree has approximately:             1 + 4 + 16 + .... + N^2

This is a geometric series:             4^{log_2 N+1} - 1 / (4 - 1)

Since 4^{log_2 N}=N^2 , this becomes O(N²).

Therefore:  O(N^2) + O(N^2) + O(log N)

Final Space Complexity              O(N^2)

"""
from typing import List

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:

    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        # Step 1: Build 2D Prefix Sum Matrix
        prefix = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                prefix[i][j] = ( grid[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] )

        # Step 2: Calculate sum of any rectangular region
        def get_sum(r1, c1, r2, c2):
            return (prefix[r2][c2] - prefix[r1][c2] - prefix[r2][c1] + prefix[r1][c1])

        # Step 3: Recursively construct Quad Tree
        def build(r1, c1, r2, c2):

            total = get_sum(r1, c1, r2, c2)
            area = (r2 - r1) * (c2 - c1)

            # Case 1: Entire region contains 0s
            if total == 0:
                return Node(False, True)

            # Case 2: Entire region contains 1s
            if total == area:
                return Node(True, True)

            # Case 3: Region contains both 0s and 1s
            # Divide into four quadrants

            mid_r = (r1 + r2) // 2
            mid_c = (c1 + c2) // 2

            root = Node(False, False)
            root.topLeft = build( r1, c1, mid_r, mid_c )
            root.topRight = build( r1, mid_c, mid_r, c2 )
            root.bottomLeft = build(mid_r, c1, r2, mid_c)
            root.bottomRight = build( mid_r, mid_c, r2, c2 )
            return root

        return build(0, 0, n, n)

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1: LeetCode
        [
            [0, 1],
            [1, 0]
        ],

        # Example 2: LeetCode
        [
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0]
        ],

        # All zeros
        [
            [0, 0],
            [0, 0]
        ],

        # All ones
        [
            [1, 1],
            [1, 1]
        ],

        # 4x4 all zeros
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],

        # 4x4 all ones
        [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ],

        # Four uniform quadrants with different values
        [
            [0, 0, 1, 1],
            [0, 0, 1, 1],
            [1, 1, 0, 0],
            [1, 1, 0, 0]
        ],

        # Alternating checkerboard pattern
        [
            [0, 1, 0, 1],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 1, 0]
        ],

        # 4x4: Three uniform quadrants and one mixed quadrant
        [
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 1, 0]
        ],

        # 8x8: Only one small region differs
        [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 0]
        ]
    ]

    def print_tree(node, level=0, position="Root"):
        if node is None:
            return

        print(
            "  " * level
            + f"{position}: val={node.val}, isLeaf={node.isLeaf}"
        )

        if not node.isLeaf:
            print_tree(node.topLeft, level + 1, "TopLeft")
            print_tree(node.topRight, level + 1, "TopRight")
            print_tree(node.bottomLeft, level + 1, "BottomLeft")
            print_tree(node.bottomRight, level + 1, "BottomRight")

    for i, grid in enumerate(test_cases, 1):
        print(f"\n{'=' * 40}")
        print(f"Test Case {i}")
        print(f"Grid size: {len(grid)}x{len(grid)}")

        result = solution.construct(grid)

        print_tree(result)
