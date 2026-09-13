'''
The key observation is:
> Being at (r, c) is not enough information to determine the future cost, because the number of turns used depends on the previous direction.

So our Dijkstra state needs:
	(row, col, previous_direction, turns_used)

####################################################################################################

State

Let:
	dist[r][c][d][t] = minimum cost to reach (r, c) where:
	* d = direction of the last move
	* t = number of turns used

We start with no previous direction, so the first move never counts as a turn.

####################################################################################################

Transition

Suppose we're currently moving in direction d, and want to move in direction nd.

new_turns = turns + (d != nd)

We only continue if new_turns <= k

Since all cell costs are non-negative, Dijkstra applies.


####################################################################################################

Why do we need the direction in the state?

Consider:
		A → B → C

When we're at C, our previous direction is right.

Now suppose we move down:
		A → B → C
				  ↓
That's a turn.

But if we arrived at C from above:
	A
	↓
	B
	↓
	C
then moving down again is not a turn.

So these two states:
	(C, previous_direction=right)
	(C, previous_direction=down)
cannot be merged even though we're physically at the same cell.

That's exactly why the state has to include previous_direction.

####################################################################################################

One subtle point: revisiting cells

Unlike a normal shortest-path problem, we cannot simply say "I've already visited (r,c), so don't visit it again."

A cell can be reached with different:

* previous directions
* numbers of turns

For example:
	(r, c, right, 1)
	(r, c, down, 1)
	(r, c, right, 2)
are different states.

That's why dist has four dimensions.

####################################################################################################

Complexity

There are at most:
	m × n × 4 × (k + 1)
states.

Each state has at most 4 outgoing edges.

Therefore:
	V = O(mn k)
	E = O(mn k)

Dijkstra using a heap takes:
				O(E log V) = O(mn k log(mn k))

Space:	O(mn k)
With m,n <= 75, this is manageable.

####################################################################################################

One cleaner way to think about it

We're essentially converting the original grid into a new graph:
(r, c)

becomes
(r, c, previous_direction, turns_used)

Then every legal movement is just a normal weighted edge, where:
	edge_cost = grid[new_r][new_c]

and changing direction consumes one unit of the turn budget.

So Dijkstra itself hasn't really changed. We've just expanded what constitutes a "node" so that the state contains all information necessary to make future decisions.
'''
import heapq

class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        # 1x1 grid
        if m == 1 and n == 1:
            return grid[0][0]

        # directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        INF = float("inf")

        # dist[r][c][direction][turns]
        dist = [
            [
                [[INF] * (k + 1) for _ in range(4)]
                for _ in range(n)
            ]
            for _ in range(m)
        ]

        heap = []

        # Special case: first move has no previous direction.
        # We simply try all possible first moves.
        for d, (dr, dc) in enumerate(directions):
            nr, nc = dr, dc

            if 0 <= nr < m and 0 <= nc < n:
                cost = grid[0][0] + grid[nr][nc]

                dist[nr][nc][d][0] = cost
                heapq.heappush(heap, (cost, nr, nc, d, 0))

        while heap:
            cost, r, c, prev_dir, turns = heapq.heappop(heap)

            # Ignore stale heap entry
            if cost != dist[r][c][prev_dir][turns]:
                continue

            # We can stop as soon as destination is popped.
            # Dijkstra guarantees this is globally minimum.
            if r == m - 1 and c == n - 1:
                return cost

            for new_dir, (dr, dc) in enumerate(directions):
                nr = r + dr
                nc = c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                # Direction changed -> one additional turn
                new_turns = turns + (prev_dir != new_dir)

                if new_turns > k:
                    continue

                new_cost = cost + grid[nr][nc]

                if new_cost < dist[nr][nc][new_dir][new_turns]:
                    dist[nr][nc][new_dir][new_turns] = new_cost

                    heapq.heappush(
                        heap,
                        (new_cost, nr, nc, new_dir, new_turns)
                    )

        return -1

