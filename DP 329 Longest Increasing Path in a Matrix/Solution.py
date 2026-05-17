'''
1. Observation

We are given a matrix, and from every cell we can move:
* Up
* Down
* Left
* Right
We need to find the length of the longest strictly increasing path.

Important:
	* We can start from any cell
	* We cannot move diagonally
	* We cannot leave matrix bounds
	* Every next value must be strictly greater

Graph Interpretation

	Think of every cell as a node.

	We create a directed edge:
	A → B
	if matrix[B] > matrix[A]

	Since values must strictly increase:
	* Cycles are impossible
	* Graph becomes a DAG

	That means:
	* DFS + Memoization works perfectly
####################################################################################################

2. Simulation

Example:
matrix =
[
 [9,9,4],
 [6,6,8],
 [2,1,1]
]

Start from cell 1 at (2,1):

	Possible moves:
	1 → 2
	2 → 6
	6 → 9
	Length becomes: 4

Now notice:

	While exploring from different cells, we repeatedly compute:
	longest path from 6
	longest path from 9
	again and again.
	So we cache results.
####################################################################################################

3. Recursion

Define recursive function: dfs(r, c)

Meaning:
	Returns longest increasing path starting from (r, c)

Base Case
	If no neighboring cell is larger:
	Return 1
	because current cell itself forms a path.

Recursive Transition
	For every direction:
	* Check bounds
	* Check increasing condition

	If valid:
	1 + dfs(nr, nc)

	Take maximum over all neighbors.

Recurrence Relation

Let:
f(r, c) = longest path starting from (r, c)

Then:
f(r, c) = 1 + max(f(nr, nc))
for all valid increasing neighbors.

Otherwise:
f(r, c) = 1
####################################################################################################
4. Dynamic Programming

DP State
dp[r][c] = longest increasing path starting from (r, c)

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        dp = {}

        def dfs(r: int, c: int) -> int:

            if (r, c) in dp:
                return dp[(r, c)]

            longest = 1

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and matrix[nr][nc] > matrix[r][c]
                ):
                    longest = max(longest, 1 + dfs(nr, nc))

            dp[(r, c)] = longest
            return longest

        ans = 0

        for r in range(rows):
            for c in range(cols):
                ans = max(ans, dfs(r, c))

        return ans

Time Complexity
    There are: m * n states.
    For every state we check 4 directions.
    So:
    Time = O(m * n * 4)
          = O(m * n)

Space Complexity
    Memo table: O(m * n)
    Recursion stack worst case: O(m * n)
    Total: O(m * n)
####################################################################################################
                                            BRUTE FORCE
####################################################################################################

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r: int, c: int) -> int:
            longest = 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and matrix[nr][nc] > matrix[r][c]
                ):
                    longest = max(longest, 1 + dfs(nr, nc))

            return longest

        ans = 0

        for r in range(rows):
            for c in range(cols):
                ans = max(ans, dfs(r, c))

        return ans

Let:
* ( m ) = number of rows
* ( n ) = number of cols
So total cells = ( m * n )

Time Complexity
    For every cell, you start a DFS:
    So DFS is called: O(m * n) times.

    Inside each DFS:
    * you can move in 4 directions
    * and because there is no memoization, the same paths are recomputed again and again.
    A loose upper bound is: O((m * n) . 4^(m * n))
    because:
    * each DFS can branch up to 4 ways
    * maximum path length can be (m * n)

Space Complexity
    Two components:

    1. Recursion stack
    In worst case, path length can include all cells:
    So recursion depth can become: O(m * n)

    2. Extra space
    No visited set.
    No DP table.
    So no additional major memory.

'''


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        dp = {}

        def dfs(r: int, c: int) -> int:

            if (r, c) in dp:
                return dp[(r, c)]

            longest = 1

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and matrix[nr][nc] > matrix[r][c]
                ):
                    longest = max(longest, 1 + dfs(nr, nc))

            dp[(r, c)] = longest
            return longest

        ans = 0

        for r in range(rows):
            for c in range(cols):
                ans = max(ans, dfs(r, c))

        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Basic examples from question
        [[3, 4, 5], [3, 2, 6], [2, 2, 1]],
        [[1]],
        [[9, 9, 4], [6, 6, 8], [2, 1, 1]],

        # Edge cases
        [[7, 7, 7], [7, 7, 7], [7, 7, 7]],  # all same values
        [[1, 2, 3, 4, 5]],  # single row increasing
        [[5, 4, 3, 2, 1]],  # single row decreasing
        [[1], [2], [3], [4], [5]],  # single column increasing
        [[5], [4], [3], [2], [1]],  # single column decreasing

        # Plateau with one increasing path
        [[1, 2, 2], [2, 2, 3], [2, 2, 4]],

        # Larger mixed case
        [[7, 8, 9], [9, 7, 6], [7, 2, 3]],

        # Spiral increasing
        [[1, 2, 3],
         [6, 5, 4],
         [7, 8, 9]],

        # Multiple possible paths
        [[1, 2, 3],
         [6, 5, 4],
         [7, 6, 5]],

        # Strictly decreasing grid
        [[9, 8, 7],
         [6, 5, 4],
         [3, 2, 1]],

        # Random shape
        [[0, 1, 2, 3],
         [5, 4, 3, 2],
         [6, 7, 8, 9],
         [5, 4, 3, 2]],
    ]

    for i, matrix in enumerate(test_cases):
        result = solution.longestIncreasingPath(matrix)
        print(f"Test Case {i + 1}: {result}")