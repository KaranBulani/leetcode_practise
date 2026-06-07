'''
## 1. Understand the Problem

We have a grid of heights.
Water can flow from a cell to a neighboring cell if: neighbor_height <= current_height
because water flows downhill (or equal height).

A cell is valid if water can reach:
* Pacific Ocean (top row OR left column)
* Atlantic Ocean (bottom row OR right column)
Return all such cells.
####################################################################################################
## 2. Brute Force Idea

For every cell:
1. Run DFS/BFS
2. Check if Pacific can be reached.
3. Check if Atlantic can be reached.
	for every cell:
		dfs(cell)

### Complexity
For each cell: O(rows * cols) work.
Total: O((rows * cols)^2)
Too slow.
####################################################################################################
# 3. Key Observation

Instead of asking:
> Can water flow FROM this cell TO ocean?

Ask the reverse:
> Starting from ocean, which cells can flow INTO me?
This is much easier.

Suppose we're at Pacific Ocean.
If water normally flows: high -> low
Then when traversing backwards we move: low -> high

So from a cell we can visit a neighbor only if: neighbor_height >= current_height
because we're reversing the flow.

Example:
1 2 3

Water normally: 3 -> 2 -> 1
Reverse search: 1 -> 2 -> 3
####################################################################################################
# 4. Main Idea

Perform two traversals.

### Pacific Traversal
Start from:
	top row
	left column

Find all cells reachable.
Store in: pacific

### Atlantic Traversal

Start from:
	bottom row
	right column

Find all cells reachable.
Store in: atlantic

Any cell present in both sets can reach both oceans.
answer = pacific & atlantic
####################################################################################################
# 5. DFS Solution

## Data Structures
	pacific = set()
	atlantic = set()


Each stores: (row, col)
reachable from that ocean.

## DFS Rule

From current cell: (r, c)
visit neighbor: (nr, nc)
only if: heights[nr][nc] >= heights[r][c]
because we're traversing opposite to water flow.
####################################################################################################
# 6. Dry Run

Grid:
	1 2 2
	3 2 3
	2 4 5

Pacific DFS starts from:
	top row
	left column
and spreads to higher/equal cells.

Pacific set might become:
	{
	(0,0),
	(0,1),
	(0,2),
	(1,0),
	...
	}

Atlantic DFS starts from:
	bottom row
	right column
and spreads similarly.

Intersection: pacific & atlantic
gives cells reaching both oceans.
####################################################################################################
# 7. Code (DFS)

from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            visited.add((r, c))

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols or
                    (nr, nc) in visited or
                    heights[nr][nc] < heights[r][c]
                ):
                    continue

                dfs(nr, nc, visited)

        # Pacific (top row)
        for c in range(cols):
            dfs(0, c, pacific)
        # Pacific (left column)
        for r in range(rows):
            dfs(r, 0, pacific)

        # Atlantic (bottom row)
        for c in range(cols):
            dfs(rows - 1, c, atlantic)
        # Atlantic (right column)
        for r in range(rows):
            dfs(r, cols - 1, atlantic)

        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result
####################################################################################################
# 9. Complexity Analysis

Let:
	m = rows
	n = cols

### Time

Each cell can be visited at most once in:
* Pacific traversal
* Atlantic traversal

So:
	O(m*n) + O(m*n)
	= O(m*n)

### Space

Visited sets: O(m*n)
Recursion stack (DFS worst case): O(m*n)
Total: O(m*n)

####################################################################################################
## BFS Approach

The idea is exactly the same as DFS:
* Start BFS from all Pacific border cells simultaneously.
* Start BFS from all Atlantic border cells simultaneously.
* Build two reachable sets.
* Return cells present in both sets.

## Why Multi-Source BFS?

Instead of running BFS from every cell: Cell -> Ocean
we reverse the flow: Ocean -> Cells
and start from all ocean-border cells at once.
For reverse traversal: heights[nr][nc] >= heights[r][c]
because water could have flowed from that higher/equal neighbor into the current cell.

## Algorithm

### Pacific BFS Sources
	Top Row
	Left Column
### Atlantic BFS Sources
	Bottom Row
	Right Column

Run BFS from each ocean and record reachable cells.
Finally: pacific & atlantic
contains cells that can reach both oceans.

## Complexity Analysis
Let:
	m = rows
	n = cols

### Time
Each cell enters the Pacific BFS at most once: O(m*n)
Each cell enters the Atlantic BFS at most once: O(m*n)
Total: O(m*n)

### Space
Visited sets: O(m*n)
Queues: O(m*n)
Total: O(m*n)

'''
from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacificSet = set()
        atlanticSet = set()
        pacificQueue = deque()
        atlanticQueue = deque()

        # Top and Bottom rows
        for c in range(cols):
            pacificSet.add((0, c))
            pacificQueue.append((0, c))

            atlanticSet.add((rows - 1, c))
            atlanticQueue.append((rows - 1, c))

        # Left and Right columns
        for r in range(rows):
            pacificSet.add((r, 0))
            pacificQueue.append((r, 0))

            atlanticSet.add((r, cols - 1))
            atlanticQueue.append((r, cols - 1))

        def bfs(queue, visited):
            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (
                        nr < 0 or nr >= rows or
                        nc < 0 or nc >= cols or
                        (nr, nc) in visited or
                        heights[nr][nc] < heights[r][c]
                    ):
                        continue
                    visited.add((nr, nc))
                    queue.append((nr, nc))

        bfs(pacificQueue, pacificSet)
        bfs(atlanticQueue, atlanticSet)

        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacificSet and (r, c) in atlanticSet:
                    result.append([r, c])
        return result

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1
        (
            [
                [1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4]
            ],
            [
                [0, 4],
                [1, 3],
                [1, 4],
                [2, 2],
                [3, 0],
                [3, 1],
                [4, 0]
            ]
        ),

        # Example 2
        (
            [[1]],
            [[0, 0]]
        ),

        # Single row
        (
            [[1, 2, 3, 4, 5]],
            [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]
        ),

        # Single column
        (
            [
                [1],
                [2],
                [3],
                [4],
                [5]
            ],
            [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]
        ),

        # All same height
        (
            [
                [1, 1],
                [1, 1]
            ],
            [[0, 0], [0, 1], [1, 0], [1, 1]]
        ),

        # Strictly increasing toward bottom-right
        (
            [
                [1, 2],
                [3, 4]
            ],
            [[0, 1], [1, 0], [1, 1]]
        ),

        # Strictly decreasing toward bottom-right
        (
            [
                [4, 3],
                [2, 1]
            ],
            [[0, 0], [0, 1], [1, 0]]
        ),

        # Center peak
        (
            [
                [1, 1, 1],
                [1, 10, 1],
                [1, 1, 1]
            ],
            [[0, 2], [1, 1], [2, 0]]
        ),

        # Basin in middle
        (
            [
                [5, 5, 5],
                [5, 1, 5],
                [5, 5, 5]
            ],
            [
                [0, 0], [0, 1], [0, 2],
                [1, 0], [1, 2],
                [2, 0], [2, 1], [2, 2]
            ]
        ),
    ]

    for idx, (heights, expected) in enumerate(test_cases, start=1):
        result = solution.pacificAtlantic(heights)

        # Sort because order is not guaranteed
        result = sorted(result)
        expected = sorted(expected)

        print(f"Test Case {idx}: {'PASS' if result == expected else 'FAIL'}")

        if result != expected:
            print(f"Expected: {expected}")
            print(f"Got     : {result}")

        print("-" * 60)