if __name__ == "__main__":
    solution = Solution()

    # ============================================================
    # Example 1
    # Expected: 12
    # ============================================================
    grid = [
        [2, 7, 3],
        [1, 4, 5]
    ]
    k = 1

    result = solution.minCost(grid, k)
    print("Example 1:", result, "Expected:", 12)


    # ============================================================
    # Example 2
    # Expected: 20
    # ============================================================
    grid = [
        [4, 1, 9],
        [3, 2, 5],
        [4, 8, 6]
    ]
    k = 2

    result = solution.minCost(grid, k)
    print("Example 2:", result, "Expected:", 20)


    # ============================================================
    # Example 3
    # Expected: -1
    # ============================================================
    grid = [
        [1, 9],
        [3, 4]
    ]
    k = 0

    result = solution.minCost(grid, k)
    print("Example 3:", result, "Expected:", -1)


    # ============================================================
    # Edge Case 1: Single cell
    # No moves, therefore no turns.
    # Expected: 5
    # ============================================================
    grid = [
        [5]
    ]
    k = 0

    result = solution.minCost(grid, k)
    print("Edge Case 1:", result, "Expected:", 5)


    # ============================================================
    # Edge Case 2: Single row
    # Only one possible direction, so 0 turns.
    # Expected: 10
    # ============================================================
    grid = [
        [1, 2, 3, 4]
    ]
    k = 0

    result = solution.minCost(grid, k)
    print("Edge Case 2:", result, "Expected:", 10)


    # ============================================================
    # Edge Case 3: Single column
    # Only one possible direction, so 0 turns.
    # Expected: 10
    # ============================================================
    grid = [
        [1],
        [2],
        [3],
        [4]
    ]
    k = 0

    result = solution.minCost(grid, k)
    print("Edge Case 3:", result, "Expected:", 10)


    # ============================================================
    # Edge Case 4: 2x2 with k = 0
    # Any path from start to end requires a direction change.
    # Expected: -1
    # ============================================================
    grid = [
        [1, 2],
        [3, 4]
    ]
    k = 0

    result = solution.minCost(grid, k)
    print("Edge Case 4:", result, "Expected:", -1)


    # ============================================================
    # Edge Case 5: 2x2 with k = 1
    # Two possible paths:
    # Right -> Down
    # Down -> Right
    # Expected: 7
    # ============================================================
    grid = [
        [1, 2],
        [3, 4]
    ]
    k = 1

    result = solution.minCost(grid, k)
    print("Edge Case 5:", result, "Expected:", 7)


    # ============================================================
    # Edge Case 6: Zero-cost cells
    # Expected: 0
    # ============================================================
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    k = 2

    result = solution.minCost(grid, k)
    print("Edge Case 6:", result, "Expected:", 0)


    # ============================================================
    # Edge Case 7: Large values
    # Straight path is possible with 1 turn.
    # Expected: 4000
    # ============================================================
    grid = [
        [1000, 1000],
        [1000, 1000]
    ]
    k = 1

    result = solution.minCost(grid, k)
    print("Edge Case 7:", result, "Expected:", 3000)


    # ============================================================
    # Edge Case 8: Need exactly 2 direction changes, but k = 1
    #
    # 1  1  1
    # 1 100 1
    # 1 100 1
    #
    # A path with <= 1 turn can still take the top/right route.
    # Expected: 5
    # ============================================================
    grid = [
        [1, 1, 1],
        [1, 100, 1],
        [1, 100, 1]
    ]
    k = 1

    result = solution.minCost(grid, k)
    print("Edge Case 8:", result, "Expected:", 5)


    # ============================================================
    # Edge Case 9: More turns allow a cheaper path
    #
    # k = 1:
    #   Right -> Right -> Down -> Down
    #
    # Expected: 5
    # ============================================================
    grid = [
        [1, 1, 1],
        [100, 100, 1],
        [100, 100, 1]
    ]
    k = 1

    result = solution.minCost(grid, k)
    print("Edge Case 9:", result, "Expected:", 5)


    # ============================================================
    # Edge Case 10: k is larger, but minimum-cost path uses fewer
    # turns. "At most k" is important here.
    # Expected: 5
    # ============================================================
    grid = [
        [1, 1, 1],
        [1, 100, 1],
        [1, 1, 1]
    ]
    k = 2

    result = solution.minCost(grid, k)
    print("Edge Case 10:", result, "Expected:", 5)


    # ============================================================
    # Edge Case 11: 3x3, k = 0
    # Impossible because reaching bottom-right requires both
    # horizontal and vertical movement.
    # Expected: -1
    # ============================================================
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    k = 0

    result = solution.minCost(grid, k)
    print("Edge Case 11:", result, "Expected:", -1)


    # ============================================================
    # Edge Case 12: Direction changes can involve backtracking.
    #
    # This checks that the solution doesn't incorrectly assume
    # that an optimal path must be monotonic.
    #
    # Expected: 5
    # ============================================================
    grid = [
        [1, 100, 1],
        [1, 100, 1],
        [1, 1, 1]
    ]
    k = 2

    result = solution.minCost(grid, k)
    print("Edge Case 12:", result, "Expected:", 5)