'''
This is a classic multi-source BFS problem.

Key Observation
All rotten oranges (2) spread rot simultaneously every minute.
Instead of running BFS from each rotten orange separately, we:
1. Put all rotten oranges into the queue initially.
2. Count the number of fresh oranges.
3. Process the queue level-by-level.
   * One BFS level = one minute.
4. Every time a fresh orange becomes rotten:
   * decrement fresh count
   * add it to the queue
5. At the end:
   * If fresh oranges remain → return -1
   * Otherwise return minutes elapsed.

Example
2 1 1
1 1 0
0 1 1

Initial queue: [(0,0)]

Minute 1:
2 2 1
2 1 0
0 1 1

Minute 2:
2 2 2
2 2 0
0 1 1

Minute 3:
2 2 2
2 2 0
0 2 1

Minute 4:
2 2 2
2 2 0
0 2 2

Answer = 4.

Why minutes += 1 after each level?
	A BFS level represents oranges that become rotten during the same minute.
		while queue:
			for _ in range(len(queue)):  # current minute's oranges
				...
			minutes += 1
	This ensures all oranges rotten at minute t spread simultaneously and only affect oranges at minute t + 1.

Complexity
* Time: O(m * n)
  * Every cell is processed at most once.
* Space: O(m * n)
  * Queue may contain all cells in the worst case.
This is the optimal solution and the standard interview approach for Rotting Oranges.
'''

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        fresh = 0

        # Find all rotten oranges and count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # No fresh oranges
        if fresh == 0:
            return 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = 0

        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))

            minutes += 1

        return minutes if fresh == 0 else -1


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # =========================
        # Examples from question
        # =========================
        (
            [[2, 1, 1],
             [1, 1, 0],
             [0, 1, 1]],
            4
        ),
        (
            [[2, 1, 1],
             [0, 1, 1],
             [1, 0, 1]],
            -1
        ),
        (
            [[0, 2]],
            0
        ),

        # =========================
        # Single cell cases
        # =========================
        (
            [[0]],
            0
        ),
        (
            [[1]],
            -1
        ),
        (
            [[2]],
            0
        ),

        # =========================
        # No rotten oranges
        # =========================
        (
            [[1, 1],
             [1, 1]],
            -1
        ),

        # =========================
        # No fresh oranges
        # =========================
        (
            [[2, 2],
             [0, 2]],
            0
        ),

        # =========================
        # Simple propagation
        # =========================
        (
            [[2, 1]],
            1
        ),
        (
            [[2, 1, 1]],
            2
        ),
        (
            [[2],
             [1],
             [1]],
            2
        ),

        # =========================
        # Multiple rotten sources
        # =========================
        (
            [[2, 1, 1],
             [1, 1, 1],
             [1, 1, 2]],
            2
        ),

        # =========================
        # Fresh orange isolated by empties
        # =========================
        (
            [[2, 0, 1]],
            -1
        ),
        (
            [[2, 0],
             [0, 1]],
            -1
        ),

        # =========================
        # Rotten oranges separated,
        # all fresh still reachable
        # =========================
        (
            [[2, 1, 1],
             [1, 1, 1],
             [1, 1, 2]],
            2
        ),

        # =========================
        # Larger propagation
        # =========================
        (
            [[2, 1, 1, 1],
             [1, 1, 1, 1],
             [1, 1, 1, 1]],
            5
        ),

        # =========================
        # Empty grid cells only
        # =========================
        (
            [[0, 0, 0],
             [0, 0, 0]],
            0
        ),

        # =========================
        # Fresh oranges surrounded
        # by empty cells
        # =========================
        (
            [[2, 0, 0],
             [0, 1, 0],
             [0, 0, 0]],
            -1
        ),

        # =========================
        # Rotten source in center
        # =========================
        (
            [[1, 1, 1],
             [1, 2, 1],
             [1, 1, 1]],
            2
        ),

        # =========================
        # Max-distance corner case
        # =========================
        (
            [[2, 1, 1, 1, 1]],
            4
        ),
    ]

    for idx, (grid, expected) in enumerate(test_cases, start=1):
        result = solution.orangesRotting([row[:] for row in grid])

        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {idx}: {status}")
        print(f"Expected: {expected}")
        print(f"Got     : {result}")
        print("-" * 40)