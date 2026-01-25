'''
####################################################################################################
############################################### DFS ################################################
####################################################################################################
from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges):
        graph = defaultdict(list)

        def dfs(curr, target, visited):
            if curr == target:
                return True

            visited.add(curr)
            for nei in graph[curr]:
                if nei not in visited:
                    if dfs(nei, target, visited):
                        return True
            return False

        for u, v in edges:
            visited = set()

            # check if path already exists
            if u in graph and v in graph:
                if dfs(u, v, visited):
                    return [u, v]

            # add edge
            graph[u].append(v)
            graph[v].append(u)

⏱️ Complexity
Time: O(n²) (worst case DFS for each edge)
Space: O(n) (graph + recursion stack)

####################################################################################################
############################################ UNION FIND ############################################
####################################################################################################

For edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
at the end
 * self.parent = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
 * self.rank = {1: 1, 2: 0, 3: 0, 4: 0, 5: 0}

Time Complexity  -->    For each edge (u, v), we do 2 × find                        find(u) find(v)                 amortized O(α(n))
                                                  + 1 union per edge                union(u, v)                     O(1)
                        For n edge we do above ^ n times
                        O(n * cost per edge)

                        O(n * α(n))

                        O(n)

Space Complexity -->    O(n) for rank & parent
                        α(n) for find's recursion depth which is Negligible

'''
from typing import List

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x: int):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, edge: List[int]) -> bool:
        x, y = edge
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return True

        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[py] < self.rank[px]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind()
        res = []
        for e in edges:
            is_cycle = uf.union(e)
            if is_cycle:
                res.append(e)
        return res[-1]

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # 2. Cycle appears later (example 2)
        {
            "edges": [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]],
            "expected": [1, 4]
        },

        # 1. Basic cycle (example 1)
        {
            "edges": [[1, 2], [1, 3], [2, 3]],
            "expected": [2, 3]
        },

        # 3. Simple triangle, last edge closes cycle
        {
            "edges": [[1, 2], [2, 3], [1, 3]],
            "expected": [1, 3]
        },

        # 4. Linear chain + one back edge to root
        {
            "edges": [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]],
            "expected": [1, 5]
        },

        # 5. Multiple cycles possible → return LAST one in input
        {
            "edges": [[1, 2], [2, 3], [3, 1], [3, 4], [4, 1]],
            "expected": [4, 1]
        },

        # 6. Star-shaped tree with cycle at the end
        {
            "edges": [[1, 2], [1, 3], [1, 4], [1, 5], [2, 5]],
            "expected": [2, 5]
        },

        # 7. Cycle not involving node 1
        {
            "edges": [[1, 2], [2, 3], [3, 4], [2, 4]],
            "expected": [2, 4]
        },

        # 8. Minimum size constraint (n = 3)
        {
            "edges": [[1, 2], [2, 3], [1, 3]],
            "expected": [1, 3]
        },

        # 9. Larger graph, cycle late in input
        {
            "edges": [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [2, 6]],
            "expected": [2, 6]
        },

        # 10. Cycle created by connecting two deep nodes
        {
            "edges": [[1, 2], [2, 3], [3, 4], [4, 5], [2, 5]],
            "expected": [2, 5]
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = solution.findRedundantConnection(test["edges"])
        print(f"Test Case {i}:")
        print(f"Edges     : {test['edges']}")
        print(f"Output    : {result}")
        print(f"Expected  : {test['expected']}")
        print(f"Pass      : {result == test['expected']}")
        print("-" * 50)