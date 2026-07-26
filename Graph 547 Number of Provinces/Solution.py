'''
# Intuition
You're given an n x n adjacency matrix.
* isConnected[i][j] == 1 means city i and city j are directly connected.
* If A is connected to B, and B to C, then A, B, C all belong to the same province.

So the problem simply asks:
> How many connected components are there?
Union Find is perfect because every edge merges two components.

# Example
isConnected =
[
 [1,1,0],
 [1,1,0],
 [0,0,1]
]

Initially every city is its own parent.
				0   1   2
				  parent
				0   1   2
Number of provinces = 3

####################################################################################################
# Process matrix.
		 (0,1)
		0 ---- 1

Union them.
		 parent
		0   0   2

Now provinces = 2

Remaining entries don't change anything.

Final answer
	{0,1}
	{2}

Answer = 2

####################################################################################################
# Union Find Operations

## Find
	def find(x):
		if parent[x] != x:
			parent[x] = find(parent[x])
		return parent[x]

Uses path compression.

## Union
If roots are different, merge them.

	rootX = find(x)
	rootY = find(y)
	if rootX != rootY:
		parent[rootY] = rootX

Each successful union decreases the number of provinces by 1.

# Algorithm

	provinces = n

	for every pair (i,j):
		if connected:
			union(i,j)

	return provinces

Since the graph is undirected, we only need to scan the upper triangle (j > i).

####################################################################################################
# Dry Run

[
 [1,1,0],
 [1,1,1],
 [0,1,1]
]

Initially
	0
	1
	2
Count = 3

(0,1)
Merge
	0
	|
	1

	2
Count = 2

(1,2)
Find(1) → 0
Merge 2 into 0
		  0
		 / \
		1   2
Count = 1
Answer = 1

####################################################################################################
# Complexity Analysis

Let n be the number of cities.

* We inspect every entry in the upper triangle of the matrix: O(n²).
* Each find/union operation is amortized O(α(n)), where α is the inverse Ackermann function (effectively constant).

Therefore:
* Time Complexity: O(n² · α(n)) ≈ O(n²)
* Space Complexity: O(n) for the parent and rank arrays.

####################################################################################################
# Alternative Solution: DFS/BFS

You can also solve this by treating the matrix as a graph and counting connected components using DFS or BFS.

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n

        def dfs(city):
            visited[city] = True
            for nei in range(n):
                if isConnected[city][nei] == 1 and not visited[nei]:
                    dfs(nei)

        provinces = 0

        for city in range(n):
            if not visited[city]:
                provinces += 1
                dfs(city)

        return provinces


This also runs in:
* Time: O(n²)
* Space: O(n) (excluding recursion stack, which can be up to O(n) in the worst case).

'''
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        parent = list(range(n))
        rank = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        provinces = n

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 0:
                    continue

                root1 = find(i)
                root2 = find(j)

                if root1 == root2:
                    continue

                if rank[root1] < rank[root2]:
                    root1, root2 = root2, root1

                parent[root2] = root1

                if rank[root1] == rank[root2]:
                    rank[root1] += 1

                provinces -= 1

        return provinces

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1
        (
            [
                [1, 1, 0],
                [1, 1, 0],
                [0, 0, 1]
            ],
            2
        ),

        # Example 2
        (
            [
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]
            ],
            3
        ),

        # Single city
        (
            [
                [1]
            ],
            1
        ),

        # Two connected cities
        (
            [
                [1, 1],
                [1, 1]
            ],
            1
        ),

        # Two disconnected cities
        (
            [
                [1, 0],
                [0, 1]
            ],
            2
        ),

        # All cities connected
        (
            [
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]
            ],
            1
        ),

        # Chain connection (indirect connectivity)
        (
            [
                [1, 1, 0, 0],
                [1, 1, 1, 0],
                [0, 1, 1, 1],
                [0, 0, 1, 1]
            ],
            1
        ),

        # Two separate provinces
        (
            [
                [1, 1, 0, 0],
                [1, 1, 0, 0],
                [0, 0, 1, 1],
                [0, 0, 1, 1]
            ],
            2
        ),

        # Three provinces
        (
            [
                [1, 1, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 1, 1],
                [0, 0, 0, 1, 1]
            ],
            3
        ),

        # Star graph (all connected through city 0)
        (
            [
                [1, 1, 1, 1, 1],
                [1, 1, 0, 0, 0],
                [1, 0, 1, 0, 0],
                [1, 0, 0, 1, 0],
                [1, 0, 0, 0, 1]
            ],
            1
        ),

        # Larger mixed example
        (
            [
                [1, 0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 1, 0],
                [0, 0, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 1]
            ],
            4
        ),
    ]

    for i, (isConnected, expected) in enumerate(test_cases, 1):
        result = solution.findCircleNum(isConnected)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {i}: {status}")
        print(f"Expected: {expected}")
        print(f"Got:      {result}")
        print("-" * 40)