'''

The key observation is:
> For any path from (0, 0) to (n-1, n-1), the required water level is the maximum elevation on that path.
So we want a path that minimizes its maximum cell value.

This is a classic Dijkstra problem.

Idea
In normal Dijkstra:
	distance[next] = distance[current] + edge_weight

Here, reaching a cell through current requires the water level to be high enough for both:
* the water level needed to reach current
* the elevation of next

Therefore:
	new_time = max(time, grid[nr][nc])

We always process the cell requiring the smallest water level first.

####################################################################################################

Let's understand new_time

Suppose we're currently here:
	grid[current] = 5
	time = 8

This means the path we've taken so far has required water level 8.

Now the neighboring cell has elevation:
	grid[next] = 12

We cannot enter it until water reaches 12.

So:
	new_time = max(8, 12)
			 = 12

If instead:
	grid[next] = 6

then:
	new_time = max(8, 6)
			 = 8

The path still only requires water level 8.

####################################################################################################
Example

0  2
1  3

Possible path:			0 → 2 → 3
Maximum elevation:		max(0, 2, 3) = 3
Other path:				0 → 1 → 3
Maximum elevation:		max(0, 1, 3) = 3

Answer = 3.

The heap stores:		(required_water, row, col)

So it might look like:

	(0, 0, 0)
	(1, 1, 0)
	(2, 0, 1)
	(3, 1, 1)

We always expand the cell with the smallest required water level.

####################################################################################################

Why is this Dijkstra?

Think of each cell as a vertex.

Instead of minimizing:
	sum of edge weights

we are minimizing:
	maximum value encountered along the path

The relaxation becomes:
	new_distance = max(current_distance, grid[nr][nc])

And the same Dijkstra principle applies:
> When we pop a cell with the smallest value from the min-heap, we've found the minimum possible required water level for that cell.

####################################################################################################

Complexity

There are n² cells and each cell has at most 4 neighbors.
Each heap operation costs O(log(n²)) = O(log n).

Therefore:
	Time:  O(n² log n)
	Space: O(n²)

The most important thing to remember for this problem is simply:
	# Normal Dijkstra
	new_dist = dist + weight

	# Swim in Rising Water
	new_dist = max(dist, grid[nr][nc])

That's the entire conceptual twist.
'''

import heapq

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while heap:
            time, r, c = heapq.heappop(heap)

            if (r, c) in visited:
                continue

            visited.add((r, c))

            if r == n - 1 and c == n - 1:
                return time

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited):
                    new_time = max(time, grid[nr][nc])
                    heapq.heappush(heap, (new_time, nr, nc))

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1
        (
            [[0, 2],
             [1, 3]],
            3
        ),

        # Example 2
        (
            [[0, 1, 2, 3, 4],
             [24, 23, 22, 21, 5],
             [12, 13, 14, 15, 16],
             [11, 17, 18, 19, 20],
             [10, 9, 8, 7, 6]],
            16
        ),

        # Edge Case 1: 1x1 grid
        (
            [[0]],
            0
        ),

        # Edge Case 2: 1x1 grid with non-zero elevation
        (
            [[7]],
            7
        ),

        # Edge Case 3: Simple 2x2, direct path has lower maximum
        (
            [[0, 1],
             [2, 3]],
            3
        ),

        # Edge Case 4: Need to take a less obvious path
        (
            [[0, 100, 2],
             [1, 3, 4],
             [2, 5, 6]],
            6
        ),

        # Edge Case 5: Start has the highest elevation
        (
            [[8, 1, 2],
             [7, 6, 3],
             [5, 4, 0]],
            8
        ),

        # Edge Case 6: End has the highest elevation
        (
            [[0, 1, 2],
             [5, 4, 3],
             [6, 7, 8]],
            8
        ),

        # Edge Case 7: Best path requires going around a high cell
        (
            [[0, 99, 98, 97],
             [1, 2, 3, 96],
             [6, 5, 4, 95],
             [7, 8, 9, 10]],
            10
        ),

        # Edge Case 8: Zig-zag path
        (
            [[0, 1, 8, 9],
             [3, 2, 7, 10],
             [4, 5, 6, 11],
             [15, 14, 13, 12]],
            12
        ),

        # Edge Case 9: 3x3 where the obvious-looking route is blocked
        (
            [[0, 8, 7],
             [1, 9, 6],
             [2, 3, 5]],
            5
        ),
    ]

    for i, (grid, expected) in enumerate(test_cases, 1):
        result = solution.swimInWater(grid)

        print(f"Test Case {i}:")
        print(f"Result:   {result}")
        print(f"Expected: {expected}")
        print(f"PASS: {result == expected}")
        print("-" * 40)