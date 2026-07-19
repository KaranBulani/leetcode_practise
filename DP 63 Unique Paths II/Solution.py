'''
1. Observation

Read the problem statement

We are given an m x n grid.
* 0 → Free cell
* 1 → Obstacle
A robot starts from (0,0) and wants to reach (m-1,n-1).

It can move only:
* Right
* Down
We need to count all possible valid paths.

Identify key observations

	Observation 1
	If a cell contains an obstacle,
	* Robot cannot stand there.
	* Therefore number of ways to reach that cell is 0.

	Observation 2
	To reach any cell (i,j), Robot could have only come from
	* Top (i-1,j)
	* Left (i,j-1)
	because movement is restricted.

	Observation 3
	If both top and left can reach this cell,
	ways(i,j) = ways(top) + ways(left)
	Exactly the same recurrence as Unique Paths I, except obstacles contribute 0 paths.

	Observation 4
	Every cell depends only on previously computed cells.
	This immediately suggests Dynamic Programming.

####################################################################################################
2. Simulation

Consider
0 0 0
0 1 0
0 0 0

Let's fill number of ways.
	Start:
	1 0 0
	0 0 0
	0 0 0

	First row
	1 1 1
	0 0 0
	0 0 0

	Second row
	First cell:		1
	Obstacle: 	0
	Last cell
	top + left
	1 + 0 = 1

	Grid becomes
	1 1 1
	1 0 1
	0 0 0

	Third row
	First cell: 1
	Middle: 1 + 1 = 2
	Last 1 + 2 = 3?
	No.

	Remember:
	Top was 1
	Left was 1

	Actually
	Top = 1
	Left = 1
	Result 2

	Final DP
	1 1 1
	1 0 1
	1 1 2

	Answer 2

Generalization
	For every free cell
	dp[i][j] = dp[i-1][j] + dp[i][j-1]

	Obstacle
	dp[i][j]=0

####################################################################################################
3. Recursion

Define the function

Let	paths(i,j) represent:
> Number of valid paths from (i,j) to destination.

Base Cases

Out of bounds
	return 0

Obstacle
	return 0

Destination reached
	return 1

Transition
From current cell,
Robot has two choices
	Go Down
	Go Right

So, paths(i,j) = paths(i+1,j) + paths(i,j+1)

Why recursion is inefficient?
	Many states repeat.

	Example
	(1,1)
	may be reached from
	* top
	* left
	and computed multiple times.
	So recursion becomes exponential.

####################################################################################################
4. Dynamic Programming

Since recursion has overlapping subproblems, cache each state.

DP State
dp[i][j] = Number of ways to reach cell (i,j).

Transition

	If obstacle
	dp[i][j] = 0

	Otherwise
	dp[i][j] = top + left

	where,
	top = dp[i-1][j] (if exists)
	left = dp[i][j-1] (if exists)

Initialization

	Special cases:
	If starting cell is blocked
		return 0

	Otherwise
		dp[0][0]=1

Fill order

	Since every cell depends on
	* top
	* left

	we compute
	Top → Bottom
	Left → Right

DP Table Example
	Grid
	0 0 0
	0 1 0
	0 0 0

	DP
	1 1 1
	1 0 1
	1 1 2

Python Solution

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = 1

        for i in range(rows):
            for j in range(cols):

                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue

                if i == 0 and j == 0:
                    continue

                top = dp[i - 1][j] if i > 0 else 0
                left = dp[i][j - 1] if j > 0 else 0

                dp[i][j] = top + left

        return dp[-1][-1]

####################################################################################################

Space Optimization

Notice dp[i][j] depends only on
* current row
* previous row

Hence, we can reduce space to O(n).

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        dp = [0] * cols
        dp[0] = 1

        for i in range(rows):
            for j in range(cols):

                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]

        return dp[-1]

Time Complexity

	There are m × n states.
	Each state performs only constant work.
	Using the DP formula:

	> Time Complexity = (# Unique States) × (Work per State)
	= (m × n) × O(1)
	= O(mn)

Space Complexity
	2D DP - O(mn)
	Optimized DP - O(n)
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        dp = [0] * cols
        dp[0] = 1

        for i in range(rows):
            for j in range(cols):

                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]

        return dp[-1]

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1
        (
            [[0, 0, 0],
             [0, 1, 0],
             [0, 0, 0]],
            2
        ),

        # Example 2
        (
            [[0, 1],
             [0, 0]],
            1
        ),

        # Single cell (free)
        (
            [[0]],
            1
        ),

        # Single cell (blocked)
        (
            [[1]],
            0
        ),

        # Start is blocked
        (
            [[1, 0],
             [0, 0]],
            0
        ),

        # Destination is blocked
        (
            [[0, 0],
             [0, 1]],
            0
        ),

        # Single row (no obstacles)
        (
            [[0, 0, 0, 0, 0]],
            1
        ),

        # Single row (obstacle in between)
        (
            [[0, 0, 1, 0, 0]],
            0
        ),

        # Single column (no obstacles)
        (
            [[0],
             [0],
             [0],
             [0]],
            1
        ),

        # Single column (obstacle in between)
        (
            [[0],
             [1],
             [0],
             [0]],
            0
        ),

        # Obstacle forcing only one path
        (
            [[0, 0, 0],
             [1, 1, 0],
             [0, 0, 0]],
            1
        ),

        # No possible path
        (
            [[0, 1, 0],
             [1, 0, 0],
             [0, 0, 0]],
            0
        ),

        # Larger grid with multiple paths
        (
            [[0, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 0]],
            4
        ),

        # Obstacle near destination
        (
            [[0, 0, 0],
             [0, 0, 1],
             [0, 0, 0]],
            3
        ),

        # Entire middle row blocked
        (
            [[0, 0, 0],
             [1, 1, 1],
             [0, 0, 0]],
            0
        ),
    ]

    for i, (obstacleGrid, expected) in enumerate(test_cases, start=1):
        result = solution.uniquePathsWithObstacles(obstacleGrid)

        print(f"Test Case {i}")
        print(f"Grid: {obstacleGrid}")
        print(f"Expected: {expected}")
        print(f"Your Output: {result}")
        print(f"PASS: {result == expected}")
        print("-" * 50)