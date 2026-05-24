'''
####################################################################################################
                                                  DFS
####################################################################################################
Time Complexity
Every cell visited once. O(rows×cols)

Space Complexity
Worst-case recursion stack: O(rows×cols)
(for completely filled grid)

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            # Out of bounds OR water
            if (
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                grid[r][c] == 0
            ):
                return 0

            # Mark visited
            grid[r][c] = 0

            area = 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)

            return area

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        return max_area

####################################################################################################
                                         BFS (Queue)
####################################################################################################

Time Complexity
O(rows×cols)

Space Complexity
Worst-case queue size: O(rows×cols)

from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        max_area = 0
        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1:
                    queue = deque([(r, c)])
                    grid[r][c] = 0
                    area = 0
                    while queue:
                        row, col = queue.popleft()
                        area += 1

                        for dr, dc in directions:
                            nr = row + dr
                            nc = col + dc

                            if (
                                0 <= nr < rows and
                                0 <= nc < cols and
                                grid[nr][nc] == 1
                            ):
                                grid[nr][nc] = 0
                                queue.append((nr, nc))
                    max_area = max(max_area, area)

        return max_area
####################################################################################################
                                            DFS using visited
####################################################################################################

Time Complexity
O(rows×cols)

Space Complexity
Visited set + recursion stack: O(rows×cols)
'''

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            if (
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                grid[r][c] == 0 or
                (r, c) in visited
            ):
                return 0

            visited.add((r, c))
            area = 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, dfs(r, c))
        return max_area

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1
        (
            [
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
            ],
            6
        ),

        # Example 2
        (
            [[0, 0, 0, 0, 0, 0, 0, 0]],
            0
        ),

        # Single land cell
        (
            [[1]],
            1
        ),

        # Single water cell
        (
            [[0]],
            0
        ),

        # Entire grid is one big island
        (
            [
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]
            ],
            9
        ),

        # Multiple separate islands
        (
            [
                [1, 0, 1, 0],
                [0, 0, 0, 0],
                [1, 1, 0, 1]
            ],
            2
        ),

        # Diagonal connections should NOT count
        (
            [
                [1, 0, 1],
                [0, 1, 0],
                [1, 0, 1]
            ],
            1
        ),

        # Island touching edges
        (
            [
                [1, 1, 0, 0],
                [1, 0, 0, 1],
                [0, 0, 1, 1]
            ],
            3
        ),

        # Long horizontal island
        (
            [[1, 1, 1, 1, 1]],
            5
        ),

        # Long vertical island
        (
            [
                [1],
                [1],
                [1],
                [1]
            ],
            4
        ),

        # Complex shape
        (
            [
                [1, 1, 0, 0, 0],
                [1, 1, 0, 1, 1],
                [0, 0, 0, 1, 1],
                [0, 1, 0, 0, 0]
            ],
            4
        ),
    ]

    for i, (grid, expected) in enumerate(test_cases, 1):
        result = solution.maxAreaOfIsland(grid)
        print(f"Test Case {i}:")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 40)