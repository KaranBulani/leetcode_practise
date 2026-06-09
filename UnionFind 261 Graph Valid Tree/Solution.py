'''
### Important Shortcut

A very useful tree property:
> An undirected graph is a tree iff it is connected and contains exactly n - 1 edges.
Therefore many solutions start with:
	if len(edges) != n - 1:
		return False

Once this condition passes:
* DFS/BFS only needs to verify connectivity.
* Union Find only needs to verify no cycle is formed.

####################################################################################################
####################################################################################################

### Approach 1: DFS + Cycle Detection + Connectivity Check

For an undirected graph to be a valid tree:
1. It must not contain a cycle.
2. It must be fully connected (all n nodes reachable).
Since the graph is undirected, when visiting a neighbor, we must ignore the edge leading back to the parent.
####################################################################################################

Idea:
* Build adjacency list.
* DFS from node 0.
* If we reach an already visited node that is not the parent, a cycle exists.
* After DFS, verify all nodes were visited.
####################################################################################################
Time Complexity

    Build Graph
        We process every edge once:
            for u, v in edges:
        Cost: O(E)

    DFS Traversal
        Each node is visited once.
        Each edge is examined twice (undirected graph).
        Cost: O(V + E)

Total Time - O(V + E)

Space Complexity

    Adjacency List
        Stores every edge twice: O(V + E)

    Visited Set O(V)

    Recursion Stack
        Worst case (chain graph): 0 - 1 - 2 - 3 - 4
        Depth: O(V)

Total Space - O(V + E)

####################################################################################################
####################################################################################################

### Approach 2: BFS + Cycle Detection + Connectivity Check
Same logic as DFS, but using a queue.
####################################################################################################

from collections import defaultdict, deque
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        queue = deque([(0, -1)])  # (node, parent)

        while queue:
            node, parent = queue.popleft()

            if node in visited:
                return False

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue

                queue.append((neighbor, node))

        return len(visited) == n

####################################################################################################
Time Complexity

Build Graph O(E)

BFS Traversal
Every node visited once.
Every edge processed twice. O(V + E)

Total Time - O(V + E)

Space Complexity

Graph O(V + E)

Queue
	Worst case: O(V)
	Visited: O(V)

Total Space: O(V + E)

####################################################################################################
####################################################################################################
### Approach 3: Union Find (Disjoint Set Union)
This is arguably the cleanest solution.

Observation:
A graph is a tree iff:
1. It has exactly n - 1 edges.
2. Adding every edge never creates a cycle.

Idea
* If len(edges) != n - 1, immediately return False.
* Process edges using Union Find.
* If two nodes already belong to the same set, adding the edge creates a cycle → False.
* Otherwise union them.
* If all edges are processed successfully, return True.

####################################################################################################
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        parent = [i for i in range(n)]

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            pa = find(a)
            pb = find(b)

            if pa == pb:
                return False

            parent[pb] = pa
            return True

        for a, b in edges:
            if not union(a, b):
                return False

        return True

####################################################################################################

Time Complexity

	Edge Count Check - O(1)

	Processing Edges
	For each edge: union(u, v)
	Each union performs:
		find(u)
		find(v)
	With Path Compression: O(α(V))
	where: α(V) = Inverse Ackermann Function
	which grows so slowly that: α(V) ≤ 5
	for any realistic input size.

Total Time - O(E · α(V))
Practically: O(E)

Space Complexity

	Parent array:
	parent = [0,1,2,...]

	Size: O(V)
	No graph construction needed.

Total Space  O(V)
####################################################################################################
'''

from collections import defaultdict
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in graph[node]:
                # Ignore the edge back to the parent
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False

            return True

        # Check for cycle
        if not dfs(0, -1):
            return False
        # Check connectivity
        return len(visited) == n

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1 (Valid Tree)
        (
            5,
            [[0, 1], [0, 2], [0, 3], [1, 4]],
            True
        ),

        # Example 2 (Contains Cycle)
        (
            5,
            [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]],
            False
        ),

        # Single Node
        (
            1,
            [],
            True
        ),

        # Two Nodes Connected
        (
            2,
            [[0, 1]],
            True
        ),

        # Two Nodes Disconnected
        (
            2,
            [],
            False
        ),

        # Disconnected Graph
        (
            4,
            [[0, 1], [2, 3]],
            False
        ),

        # Simple Cycle
        (
            3,
            [[0, 1], [1, 2], [2, 0]],
            False
        ),

        # Tree with More Nodes
        (
            6,
            [[0, 1], [0, 2], [0, 3], [3, 4], [4, 5]],
            True
        ),

        # Connected but Contains Cycle
        (
            6,
            [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]],
            False
        ),

        # Connected Component + Isolated Node
        (
            5,
            [[0, 1], [1, 2], [2, 3]],
            False
        ),

        # Too Many Edges (Guaranteed Cycle)
        (
            4,
            [[0, 1], [1, 2], [2, 3], [3, 0]],
            False
        ),

        # Star-Shaped Tree
        (
            7,
            [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6]],
            True
        ),

        # Linear Chain
        (
            7,
            [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],
            True
        ),
    ]

    for i, (n, edges, expected) in enumerate(test_cases, start=1):
        result = solution.validTree(n, edges)
        print(
            f"Test Case {i}: "
            f"Expected={expected}, "
            f"Got={result}, "
            f"{'PASS' if result == expected else 'FAIL'}"
        )