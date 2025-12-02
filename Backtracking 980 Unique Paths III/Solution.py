'''
Time complexity:  O(4^(m*n))			worst-case exponential (backtracking)
Space complexity: O(m*n)    			recursion depth in worst case.
'''

class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        start = None
        total_to_visit = 0  # number of squares that must be visited (zeros + start)

        # Count zeros and find start
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    total_to_visit += 1
                elif grid[i][j] == 1:
                    start = (i, j)
                    total_to_visit += 1  # include start in required visits

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        self.paths = 0

        def dfs(r, c, remaining):
            # If out of bounds or on obstacle, stop
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == -1:
                return

            # If we reached the end
            if grid[r][c] == 2:
                # valid only if all required squares have been visited
                if remaining == 0:
                    self.paths += 1
                return

            # Save original value to restore on backtrack
            orig = grid[r][c]
            # Mark visited (use -1 as obstacle)
            grid[r][c] = -1

            # Explore neighbors with one less remaining visit
            for dr, dc in directions:
                dfs(r + dr, c + dc, remaining - 1)

            # Restore original value
            grid[r][c] = orig

        # Start DFS from start cell
        if start:
            sr, sc = start
            dfs(sr, sc, total_to_visit - 1)  # we step on start so remaining decremented by 1

        return self.paths


if __name__ == "__main__":
    solution = Solution()

    grid1 = [
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 2, -1]
    ]
    print("Example 1 Output (Expected = 2):", solution.uniquePathsIII(grid1))

    grid2 = [
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 2]
    ]
    print("Example 2 Output (Expected = 4):", solution.uniquePathsIII(grid2))

    grid3 = [
        [0, 1],
        [2, 0]
    ]
    print("Example 3 Output (Expected = 0):", solution.uniquePathsIII(grid3))

    # Case 4: Start next to end, but there are still empty squares → impossible
    grid4 = [
        [1, 2],
        [0, 0]
    ]
    print("Edge Case 4 (Expected = 0):", solution.uniquePathsIII(grid4))

    # Case 5: Smallest valid grid with no extra empty cells
    grid5 = [
        [1, 2]
    ]
    print("Edge Case 5 (Expected = 1):", solution.uniquePathsIII(grid5))

    # Case 6: All empty except start + end, simple straight path
    grid6 = [
        [1, 0, 2]
    ]
    print("Edge Case 6 (Expected = 1):", solution.uniquePathsIII(grid6))

    # Case 7: Start surrounded by obstacles → no path
    grid7 = [
        [-1, -1, -1],
        [-1, 1, -1],
        [-1, 2, -1]
    ]
    print("Edge Case 7 (Expected = 0):", solution.uniquePathsIII(grid7))

    # Case 8: Multiple paths but must use all open squares exactly once
    grid8 = [
        [1, 0, 0],
        [0, -1, 0],
        [0, 0, 2]
    ]
    print("Edge Case 8 (Expected = 2):", solution.uniquePathsIII(grid8))

    # Case 9: 1x1 impossible grid (start cannot also be end)
    grid9 = [
        [1]
    ]
    print("Edge Case 9 (Expected = 0):", solution.uniquePathsIII(grid9))

    # Case 10: 1x2 but cells reversed end-start
    grid10 = [
        [2, 1]
    ]
    print("Edge Case 10 (Expected = 0):", solution.uniquePathsIII(grid10))