'''
Intuition

The given graph is a tree:
* n cities
* n-1 roads
* Exactly one path between every pair of cities.
We want every city to be able to reach city 0.

Key Observation

	Suppose there is an edge
		a → b

	If during our traversal from city 0 we move
		0 ... a → b
	then this edge is pointing away from city 0.

	To make every node reach 0, this edge must become
		b → a
	So we count one reversal.

	On the other hand, if the original edge is
		b → a
	while traversing
		0 ... a ← b
	then it already points toward city 0, so no reversal is needed.

####################################################################################################

Main Idea

Since the roads are directed, but we need to explore the entire tree, create an undirected graph while remembering the original direction.

For every directed edge
	u → v

store
	u -> (v, 1)
	v -> (u, 0)

where
* 1 means this edge is in the original direction.
* 0 means this is the reverse representation.

Example:
	0 → 1
	Store:
	0 : (1,1)
	1 : (0,0)

When DFS/BFS goes from 0 to 1, it sees 1, meaning the road must be reversed.

####################################################################################################

Example

Input
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]

Graph becomes
0 : (1,1), (4,0)
1 : (0,0), (3,1)
2 : (3,1)
3 : (1,0), (2,0)
4 : (0,1), (5,1)
5 : (4,0)

DFS from 0
0
├── 1   (+1)
│     └──3 (+1)
│          └──2 (+0)
└──4 (+0)
      └──5 (+1)

Total
1 + 1 + 0 + 0 + 1 = 3
Answer = 3

####################################################################################################

Why does this work?

Whenever DFS moves away from city 0:
* If the road also points away from 0, it is wrong and must be reversed.
* If it already points toward 0, leave it unchanged.

Since the graph is a tree, every edge is visited exactly once, so every required reversal is counted exactly once.

####################################################################################################
DFS Solution

from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        graph = defaultdict(list)

        for u, v in connections:
            graph[u].append((v, 1))   # original direction
            graph[v].append((u, 0))   # reverse direction

        visited = set()
        ans = 0

        def dfs(node):
            nonlocal ans
            visited.add(node)

            for nei, needs_reverse in graph[node]:
                if nei not in visited:
                    ans += needs_reverse
                    dfs(nei)

        dfs(0)
        return ans

####################################################################################################
BFS Solution

from collections import defaultdict, deque
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]):

        graph = defaultdict(list)

        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))

        visited = {0}
        q = deque([0])

        ans = 0

        while q:
            node = q.popleft()

            for nei, needs_reverse in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    ans += needs_reverse
                    q.append(nei)

        return ans

####################################################################################################

Dry Run

Input
n = 6
0→1
1→3
2→3
4→0
4→5

Start
	visited = {0}
	ans = 0

Visit 0
	0 -> 1 (needs_reverse = 1)
	ans = 1

Visit 1
	1 -> 3 (needs_reverse = 1)
	ans = 2

Visit 3
	3 -> 2 (needs_reverse = 0)
	ans = 2

Visit 4
	0 <- 4
	needs_reverse = 0
	ans = 2

Visit 5
	4 -> 5
	needs_reverse = 1
	ans = 3

Return
	3

####################################################################################################

Complexity Analysis

* Time Complexity: O(n)
  * Building the graph takes O(n).
  * DFS/BFS visits every node and edge once.

* Space Complexity: O(n)
  * Adjacency list, visited set, and recursion stack (or queue).

'''
from collections import defaultdict
from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        graph = defaultdict(list)

        for u, v in connections:
            graph[u].append((v, 1))   # original direction
            graph[v].append((u, 0))   # reverse direction

        visited = set()
        ans = 0

        def dfs(node):
            nonlocal ans
            visited.add(node)

            for nei, needs_reverse in graph[node]:
                if nei not in visited:
                    ans += needs_reverse
                    dfs(nei)

        dfs(0)
        return ans

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # -------------------------
        # Examples from Question
        # -------------------------
        (
            3,
            [[1, 0], [2, 0]],
            0
        ),
        (
            6,
            [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]],
            3
        ),
        (
            5,
            [[1, 0], [1, 2], [3, 2], [3, 4]],
            2
        ),

        # -------------------------
        # Smallest Tree
        # -------------------------
        (
            2,
            [[0, 1]],
            1
        ),
        (
            2,
            [[1, 0]],
            0
        ),

        # -------------------------
        # Chain
        # -------------------------
        (
            5,
            [[0, 1], [1, 2], [2, 3], [3, 4]],
            4
        ),
        (
            5,
            [[1, 0], [2, 1], [3, 2], [4, 3]],
            0
        ),

        # -------------------------
        # Star
        # -------------------------
        (
            5,
            [[0, 1], [0, 2], [0, 3], [0, 4]],
            4
        ),
        (
            5,
            [[1, 0], [2, 0], [3, 0], [4, 0]],
            0
        ),

        # -------------------------
        # Mixed Trees
        # -------------------------
        (
            7,
            [[0, 1], [2, 0], [3, 2], [3, 4], [5, 4], [6, 5]],
            2
        ),
        (
            7,
            [[1, 0], [1, 2], [3, 1], [4, 3], [5, 4], [6, 5]],
            1
        ),
        (
            8,
            [[0, 1], [2, 1], [3, 2], [4, 2], [4, 5], [6, 5], [7, 6]],
            4
        ),
        (
            8,
            [[1, 0], [2, 1], [2, 3], [4, 2], [5, 4], [5, 6], [7, 6]],
            2
        ),
        (
            9,
            [[0, 1], [2, 0], [2, 3], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7]],
            6
        ),
        (
            9,
            [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7]],
            0
        ),
    ]

    for i, (n, connections, expected) in enumerate(test_cases, 1):
        result = solution.minReorder(n, connections)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test Case {i}: {status} | "
            f"Expected = {expected}, Got = {result}"
        )