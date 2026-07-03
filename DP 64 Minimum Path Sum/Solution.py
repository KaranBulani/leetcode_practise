'''
1. Observation

We need to find the minimum sum path from the top-left cell to the bottom-right cell.
At every step we can only move:
* Right
* Down
The answer is the minimum possible sum of all values visited.

Constraints
* Grid size: 1 <= m, n <= 200
* Cell values are non-negative.
* Only two directions are allowed.
Since every path only moves forward (right/down), there are no cycles.

Identify processing direction

To reach any cell (r, c), we can only come from:
* Top (r-1, c)
* Left (r, c-1)
So every cell depends on previously computed cells.

This naturally suggests processing:
* Top → Bottom
* Left → Right

Core Observations

Suppose we're standing at cell (r, c).
There are only two possible ways to arrive here:

From Top
      |
      v
    (r,c)
or
(r,c-1) ---> (r,c)

If we already know:
* Minimum cost to reach top
* Minimum cost to reach left
then the best cost for current cell is simply: current value + minimum(previous top, previous left)

This repeated structure is the key observation.
####################################################################################################

2. Simulation

Consider:
	1 3 1
	1 5 1
	4 2 1

Start:
	1 ? ?
	? ? ?
	? ? ?

First Row Can only move right.
	1 4 5
	? ? ?
	? ? ?

because
	4 = 1+3
	5 = 4+1

First Column Can only move down.
1 4 5
2 ? ?
6 ? ?

Remaining Cells

Cell (1,1):
	Top = 4
	Left = 2

	min = 2

	2 + 5 = 7

	1 4 5
	2 7 ?
	6 ? ?

Cell (1,2):
	Top = 5
	Left = 7

	min = 5

	5 + 1 = 6

	1 4 5
	2 7 6
	6 ? ?

Cell (2,1):
	Top = 7
	Left = 6

	min = 6

	6 + 2 = 8

	1 4 5
	2 7 6
	6 8 ?

Cell (2,2):
	Top = 6
	Left = 8

	min = 6

	6 + 1 = 7

Final DP:
	1 4 5
	2 7 6
	6 8 7

Answer:	7

Generalization

For every cell,
	Minimum Cost(Current Cell) = Current Cell Value + Minimum( Cost from Top, Cost from Left )
This is exactly a recurrence relation.
####################################################################################################

3. Recursion

Build the recurrence relation

Let solve(r,c)
represent the minimum path sum from (0,0) to (r,c).

Base Case
	Starting cell:
	solve(0,0) = grid[0][0]

First Row
	Can only come from left.
	solve(0,c) = grid[0][c] + solve(0,c-1)

First Column
	Can only come from top.
	solve(r,0) = grid[r][0] + solve(r-1,0)

General Cell
solve(r,c) = grid[r][c] + min( solve(r-1,c), solve(r,c-1) )

Parameters
Only two parameters change: (row, column)
####################################################################################################

4. Dynamic Programming

Why DP?
	The recursive solution repeatedly computes the same cells.

Example:
solve(2,2) needs solve(1,2) and solve(2,1)
Both again need solve(1,1)

So many overlapping subproblems occur.

We cache each cell once.

DP State
dp[r][c] = Minimum path sum to reach cell (r,c)

Transition
dp[r][c] = grid[r][c] + min( dp[r-1][c], dp[r][c-1])

Initialization
dp[0][0] = grid[0][0]

First row:
dp[0][c] = grid[0][c] + dp[0][c-1]

First column:
dp[r][0] = grid[r][0] + dp[r-1][0]

DP Table Evolution

Grid
	1 3 1
	1 5 1
	4 2 1
	  ↓
	1 4 5
	2 7 6
	6 8 7

Answer: dp[m-1][n-1]
####################################################################################################

Python (2D DP)

Time Complexity
	States = m × n
	Work per state = O(1)
	Time = O(m × n)

Space Complexity
	DP table O(m × n)
####################################################################################################

Space Optimized DP (1D DP)

Observation
	Notice the recurrence:
	dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1])

	To compute the current row, we only need:
	* the value directly above (previous row)
	* the value to the left (current row)
	So instead of storing the entire m × n table, we can keep a single array representing the current row.

How it Works
	Let dp[c] represent the minimum path sum for column c in the current row.
	Before updating dp[c]:
	* dp[c] = value from the previous row (top)
	* dp[c-1] = value already updated for the current row (left)
	Thus,
	dp[c] = grid[r][c] + min(
				dp[c],      # Top
				dp[c-1]     # Left
			)

Example
	Grid:
		1 3 1
		1 5 1
		4 2 1

	Initial:
		dp = [1, 4, 5]

	After processing second row:
	dp = [2, 7, 6]

	After processing third row:
	dp = [6, 8, 7]

	The last element is the answer.

Python (Space Optimized)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        dp = [0] * cols
        dp[0] = grid[0][0]

        # Initialize first row
        for c in range(1, cols):
            dp[c] = dp[c - 1] + grid[0][c]

        # Process remaining rows
        for r in range(1, rows):
            dp[0] += grid[r][0]  # First column

            for c in range(1, cols):
                dp[c] = grid[r][c] + min(dp[c], dp[c - 1])

        return dp[-1]


Time Complexity - O(m × n)
Space Complexity - O(n)
'''
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        dp = [[0] * cols for _ in range(rows)]

        dp[0][0] = grid[0][0]

        # First row
        for c in range(1, cols):
            dp[0][c] = dp[0][c - 1] + grid[0][c]

        # First column
        for r in range(1, rows):
            dp[r][0] = dp[r - 1][0] + grid[r][0]

        # Remaining cells
        for r in range(1, rows):
            for c in range(1, cols):
                dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1])

        return dp[-1][-1]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1
        (
            [[1, 3, 1],
             [1, 5, 1],
             [4, 2, 1]],
            7
        ),

        # Example 2
        (
            [[1, 2, 3],
             [4, 5, 6]],
            12
        ),

        # Single cell
        (
            [[5]],
            5
        ),

        # Single row
        (
            [[1, 2, 3, 4, 5]],
            15
        ),

        # Single column
        (
            [[1],
             [2],
             [3],
             [4],
             [5]],
            15
        ),

        # All zeros
        (
            [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]],
            0
        ),

        # All same values
        (
            [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]],
            5
        ),

        # Path prefers going down first
        (
            [[1, 100, 100],
             [1, 1, 100],
             [100, 1, 1]],
            5
        ),

        # Path prefers going right first
        (
            [[1, 1, 1],
             [100, 100, 1],
             [100, 100, 1]],
            5
        ),

        # Larger mixed values
        (
            [[5, 9, 6],
             [11, 5, 2],
             [4, 7, 1]],
            22
        ),

        # Large values near constraint
        (
            [[200, 200],
             [200, 200]],
            600
        ),

        # Multiple optimal paths
        (
            [[1, 2, 1],
             [2, 1, 2],
             [1, 2, 1]],
            7
        ),
    ]

    for i, (grid, expected) in enumerate(test_cases, start=1):
        result = solution.minPathSum(grid)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {i}: {status}")
        print(f"Expected: {expected}")
        print(f"Got:      {result}")
        print("-" * 40)