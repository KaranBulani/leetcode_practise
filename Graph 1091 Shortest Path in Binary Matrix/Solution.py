'''
Key Observation

This is a shortest path in an unweighted graph problem.
* Each cell is a node.
* You can move in 8 directions.
* Every move has equal cost (1 step).
Whenever you need the shortest path in an unweighted graph, think BFS.

Why BFS Works

BFS explores nodes level by level:
	Distance = 1
	Distance = 2
	Distance = 3
	...
The first time we reach (n-1, n-1), we are guaranteed to have found the shortest path.

Approach
1. If start (0,0) or destination (n-1,n-1) is blocked (1), return -1.
2. Start BFS from (0,0).
3. Explore all 8 neighbors.
4. Mark visited cells so they aren't processed again.
5. When destination is reached, return the current path length.
6. If BFS finishes without reaching destination, return -1.

Complexity
	Let n be the grid size.
	* Time: O(n²)
	  * Each cell is visited at most once.
	* Space: O(n²)
	  * Queue can contain up to all cells.

Interview Pattern Recognition

When you see:
* Grid
* Shortest path
* Equal edge weights
* Minimum number of moves
→ Think BFS

When you see:
* Different costs/weights
→ Think Dijkstra

For this problem, BFS is the optimal solution.
'''
from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        q = deque([(0, 0, 1)])  # row, col, path_length
        grid[0][0] = 1          # mark visited

        while q:
            r, c, dist = q.popleft()

            if r == n - 1 and c == n - 1:
                return dist

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0):
                    grid[nr][nc] = 1
                    q.append((nr, nc, dist + 1))

        return -1

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # -------------------------
        # Examples from question
        # -------------------------
        (
            [[0, 1],
             [1, 0]],
            2
        ),
        (
            [[0, 0, 0],
             [1, 1, 0],
             [1, 1, 0]],
            4
        ),
        (
            [[1, 0, 0],
             [1, 1, 0],
             [1, 1, 0]],
            -1
        ),

        # -------------------------
        # Edge Cases
        # -------------------------

        # Single cell (open)
        (
            [[0]],
            1
        ),

        # Single cell (blocked)
        (
            [[1]],
            -1
        ),

        # Start blocked
        (
            [[1, 0],
             [0, 0]],
            -1
        ),

        # End blocked
        (
            [[0, 0],
             [0, 1]],
            -1
        ),

        # Fully open 2x2
        (
            [[0, 0],
             [0, 0]],
            2
        ),

        # Fully open 3x3
        (
            [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]],
            3
        ),

        # Requires diagonal movement
        (
            [[0, 1, 1],
             [1, 0, 1],
             [1, 1, 0]],
            3
        ),

        # No path despite open start/end
        (
            [[0, 1, 1],
             [1, 1, 1],
             [1, 1, 0]],
            -1
        ),

        # Narrow winding path
        (
            [[0, 0, 1, 1],
             [1, 0, 1, 1],
             [1, 0, 0, 1],
             [1, 1, 0, 0]],
            5
        ),

        # Path along border
        (
            [[0, 1, 1, 1],
             [0, 1, 1, 1],
             [0, 1, 1, 1],
             [0, 0, 0, 0]],
            7
        ),

        # Larger diagonal path
        (
            [[0, 1, 1, 1, 1],
             [1, 0, 1, 1, 1],
             [1, 1, 0, 1, 1],
             [1, 1, 1, 0, 1],
             [1, 1, 1, 1, 0]],
            5
        ),

        # Multiple shortest paths
        (
            [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]],
            3
        ),
    ]

    for idx, (grid, expected) in enumerate(test_cases, start=1):
        result = solution.shortestPathBinaryMatrix([row[:] for row in grid])

        status = "PASS" if result == expected else "FAIL"

        print(
            f"Test {idx:02d}: "
            f"Expected={expected}, "
            f"Got={result} --> {status}"
        )