'''
## Intuition

We need to fill each land cell (INF) with the distance to its nearest treasure chest (0).
A naive approach would be:
* For every INF cell, run BFS to find the nearest treasure.
* Time Complexity: O((m*n)²) in the worst case.

Instead, notice that:
* We already know the locations of all treasures.
* Distance from a treasure to nearby cells grows level by level.
So rather than running BFS from every land cell, we run one multi-source BFS starting from all treasure cells simultaneously.

## Key Observation

In BFS:
* Level 0 = treasure cells (0)
* Level 1 = cells at distance 1 from a treasure
* Level 2 = cells at distance 2 from a treasure
* ...
The first time we reach a land cell is guaranteed to be its shortest distance to any treasure.

## Algorithm

1. Add all treasure cells (0) into a queue.
2. Perform BFS.
3. For each popped cell:
   * Visit its 4 neighbors.
   * If a neighbor is INF:
     * Set its value to current distance + 1.
     * Add it to the queue.
4. Continue until queue becomes empty.
Cells that are never reached remain INF.

## Dry Run

### Input
[
 [INF,-1,0,INF],
 [INF,INF,INF,-1],
 [INF,-1,INF,-1],
 [0,-1,INF,INF]
]

Initial Queue: [(0,2), (3,0)]

### BFS Level Expansion

From (0,2):
[
 [INF,-1,0,1],
 [INF,INF,1,-1],
 [INF,-1,INF,-1],
 [0,-1,INF,INF]
]

From (3,0):
[
 [INF,-1,0,1],
 [1,INF,1,-1],
 [1,-1,INF,-1],
 [0,-1,INF,INF]
]
Continue expanding until all reachable cells are updated.

Final:
[
 [3,-1,0,1],
 [2,2,1,-1],
 [1,-1,2,-1],
 [0,-1,3,4]
]

## Why We Don't Need a Visited Set

A cell is added to the queue only when it is INF. When we visit it:
grid[newRow][newCol] = grid[row][col] + 1
It is no longer INF.
Therefore, it can never be added again.
So the grid itself acts as the visited structure.

## Time Complexity

Let:
* m = number of rows
* n = number of columns

Each cell is:
* Added to queue at most once
* Processed at most once

Therefore:
Time Complexity: O(m * n)

## Space Complexity
Queue can contain up to all cells.
Space Complexity: O(m * n)
'''
from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        queue = deque()

        # Add all treasures to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                newRow = row + dr
                newCol = col + dc

                if (
                    0 <= newRow < rows
                    and 0 <= newCol < cols
                    and grid[newRow][newCol] == 2147483647
                ):
                    grid[newRow][newCol] = grid[row][col] + 1
                    queue.append((newRow, newCol))

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1
        (
            [
                [2147483647, -1, 0, 2147483647],
                [2147483647, 2147483647, 2147483647, -1],
                [2147483647, -1, 2147483647, -1],
                [0, -1, 2147483647, 2147483647]
            ],
            [
                [3, -1, 0, 1],
                [2, 2, 1, -1],
                [1, -1, 2, -1],
                [0, -1, 3, 4]
            ]
        ),

        # Example 2
        (
            [
                [0, -1],
                [2147483647, 2147483647]
            ],
            [
                [0, -1],
                [1, 2]
            ]
        ),

        # Single treasure
        (
            [
                [0]
            ],
            [
                [0]
            ]
        ),

        # Single wall
        (
            [
                [-1]
            ],
            [
                [-1]
            ]
        ),

        # Single INF, no treasure reachable
        (
            [
                [2147483647]
            ],
            [
                [2147483647]
            ]
        ),

        # All treasures
        (
            [
                [0, 0],
                [0, 0]
            ],
            [
                [0, 0],
                [0, 0]
            ]
        ),

        # No treasures
        (
            [
                [2147483647, 2147483647],
                [2147483647, 2147483647]
            ],
            [
                [2147483647, 2147483647],
                [2147483647, 2147483647]
            ]
        ),

        # Treasure surrounded by reachable cells
        (
            [
                [2147483647, 2147483647, 2147483647],
                [2147483647, 0, 2147483647],
                [2147483647, 2147483647, 2147483647]
            ],
            [
                [2, 1, 2],
                [1, 0, 1],
                [2, 1, 2]
            ]
        ),

        # Unreachable region due to walls
        (
            [
                [0, -1, 2147483647],
                [-1, -1, 2147483647],
                [2147483647, 2147483647, 2147483647]
            ],
            [
                [0, -1, 2147483647],
                [-1, -1, 2147483647],
                [2147483647, 2147483647, 2147483647]
            ]
        ),

        # Multiple treasures
        (
            [
                [0, 2147483647, 2147483647],
                [2147483647, 2147483647, 2147483647],
                [2147483647, 2147483647, 0]
            ],
            [
                [0, 1, 2],
                [1, 2, 1],
                [2, 1, 0]
            ]
        )
    ]

    for i, (grid, expected) in enumerate(test_cases, start=1):
        solution.islandsAndTreasure(grid)  # modifies grid in-place

        print(f"\nTest Case {i}")
        print("Result:")
        for row in grid:
            print(row)

        print("Expected:")
        for row in expected:
            print(row)

        print("PASS" if grid == expected else "FAIL")