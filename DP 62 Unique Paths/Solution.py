'''
1. Observation

We start at the top-left corner of an m × n grid.

At every step, the robot can move only:
* Right
* Down
We need to count all possible ways to reach the bottom-right cell.

Identify key words and phrases
* Count number of paths (not the path itself).
* Only two possible moves.
* Every path eventually reaches the destination.
* 1 <= m, n <= 100
* Answer fits in 2 × 10^9.

Identify processing direction
Suppose we are standing at cell (r, c).

Where can we go?
* Right → (r, c+1)
* Down → (r+1, c)

Instead of thinking where can I go, it is often easier to think:

How many ways can I reach this cell?
A cell can only be reached from:
* Above
* Left
This naturally suggests building the answer from smaller subproblems.

Core Observations

Suppose we want the number of ways to reach cell (r, c).

The last move must have come from either:		(r-1, c) or (r, c-1)
Therefore,		                                ways(r,c) = ways(r-1,c) + ways(r,c-1)
This recurrence repeats for every cell.

Since many cells depend on previously computed cells, the problem has overlapping subproblems, making Dynamic Programming a natural choice.
####################################################################################################

2. Simulation

Consider
	m = 3
	n = 4

Grid:
	S . . .
	. . . .
	. . . E

Step 1
There is exactly one way to stay at the starting cell.			1

Step 2
First row		-		Since we can only move right,			1 1 1 1

Step 3
First column		-		Since we can only move down,
1
1
1

Current DP table
1 1 1 1
1 . . .
1 . . .

Step 4
Fill remaining cells.

Cell (1,1)	1 + 1 = 2
1 1 1 1
1 2 . .
1 . . .

Cell (1,2)			2 + 1 = 3
1 1 1 1
1 2 3 .
1 . . .

Cell (1,3)			3 + 1 = 4
1 1 1 1
1 2 3 4
1 . . .

Last row (2,1)		2 + 1 = 3
1 1 1 1
1 2 3 4
1 3 . .

(2,2)				3 + 3 = 6
1 1 1 1
1 2 3 4
1 3 6 .

(2,3)				6 + 4 = 10
Final DP
1 1 1 1
1 2 3 4
1 3 6 10

Answer = 10

Generalization

Every cell depends only on:
* top
* left
So once those are known, the current cell is immediately determined.
####################################################################################################

3. Recursion

Let paths(r, c) represent the number of unique paths from (r, c) to the destination.

Base Cases

Reached destination
	if r == m-1 and c == n-1:
		return 1

Out of bounds
	if r == m or c == n:
		return 0

Recursive Relation
	From (r,c) we have two choices:
	* Move Down
	* Move Right

Therefore,		paths(r,c) = paths(r+1,c) + paths(r,c+1)

Why recursion alone is inefficient?
Many states repeat.

Example:
paths(1,1), may be computed from multiple recursive branches.
This leads to exponential time.
####################################################################################################

4. Dynamic Programming

Step 1 - Identify the state.
	dp[r][c] = number of ways to reach cell (r,c)

Step 2
	Transition
	dp[r][c] = dp[r-1][c] + dp[r][c-1]

Step 3
	Initialization

	First row
	1 1 1 ...

	First column
	1
	1
	1

	because there is only one possible path along the edges.

Step 4
	Fill row by row.
	Finally, dp[m-1][n-1] is the answer.

DP Table Example
	1 1 1 1
	1 2 3 4
	1 3 6 10

Time Complexity

There are		m × n		states.

Each state takes O(1) work.

Therefore,
Time = O(m × n)

Space Complexity
DP table O(m × n)
Can be optimized because each row only depends on the previous row.

Optimized space: O(n)
####################################################################################################

5. Technique Selection

Observation:
* Count total ways.
* Every cell depends on smaller cells.
* Same states appear repeatedly.

				↓
	Recurrence relation exists.
				↓
	Overlapping subproblems.
				↓
	Use Dynamic Programming.
####################################################################################################

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[m - 1][n - 1]

Time Complexity
* O(m × n)

Space Complexity
* O(m × n)
####################################################################################################

Space Optimized Solution (1D DP)

Since each row depends only on the current row and the previous row, we can compress the DP table into a single array.

The key intuition
Think of the 1D array as sliding downward through the grid.

Initially:
    dp = Row 0
    ↓ update
    dp = Row 1
    ↓ update
    dp = Row 2
    ↓ update
    ...
    dp = Last Row

At every step:
    dp[c] (before update) = value from the previous row (top).
    dp[c-1] (after update) = value from the current row (left).

That's why a single array is enough—we overwrite the previous row only after we've used its values. This pattern appears frequently in dynamic programming whenever each state depends only on the current row and the previous row.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for _ in range(1, m):
            for c in range(1, n):
                dp[c] += dp[c - 1]

        return dp[-1]


Time Complexity

* O(m × n)

Space Complexity

* O(n)
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return 1

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (m, n, expected)

        # Examples from the question
        (3, 7, 28),
        (3, 2, 3),

        # Smallest grid
        (1, 1, 1),

        # Single row
        (1, 5, 1),
        (1, 100, 1),

        # Single column
        (5, 1, 1),
        (100, 1, 1),

        # Small square grids
        (2, 2, 2),
        (3, 3, 6),
        (4, 4, 20),
        (5, 5, 70),

        # Rectangular grids
        (2, 3, 3),
        (3, 4, 10),
        (4, 3, 10),
        (5, 3, 15),
        (3, 5, 15),

        # Symmetry checks
        (7, 3, 28),
        (10, 2, 10),
        (2, 10, 10),

        # Larger cases
        (10, 10, 48620),
        (15, 10, 817190),
        (20, 20, 35345263800),  # Note: exceeds LeetCode answer constraint
    ]

    for i, (m, n, expected) in enumerate(test_cases, start=1):
        result = solution.uniquePaths(m, n)

        print(f"Test Case {i}")
        print(f"Input    : m={m}, n={n}")
        print(f"Expected : {expected}")
        print(f"Your Ans : {result}")
        print("PASS" if result == expected else "FAIL")
        print("-" * 40)