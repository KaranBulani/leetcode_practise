'''
tuple1 = (10, 20, 30)
tuple2 = (10, 15, 40)
tuple3 = (5, 50)
tuple4 = (10, 20, 30, 40)

print(max(tuple1, tuple2)) # Output: (10, 20, 30) (because 20 > 15)
print(max(tuple1, tuple3)) # Output: (10, 20, 30) (because 10 > 5)
print(max(tuple1, tuple4)) # Output: (10, 20, 30, 40) (because tuple4 is a longer prefix match)

####################################################################################################
############################################### DFS ################################################
####################################################################################################

edges = [[0,1],[0,2],[2,3],[2,4],[4,5]]

STEP 1: Build graph (adjacency list)
| Node | Neighbors |
| ---- | --------- |
| 0    | [1, 2]    |
| 1    | [0]       |
| 2    | [0, 3, 4] |
| 3    | [2]       |
| 4    | [2, 5]    |
| 5    | [4]       |

STEP 2: First DFS (start at 0)
We start DFS(0):
* Visit 0 → children: 1 and 2

Explore 1
→ DFS(1): only neighbor is 0 (parent), so we return (1, 1) (distance = 1 from 0)
Explore 2
→ DFS(2):
    - go to 3 → DFS(3): returns (2, 3)
    - go to 4 → DFS(4):
        • go to 5 → DFS(5): returns (3, 5)
        • DFS(4) compares (3, 5) and (2, 3), picks (3, 5)
Now from 0’s perspective, farthest distance is 3 (to node 5).
✅ So first DFS gives far_node = 5.

STEP 3: Second DFS (start at 5)
Now we start from 5:
5 — 4 — 2 — 0 — 1
          \
           3
Traverse:
* From 5 to 4 → distance 1
* From 4 to 2 → distance 2
* From 2 to 0 → distance 3
* From 0 to 1 → distance 4
  or from 2 to 3 → distance 3
The farthest node from 5 is 1, with distance 4.
✅ So diameter = 4 edges.

STEP 4: Intuition check
Longest path: 1 → 0 → 2 → 4 → 5
That’s 4 edges, exactly the diameter we found.

Time complexity:  O(n)						    DFS
Space complexity: O(n)							graph

from collections import defaultdict

class Solution:
    def treeDiameter(self, edges):
        if not edges:
            return 0

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, parent, dist):
            farthest = (dist, node)
            for nei in graph[node]:
                # To avoid child parent forever loop
                if nei != parent:
                    farthest = max(farthest, dfs(nei, node, dist + 1))
            return farthest

        _, far_node = dfs(edges[0][0], -1, 0)
        diameter, _ = dfs(far_node, -1, 0)
        return diameter

####################################################################################################
############################################### BFS ################################################
####################################################################################################

edges = [[0,1],[0,2],[2,3],[2,4],[4,5]]

STEP 1: Build adjacency list again
| Node | Neighbors |
| ---- | --------- |
| 0    | [1, 2]    |
| 1    | [0]       |
| 2    | [0, 3, 4] |
| 3    | [2]       |
| 4    | [2, 5]    |
| 5    | [4]       |

STEP 2: First BFS from node 0
We start with:
queue = [(0, 0)]
visited = {0}

Now BFS expands level by level:
| Level | Current Node | Neighbors Added | Queue After Expansion | Farthest Node |
| ----- | ------------ | --------------- | --------------------- | ------------- |
| 0     | 0            | [1, 2]          | [(1,1), (2,1)]        | 0             |
| 1     | 1            | []              | [(2,1)]               | 1             |
| 1     | 2            | [3, 4]          | [(3,2), (4,2)]        | 2             |
| 2     | 3            | []              | [(4,2)]               | 3             |
| 2     | 4            | [5]             | [(5,3)]               | 4             |
| 3     | 5            | []              | []                    | 5             |
✅ At the end of the first BFS,
farthest_node = 5, distance = 3.

STEP 3: Second BFS from node 5
Start:
queue = [(5,0)]
visited = {5}

Now again, BFS expands:
| Level | Current Node | Neighbors Added | Queue After Expansion | Farthest Node |
| ----- | ------------ | --------------- | --------------------- | ------------- |
| 0     | 5            | [4]             | [(4,1)]               | 5             |
| 1     | 4            | [2]             | [(2,2)]               | 4             |
| 2     | 2            | [0,3]           | [(0,3),(3,3)]         | 2             |
| 3     | 0            | [1]             | [(3,3),(1,4)]         | 0             |
| 3     | 3            | []              | [(1,4)]               | 3             |
| 4     | 1            | []              | []                    | 1             |
✅ Farthest node = 1, distance = 4
Hence, diameter = 4.

STEP 4: Longest path found
1 → 0 → 2 → 4 → 5 (4 edges)

Time complexity:  O(n)						    DFS
Space complexity: O(n)							queue

'''
from collections import defaultdict, deque

class Solution:
    def treeDiameter(self, edges):
        if not edges:
            return 0

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(start):
            visited = set([start])
            queue = deque([(start, 0)])
            farthest_node = start
            max_dist = 0

            while queue:
                node, dist = queue.popleft()
                if dist > max_dist:
                    max_dist = dist
                    farthest_node = node
                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, dist + 1))
            return farthest_node, max_dist

        far_node, _ = bfs(edges[0][0])
        _, diameter = bfs(far_node)
        return diameter


if __name__ == "__main__":
    solution = Solution()

    # Example cases from the problem
    print(solution.treeDiameter([[0, 1], [0, 2]]))  # Expected: 2
    print(solution.treeDiameter([[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]))  # Expected: 4