'''
####################################################################################################
                                                  BFS
####################################################################################################
Time Complexity - O(m×n)

Space Complexity
Worst-case queue size: O(m×n)

from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1":
                    islands += 1

                    queue = deque([(r, c)])
                    grid[r][c] = "0"

                    while queue:
                        row, col = queue.popleft()

                        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                        for dr, dc in directions:
                            nr = row + dr
                            nc = col + dc

                            if (
                                0 <= nr < rows and
                                0 <= nc < cols and
                                grid[nr][nc] == "1"
                            ):
                                queue.append((nr, nc))
                                grid[nr][nc] = "0"

        return islands

####################################################################################################
                                                  DFS
####################################################################################################

Time Complexity
Every cell is visited once. O(m×n)

Space Complexity
Worst-case recursion stack: O(m×n)
Example: Entire grid is land

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(r, c):
            # Boundary + water check
            if (
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                grid[r][c] == "0"
            ):
                return

            # Mark visited
            grid[r][c] = "0"

            # Explore 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands

####################################################################################################
                                                  UnionFind
####################################################################################################

Time Complexity
Almost linear: O(m×n×α(n))
Where:
	α(n) = inverse Ackermann function
	Practically constant
So effectively: O(m×n)

Space Complexity
O(m×n) for parent + rank arrays/maps.
'''

from typing import List


class UnionFind:
    def __init__(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        self.parent = {}
        self.rank = {}
        self.count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    self.parent[(r, c)] = (r, c)
                    self.rank[(r, c)] = 0
                    self.count += 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return

        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX

        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY

        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

        self.count -= 1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        uf = UnionFind(grid)

        directions = [(1, 0), (0, 1)]

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1":

                    for dr, dc in directions:
                        nr = r + dr
                        nc = c + dc

                        if (
                                0 <= nr < rows and
                                0 <= nc < cols and
                                grid[nr][nc] == "1"
                        ):
                            uf.union((r, c), (nr, nc))

        return uf.count


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        {
            "name": "Example 1 - Single Large Island",
            "grid": [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"]
            ],
            "expected": 1
        },
        {
            "name": "Example 2 - Multiple Islands",
            "grid": [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"]
            ],
            "expected": 3
        },
        {
            "name": "Single Cell Land",
            "grid": [
                ["1"]
            ],
            "expected": 1
        },
        {
            "name": "Single Cell Water",
            "grid": [
                ["0"]
            ],
            "expected": 0
        },
        {
            "name": "All Water Grid",
            "grid": [
                ["0", "0", "0"],
                ["0", "0", "0"],
                ["0", "0", "0"]
            ],
            "expected": 0
        },
        {
            "name": "All Land Grid",
            "grid": [
                ["1", "1", "1"],
                ["1", "1", "1"],
                ["1", "1", "1"]
            ],
            "expected": 1
        },
        {
            "name": "Diagonal Lands Not Connected",
            "grid": [
                ["1", "0", "1"],
                ["0", "1", "0"],
                ["1", "0", "1"]
            ],
            "expected": 5
        },
        {
            "name": "Single Row",
            "grid": [
                ["1", "0", "1", "1", "0", "1"]
            ],
            "expected": 3
        },
        {
            "name": "Single Column",
            "grid": [
                ["1"],
                ["0"],
                ["1"],
                ["1"],
                ["0"],
                ["1"]
            ],
            "expected": 3
        },
        {
            "name": "Complex Shape",
            "grid": [
                ["1", "1", "0", "0", "1"],
                ["1", "0", "0", "1", "1"],
                ["0", "0", "1", "0", "0"],
                ["1", "1", "0", "0", "1"]
            ],
            "expected": 5
        },
        {
            "name": "Checkerboard Pattern",
            "grid": [
                ["1", "0", "1", "0"],
                ["0", "1", "0", "1"],
                ["1", "0", "1", "0"],
                ["0", "1", "0", "1"]
            ],
            "expected": 8
        },
        {
            "name": "Island Touching Borders",
            "grid": [
                ["1", "1", "0", "0"],
                ["1", "0", "0", "1"],
                ["0", "0", "1", "1"],
                ["0", "1", "0", "0"]
            ],
            "expected": 3
        }
    ]

    for idx, test in enumerate(test_cases, 1):
        grid_copy = [row[:] for row in test["grid"]]

        result = solution.numIslands(grid_copy)

        print(f"Test Case {idx}: {test['name']}")
        print(f"Expected: {test['expected']}")
        print(f"Your Output: {result}")
        print(f"Passed: {result == test['expected']}")
        print("-" * 50)