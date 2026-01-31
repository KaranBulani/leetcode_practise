'''
Time Complexity:
    - Union-Find operations take O(α(n)) amortized time, whereas its actually 2 *  O(α(n)) due to 2 find operation
    - Total unions: O(e · α(n))
    - Final traversal of nodes: O(n)

Space Complexity:
    O(n)            for each - self.parent, self.rank
    O(α(n))         recursion stack due to self.find()`
'''
from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = {}
        self.rank = {}
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, x: int):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return

        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[px] = py
            self.rank[py] += 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for x, y in edges:
            uf.union(x, y)

        res = 0
        for i in range(n):
            if uf.parent[i] == i:
                res += 1
        return res

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # 1️⃣ Example from problem statement (multiple components)
        {
            "n": 5,
            "edges": [[0,1],[1,2],[3,4]],
            "description": "Two separate components",
            "expected": "More than one component"
        },

        # 2️⃣ Example from problem statement (fully connected chain)
        {
            "n": 5,
            "edges": [[0,1],[1,2],[2,3],[3,4]],
            "description": "All nodes connected",
            "expected": "Single component"
        },

        # 3️⃣ No edges at all
        {
            "n": 4,
            "edges": [],
            "description": "No edges, all nodes isolated",
            "expected": "Each node is its own component"
        },

        # 4️⃣ Single node graph
        {
            "n": 1,
            "edges": [],
            "description": "Single node, no edges",
            "expected": "Exactly one component"
        },

        # 5️⃣ Star topology
        {
            "n": 6,
            "edges": [[0,1],[0,2],[0,3],[0,4],[0,5]],
            "description": "One central node connected to all",
            "expected": "Single component"
        },

        # 6️⃣ Multiple small disconnected clusters
        {
            "n": 8,
            "edges": [[0,1],[2,3],[4,5]],
            "description": "Several small disconnected components",
            "expected": "More than two components"
        },

        # 7️⃣ Chain + isolated node
        {
            "n": 6,
            "edges": [[0,1],[1,2],[2,3]],
            "description": "One chain and isolated nodes",
            "expected": "More than one component"
        },

        # 8️⃣ Dense subgraph + isolated nodes
        {
            "n": 7,
            "edges": [[0,1],[1,2],[2,0],[3,4]],
            "description": "Cycle + pair + isolated nodes",
            "expected": "Multiple components"
        }
    ]

    for idx, test in enumerate(test_cases, 1):
        result = solution.countComponents(test["n"], test["edges"])
        print(f"Test Case {idx}: {test['description']}")
        print(f"Result: {result}")
        print(f"Expected: {test['expected']}")
        print("-" * 50)