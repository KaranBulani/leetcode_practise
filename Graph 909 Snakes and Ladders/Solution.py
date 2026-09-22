'''

The key idea is to treat the board as a graph:

* Each square 1 ... n² is a node.
* From square curr, you can move to curr + 1 ... curr + 6.
* If the destination has a snake/ladder, you must move to its destination.
* Every move costs 1, so this is a BFS shortest-path problem.

####################################################################################################

1. Convert square number → (row, col)

The board is numbered in Boustrophedon order:

	For n = 6:

	36 35 34 33 32 31
	25 26 27 28 29 30
	24 23 22 21 20 19
	13 14 15 16 17 18
	12 11 10  9  8  7
	 1  2  3  4  5  6

Notice that square 1 is at:		board[n - 1][0]

For a square s:
	row_from_bottom = (s - 1) // n
	col = (s - 1) % n

The actual matrix row is:
	row = n - 1 - row_from_bottom

The column depends on whether that row is traversed left-to-right or right-to-left:
	if row_from_bottom % 2 == 0:
		col = (s - 1) % n
	else:
		col = n - 1 - (s - 1) % n

####################################################################################################

Why BFS?

Suppose you're at square 1:
	1
	├── 2
	├── 3
	├── 4
	├── 5
	├── 6
	└── 7

All of these require 1 dice roll.

From each of them, their reachable squares require 2 rolls.

So BFS naturally explores:

	0 rolls: 1

	1 roll:  2 3 4 5 6 7

	2 rolls: all squares reachable from those

	3 rolls: ...

The first time we reach n², we've found the minimum number of rolls.

####################################################################################################

Important detail: snake/ladder is not another move

This is the part that is easy to get wrong.

Suppose:
	curr = 5
	dice = 3
	next_square = 8

and:
	board[...][...] = 15

Then:
	5 --dice 3--> 8 --ladder--> 15

This entire thing costs one dice roll, not two.

That's why we do:
	destination = board[row][col]

	if destination != -1:
		next_square = destination


before adding the square to the BFS queue.

####################################################################################################

Complexity

There are at most n² squares, and each square examines at most 6 dice outcomes.

Therefore:
	Time:  O(n²)
	Space: O(n²)

The visited set is important because snakes/ladders can create cycles, so without it we could repeatedly revisit the same squares.

'''
from collections import deque

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        target = n * n

        def get_coordinates(square: int) -> tuple[int, int]:
            row_from_bottom = (square - 1) // n
            col = (square - 1) % n

            row = n - 1 - row_from_bottom

            if row_from_bottom % 2 == 1:
                col = n - 1 - col

            return row, col

        queue = deque([(1, 0)])
        visited = {1}

        while queue:
            curr, moves = queue.popleft()

            if curr == target:
                return moves

            for next_square in range(curr + 1, min(curr + 6, target) + 1):
                row, col = get_coordinates(next_square)

                destination = board[row][col]

                if destination != -1:
                    next_square = destination

                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))

        return -1

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # ============================================================
        # 1. Official Example 1
        # ============================================================
        (
            [
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, 35, -1, -1, 13, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, 15, -1, -1, -1, -1],
            ],
            4,
            "Official Example 1"
        ),

        # ============================================================
        # 2. Official Example 2
        # ============================================================
        (
            [
                [-1, -1],
                [-1, 3],
            ],
            1,
            "Official Example 2"
        ),

        # ============================================================
        # 3. Smallest possible board, no snakes/ladders
        #    1 -> 2
        # ============================================================
        (
            [
                [-1, -1],
                [-1, -1],
            ],
            1,
            "2x2 board, no jumps"
        ),

        # ============================================================
        # 4. 3x3 board, no snakes/ladders
        #    1 -> 7 -> 9
        # ============================================================
        (
            [
                [-1, -1, -1],
                [-1, -1, -1],
                [-1, -1, -1],
            ],
            2,
            "3x3 board, no jumps"
        ),

        # ============================================================
        # 5. 4x4 board, no snakes/ladders
        #    Maximum dice roll can reach 7, then 13, then 16
        # ============================================================
        (
            [
                [-1, -1, -1, -1],
                [-1, -1, -1, -1],
                [-1, -1, -1, -1],
                [-1, -1, -1, -1],
            ],
            3,
            "4x4 board, no jumps"
        ),

        # ============================================================
        # 6. Immediate ladder from square 2 -> 9
        # ============================================================
        (
            [
                [-1, -1, -1],
                [-1, -1, -1],
                [-1, 8, -1],
            ],
            2,
            "Immediate ladder"
        ),

        # ============================================================
        # 7. Ladder directly to final square
        #    2 -> 9
        # ============================================================
        (
            [
                [-1, -1, -1],
                [-1, -1, -1],
                [-1, 9, -1],
            ],
            1,
            "Ladder directly to destination"
        ),

        # ============================================================
        # 8. Snake sends you backwards
        # ============================================================
        (
            [
                [-1, -1, -1],
                [-1, -1, 2],
                [-1, -1, -1],
            ],
            2,
            "Snake sends player backwards"
        ),

        # ============================================================
        # 9. Ladder + snake
        # ============================================================
        (
            [
                [-1, -1, -1],
                [-1, -1, 7],
                [-1, 9, -1],
            ],
            1,
            "Jump near beginning"
        ),

        # ============================================================
        # 10. Multiple ladders
        # ============================================================
        (
            [
                [-1, -1, -1, -1],
                [-1, -1, -1, -1],
                [-1, -1, -1, -1],
                [-1, 16, 10, -1],
            ],
            2,
            "Multiple ladders"
        ),

        # ============================================================
        # 11. Snake/ladder chain must NOT be followed twice
        #
        # Square 2 -> 3
        # Square 3 -> 16
        #
        # Landing on 2 should result in 3, NOT 16.
        # ============================================================
        (
            [
                [-1, -1, -1, -1],
                [-1, -1, -1, -1],
                [-1, -1, -1, -1],
                [-1, 3, 16, -1],
            ],
            3,
            "Only one snake/ladder per roll"
        ),

        # ============================================================
        # 12. Snake/ladder chain in opposite direction
        #
        # 2 -> 8
        # 8 -> 15
        #
        # Landing on 2 should stop at 8.
        # ============================================================
        (
            [
                [-1, -1, -1, -1],
                [-1, -1, -1, -1],
                [-1, 15, -1, -1],
                [-1, 8, -1, -1],
            ],
            2,
            "Jump chain must stop after one jump"
        ),

        # ============================================================
        # 13. Snake near the end
        # ============================================================
        (
            [
                [-1, -1, -1, -1],
                [-1, -1, -1, 1],
                [-1, -1, -1, -1],
                [-1, -1, -1, -1],
            ],
            3,
            "Snake near destination"
        ),

        # ============================================================
        # 14. Board with many snakes
        # ============================================================
        (
            [
                [-1, -1, -1, -1],
                [1, -1, 2, -1],
                [1, -1, 3, -1],
                [-1, 1, -1, -1],
            ],
            3,
            "Many snakes"
        ),

        # ============================================================
        # 15. Unreachable board
        #
        # Every possible destination from the starting area
        # eventually sends the player back.
        # ============================================================
        (
            [
                [-1, 1],
                [1, 1],
            ],
            -1,
            "Unreachable destination"
        ),

        # ============================================================
        # 16. Self-loop
        #
        # A square points to itself. This should not cause
        # infinite processing.
        # ============================================================
        (
            [
                [-1, -1, -1],
                [-1, 5, -1],
                [-1, -1, -1],
            ],
            2,
            "Self-loop"
        ),

        # ============================================================
        # 17. Ladder requires choosing a specific dice result
        # ============================================================
        (
            [
                [-1, -1, -1, -1],
                [-1, -1, -1, -1],
                [-1, -1, -1, -1],
                [-1, -1, 14, -1],
            ],
            2,
            "Specific dice choice gives ladder"
        ),

        # ============================================================
        # 18. Several jumps but shortest path skips some
        # ============================================================
        (
            [
                [-1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1],
                [-1, 20, -1, 18, -1],
                [-1, 12, -1, -1, -1],
            ],
            3,
            "Multiple possible routes"
        ),

        # ============================================================
        # 19. Large 6x6 board with no jumps
        # ============================================================
        (
            [
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
            ],
            6,
            "6x6 board, no jumps"
        ),

        # ============================================================
        # 20. 20x20 board, no jumps
        # ============================================================
        (
            [[-1] * 20 for _ in range(20)],
            67,
            "20x20 board, no jumps"
        ),
    ]

    for i, (board, expected, description) in enumerate(test_cases, 1):
        result = solution.snakesAndLadders(board)

        status = "PASS" if result == expected else "FAIL"

        print(
            f"Test {i:02d} | "
            f"{status:4} | "
            f"Expected: {expected:2} | "
            f"Got: {result:2} | "
            f"{description}"
        )