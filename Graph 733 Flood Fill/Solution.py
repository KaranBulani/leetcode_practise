'''
####################################################################################################
                                                  DFS
####################################################################################################
class Solution:
    def floodFill(self, image, sr, sc, color):
        rows, cols = len(image), len(image[0])
        original = image[sr][sc]

        # If original color is same as target color
        # no need to process
        if original == color:
            return image

        def dfs(r, c):
            # Boundary check
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # Only process cells with original color
            if image[r][c] != original:
                return

            # Change color
            image[r][c] = color

            # Explore 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)

        return image

Time Complexity
Each cell is visited at most once. O(m×n)

Space Complexity
Recursive stack space
Worst case: O(m×n)
####################################################################################################
                                                  BFS
####################################################################################################

from collections import deque

class Solution:
    def floodFill(self, image, sr, sc, color):
        rows, cols = len(image), len(image[0])
        original = image[sr][sc]

        # No work needed
        if original == color:
            return image

        q = deque()
        q.append((sr, sc))

        # Change starting cell color
        image[sr][sc] = color

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Valid cell with original color
                if (0 <= nr < rows and
                    0 <= nc < cols and
                    image[nr][nc] == original):

                    image[nr][nc] = color
                    q.append((nr, nc))

        return image

Time Complexity
Each cell is visited at most once: O(m×n)

Space Complexity
Queue can hold all cells in worst case: O(m×n)

####################################################################################################
                                            MY SOLUTION
####################################################################################################

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows = len(image)
        cols = len(image[0])
        visited = set()

        def dfs(sr: int, sc: int) -> None:
            temp = image[sr][sc]
            image[sr][sc] = color
            visited.add((sr, sc))

            for dr, dc in dirs:
                nr, nc = sr + dr, sc + dc
                if (0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == temp and (nr, nc) not in visited):
                    dfs(nr, nc)
        dfs(sr, sc)
        return image

Time Complexity

Let:    m = number of rows    n = number of cols
Each cell is:
    visited at most once
    processed once in DFS
So: O(m×n)
Worst case occurs when the entire grid has the same color.

Space Complexity

You are using:
    visited set
    recursion call stack
Visited set can store all cells: O(m×n)
Recursion stack in worst case DFS can go through all cells: O(m×n)
So total auxiliary space: O(m×n)

'''

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows = len(image)
        cols = len(image[0])
        visited = set()

        def dfs(sr: int, sc: int) -> None:
            temp = image[sr][sc]
            image[sr][sc] = color
            visited.add((sr, sc))

            for dr, dc in dirs:
                nr, nc = sr + dr, sc + dc
                if (0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == temp and (nr, nc) not in visited):
                    dfs(nr, nc)

        dfs(sr, sc)
        return image


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1
        {
            "image": [[1, 1, 1], [1, 1, 0], [1, 0, 1]],
            "sr": 1,
            "sc": 1,
            "color": 2,
            "expected": [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
        },

        # Example 2
        {
            "image": [[0, 0, 0], [0, 0, 0]],
            "sr": 0,
            "sc": 0,
            "color": 0,
            "expected": [[0, 0, 0], [0, 0, 0]]
        },

        # Single cell matrix
        {
            "image": [[5]],
            "sr": 0,
            "sc": 0,
            "color": 9,
            "expected": [[9]]
        },

        # Single row
        {
            "image": [[1, 1, 1, 2, 2]],
            "sr": 0,
            "sc": 1,
            "color": 3,
            "expected": [[3, 3, 3, 2, 2]]
        },

        # Single column
        {
            "image": [[1], [1], [0], [1]],
            "sr": 0,
            "sc": 0,
            "color": 2,
            "expected": [[2], [2], [0], [1]]
        },

        # Diagonal should NOT be filled
        {
            "image": [
                [1, 0, 1],
                [0, 1, 0],
                [1, 0, 1]
            ],
            "sr": 1,
            "sc": 1,
            "color": 2,
            "expected": [
                [1, 0, 1],
                [0, 2, 0],
                [1, 0, 1]
            ]
        },

        # Entire matrix fill
        {
            "image": [
                [7, 7, 7],
                [7, 7, 7]
            ],
            "sr": 0,
            "sc": 0,
            "color": 1,
            "expected": [
                [1, 1, 1],
                [1, 1, 1]
            ]
        },

        # Starting point surrounded by different colors
        {
            "image": [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ],
            "sr": 1,
            "sc": 1,
            "color": 0,
            "expected": [
                [1, 2, 3],
                [4, 0, 6],
                [7, 8, 9]
            ]
        },

        # Complex connected component
        {
            "image": [
                [1, 1, 0, 0],
                [1, 0, 0, 1],
                [0, 0, 1, 1],
                [1, 1, 1, 0]
            ],
            "sr": 0,
            "sc": 0,
            "color": 9,
            "expected": [
                [9, 9, 0, 0],
                [9, 0, 0, 1],
                [0, 0, 1, 1],
                [1, 1, 1, 0]
            ]
        }
    ]

    for idx, test in enumerate(test_cases, 1):
        result = solution.floodFill(
            image=[row[:] for row in test["image"]],  # deep copy
            sr=test["sr"],
            sc=test["sc"],
            color=test["color"]
        )

        print(f"Test Case {idx}")
        print("Input Image:")
        for row in test["image"]:
            print(row)

        print(f"sr={test['sr']}, sc={test['sc']}, color={test['color']}")

        print("Expected:")
        for row in test["expected"]:
            print(row)

        print("Your Output:")
        for row in result:
            print(row)

        print("PASS" if result == test["expected"] else "FAIL")
        print("-" * 50)