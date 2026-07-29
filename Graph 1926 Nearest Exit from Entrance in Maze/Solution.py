'''
1. Intuition

We need to find the minimum number of steps from the entrance to any exit.
Since every move (up, down, left, right) costs exactly 1 step, this is a shortest path in an unweighted graph.
Whenever we need the shortest distance in an unweighted graph, Breadth-First Search (BFS) is the ideal algorithm.

Think of the maze as a graph:
* Every empty cell ('.') is a node.
* You can move to its neighboring empty cells.
* We start BFS from the entrance.
* The first exit we encounter is guaranteed to be the closest one because BFS explores level by level.

####################################################################################################

2. Why BFS?

Suppose the maze is
+ + . +
. . . +
+ + . +

Entrance: (1,1)

BFS expands like this:

Distance 0:
    E

Distance 1:
 Left   Right   Up

Distance 2:
 Continue expanding...

The first boundary cell (excluding the entrance itself) reached by BFS is automatically the nearest exit.
DFS cannot guarantee this because it may explore a long path before a short one.

####################################################################################################

3. Algorithm

1. Put the entrance into a queue with distance 0.
2. Mark it as visited.
3. While queue is not empty:
   * Pop the current cell.
   * Explore four directions.
   * Ignore cells that are:
     * outside the maze,
     * walls ('+'),
     * already visited.
   * If the neighbor is on the boundary, it is an exit.
     * Return distance + 1.
   * Otherwise mark visited and push into queue.
4. If BFS finishes, return -1.

####################################################################################################

4. Dry Run

Maze:
[
["+","+",".","+"],
[".",".",".","+"],
["+","+","+", "."]
]

Entrance = [1,2]

Visualization:
+ + . +
. . E +
+ + + .

Queue: [(1,2,0)]


####################################################################################################

Pop (1,2), distance = 0

Neighbors:
(0,2)
(1,1)

Queue: [(0,2,1), (1,1,1)]

Now examine (0,2):

Top boundary ✔
Not entrance ✔

Return 1

Correct answer.

####################################################################################################

5. Python Solution

####################################################################################################

6. Why Mark Visited Immediately?

Notice:
maze[nr][nc] = '+'
queue.append((nr, nc, dist + 1))

We mark the cell before pushing it into the queue.
Otherwise, another neighboring cell could also enqueue the same location, leading to duplicate work.

####################################################################################################

7. Complexity Analysis

Let:
* m = number of rows
* n = number of columns

Time Complexity
Each cell is visited at most once.
O(m × n)


Space Complexity
In the worst case, the queue stores every empty cell.
O(m × n)
'''
from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])

        queue = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'   # mark visited

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while queue:
            row, col, dist = queue.popleft()

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if (
                    nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols or
                    maze[nr][nc] == '+'
                ):
                    continue

                if nr in (0, rows - 1) or nc in (0, cols - 1):
                    return dist + 1

                maze[nr][nc] = '+'
                queue.append((nr, nc, dist + 1))

        return -1
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # ==========================
        # Examples from question
        # ==========================
        (
            [
                ["+", "+", ".", "+"],
                [".", ".", ".", "+"],
                ["+", "+", "+", "."]
            ],
            [1, 2],
            1
        ),
        (
            [
                ["+", "+", "+"],
                [".", ".", "."],
                ["+", "+", "+"]
            ],
            [1, 0],
            2
        ),
        (
            [
                [".", "+"]
            ],
            [0, 0],
            -1
        ),

        # ==========================
        # Additional Edge Cases
        # ==========================

        # 1. Single cell maze (entrance is only cell)
        (
            [
                ["."]
            ],
            [0, 0],
            -1
        ),

        # 2. 2x2 all open, entrance inside border
        (
            [
                [".", "."],
                [".", "."]
            ],
            [1, 1],
            1
        ),

        # 3. Entrance on border but should NOT count as exit
        (
            [
                [".", ".", "."]
            ],
            [0, 1],
            1
        ),

        # 4. Entrance surrounded by walls
        (
            [
                ["+", "+", "+"],
                ["+", ".", "+"],
                ["+", "+", "+"]
            ],
            [1, 1],
            -1
        ),

        # 5. No possible exit although open cells exist
        (
            [
                ["+", "+", "+", "+"],
                ["+", ".", ".", "+"],
                ["+", ".", ".", "+"],
                ["+", "+", "+", "+"]
            ],
            [1, 1],
            -1
        ),

        # 6. Multiple exits, nearest should be chosen
        (
            [
                [".", ".", "."],
                [".", ".", "."],
                [".", ".", "."]
            ],
            [1, 1],
            1
        ),

        # 7. Longer winding path
        (
            [
                ["+", ".", "+", "+", "+"],
                ["+", ".", ".", ".", "+"],
                ["+", "+", "+", ".", "+"],
                ["+", ".", ".", ".", "."],
                ["+", "+", "+", "+", "+"]
            ],
            [1, 1],
            5
        ),

        # 8. Exit immediately adjacent
        (
            [
                ["+", ".", "+"],
                ["+", ".", "+"],
                ["+", "+", "+"]
            ],
            [1, 1],
            1
        ),

        # 9. Large open area
        (
            [
                [".", ".", ".", ".", "."],
                [".", ".", ".", ".", "."],
                [".", ".", ".", ".", "."],
                [".", ".", ".", ".", "."],
                [".", ".", ".", ".", "."]
            ],
            [2, 2],
            2
        ),

        # 10. Entrance at corner, other border cells reachable
        (
            [
                [".", ".", "."],
                [".", "+", "."],
                [".", ".", "."]
            ],
            [0, 0],
            1
        ),

        # 11. Entrance on border, only entrance is border opening
        (
            [
                [".", "+"],
                ["+", "+"]
            ],
            [0, 0],
            -1
        ),

        # 12. Narrow corridor
        (
            [
                ["+", ".", "+", "+", "+"],
                ["+", ".", ".", ".", "."],
                ["+", "+", "+", "+", "+"]
            ],
            [1, 1],
            3
        ),
    ]

    for i, (maze, entrance, expected) in enumerate(test_cases, 1):
        result = solution.nearestExit([row[:] for row in maze], entrance)
        print(f"Test Case {i}:")
        print(f"Expected: {expected}")
        print(f"Your Output: {result}")
        print(f"PASS: {result == expected}")
        print("-" * 50)