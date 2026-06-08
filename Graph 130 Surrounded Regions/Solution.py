'''
### Key Observation

An 'O' should not be flipped if it is connected (directly or indirectly) to a border 'O'.
So instead of finding regions that are surrounded, it's easier to:
1. Start from all border 'O' cells.
2. Mark every 'O' reachable from the border as safe.
3. Any remaining 'O' must be surrounded and should be flipped to 'X'.

## Example

Input:
	X X X X
	X O O X
	X X O X
	X O X X
The bottom 'O' is connected to the border, so it stays.

After marking border-connected cells:
	X X X X
	X O O X
	X X O X
	X S X X
(S = safe)

Now flip all remaining 'O':
	X X X X
	X X X X
	X X X X
	X O X X

## BFS Solution

### Algorithm
1. Put every border 'O' into a queue.
2. BFS from them and mark visited cells as safe ('S').
3. Traverse the board:
   * 'O' → 'X'
   * 'S' → 'O'

### Code
	USED IN FUNCTION

## DFS Solution
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != "O"
            ):
                return

            board[r][c] = "S"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Start DFS from border O's
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][cols - 1] == "O":
                dfs(r, cols - 1)

        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)

        # Flip cells
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"

## Complexity Analysis

* Time: O(mn)
  * Every cell is processed at most once.

* Space (BFS): O(mn)
  * Queue may contain all cells.
* Space (DFS): O(mn)
  * Recursive call stack in the worst case.

### Interview Insight

The trick is to think in reverse:
* Don't search for surrounded regions.
* Search for regions that cannot be surrounded (those touching the border).
* Protect them first, then flip everything else. This turns a difficult region-validation problem into a straightforward flood-fill from the boundary.

'''
from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        queue = deque()

        # Add all border O's
        for r in range(rows):
            for c in range(cols):
                if (
                    r == 0 or
                    r == rows - 1 or
                    c == 0 or
                    c == cols - 1
                ) and board[r][c] == "O":
                    queue.append((r, c))
                    board[r][c] = "S"

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Mark all border-connected O's as safe
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    board[nr][nc] == "O"
                ):
                    board[nr][nc] = "S"
                    queue.append((nr, nc))

        # Flip surrounded regions
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1
        (
            [
                ["X", "X", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "O", "X"],
                ["X", "O", "X", "X"]
            ],
            [
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "O", "X", "X"]
            ]
        ),

        # Example 2
        (
            [["X"]],
            [["X"]]
        ),

        # Single O
        (
            [["O"]],
            [["O"]]
        ),

        # All X
        (
            [
                ["X", "X"],
                ["X", "X"]
            ],
            [
                ["X", "X"],
                ["X", "X"]
            ]
        ),

        # All O (all connected to border)
        (
            [
                ["O", "O", "O"],
                ["O", "O", "O"],
                ["O", "O", "O"]
            ],
            [
                ["O", "O", "O"],
                ["O", "O", "O"],
                ["O", "O", "O"]
            ]
        ),

        # Single surrounded O
        (
            [
                ["X", "X", "X"],
                ["X", "O", "X"],
                ["X", "X", "X"]
            ],
            [
                ["X", "X", "X"],
                ["X", "X", "X"],
                ["X", "X", "X"]
            ]
        ),

        # Multiple surrounded regions
        (
            [
                ["X", "X", "X", "X", "X"],
                ["X", "O", "X", "O", "X"],
                ["X", "X", "X", "X", "X"],
                ["X", "O", "X", "O", "X"],
                ["X", "X", "X", "X", "X"]
            ],
            [
                ["X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X"]
            ]
        ),

        # Border-connected chain protects interior O's
        (
            [
                ["X", "O", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "O", "X"],
                ["X", "X", "X", "X"]
            ],
            [
                ["X", "O", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "O", "X"],
                ["X", "X", "X", "X"]
            ]
        ),

        # Only corner O's
        (
            [
                ["O", "X", "O"],
                ["X", "X", "X"],
                ["O", "X", "O"]
            ],
            [
                ["O", "X", "O"],
                ["X", "X", "X"],
                ["O", "X", "O"]
            ]
        ),

        # Large enclosed region
        (
            [
                ["X", "X", "X", "X", "X"],
                ["X", "O", "O", "O", "X"],
                ["X", "O", "O", "O", "X"],
                ["X", "O", "O", "O", "X"],
                ["X", "X", "X", "X", "X"]
            ],
            [
                ["X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X"]
            ]
        ),

        # Narrow board (1 row)
        (
            [["O", "X", "O", "O", "X"]],
            [["O", "X", "O", "O", "X"]]
        ),

        # Narrow board (1 column)
        (
            [
                ["O"],
                ["X"],
                ["O"],
                ["O"],
                ["X"]
            ],
            [
                ["O"],
                ["X"],
                ["O"],
                ["O"],
                ["X"]
            ]
        ),
    ]

    for i, (board, expected) in enumerate(test_cases, start=1):
        solution.solve(board)  # modifies board in-place

        print(f"Test Case {i}")
        print("Output  :", board)
        print("Expected:", expected)
        print("PASS" if board == expected else "FAIL")
        print("-" * 60)