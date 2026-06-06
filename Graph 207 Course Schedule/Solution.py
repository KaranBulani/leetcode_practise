'''
1. Understanding the Problem
We have:
* numCourses courses labeled from 0 to numCourses - 1
* prerequisites[i] = [a, b]
  * To take course a, you must first complete course b

Return:
* True → if it is possible to finish all courses
* False → if it is impossible

### Example 1
numCourses = 2
prerequisites = [[1,0]]

Graph: 0 → 1
Take: 0 → 1
Possible.
Output: True

### Example 2
numCourses = 2
prerequisites = [[1,0],[0,1]]

Graph:
0 → 1
↑   ↓
└───┘
Cycle exists.

Output:False

####################################################################################################
2. Key Observation

The only reason we cannot finish all courses is:
> A cycle exists in the prerequisite graph.

Example:
0 requires 1
1 requires 2
2 requires 0

Before taking:
0 → need 1
1 → need 2
2 → need 0

Impossible.

So the problem becomes:
> Detect whether a directed graph contains a cycle.

####################################################################################################
3. Graph Representation

For:
prerequisites = [[1,0],[2,1]]

Meaning:
1 requires 0
2 requires 1

Store:
graph = {
    0: [1],
    1: [2]
}

Edge: 0 → 1 → 2

####################################################################################################
4. DFS Cycle Detection Idea

We'll maintain:

visited - Courses already fully processed.

visited = {0,1}
If we reach them again:
No need to explore again.

path - Courses currently in the DFS recursion stack.

Example:
DFS(0)
  DFS(1)
    DFS(2)
Then:
path = {0,1,2}
If during DFS we see a node already in path: 0 → 1 → 2 → 0
Cycle found.
Return: False

####################################################################################################
5. Dry Run

Input
numCourses = 2
prerequisites = [[1,0],[0,1]]

Graph:
	0 → 1
	1 → 0

Start:
	visited = {}
	path = {}

DFS(0)
path = {0}

Explore neighbor: 1
DFS(1)
path = {0,1}

Explore neighbor: 0
DFS(0)

Check: 0 in path
Yes.
Cycle found.
Return: False

####################################################################################################
6. Algorithm
For every course:
	1. Run DFS if not already processed.
	2. During DFS:
	   * If node in current path → cycle found
	   * If node already visited → skip
	3. Add node to path
	4. Explore neighbors
	5. Remove node from path
	6. Add node to visited
	7. If no cycle found anywhere → return True

####################################################################################################
8. Complexity Analysis
Let:
* V = numCourses
* E = len(prerequisites)

Time Complexity
	Each course is fully processed once: O(V)
	Each edge is explored once: O(E)
	Total: O(V + E)

Space Complexity
	Graph - Stores all vertices and edges: O(V + E)
	Visited Set: O(V)
	Path Set - O(V)

	Recursion Stack
	In worst case: 0 → 1 → 2 → ... → V-1
	Depth: O(V)
	Total auxiliary space: O(V)

	Overall space including graph: O(V + E)
'''
from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visited = set()
        path = set()
        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True

            path.add(course)
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            path.remove(course)
            # A node should enter visited only when we are completely sure:
            # "I explored every path starting from this node and found no cycle.".
            # Hence, added later
            visited.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1
        {
            "numCourses": 2,
            "prerequisites": [[1, 0]],
            "expected": True
        },

        # Example 2 (simple cycle)
        {
            "numCourses": 2,
            "prerequisites": [[1, 0], [0, 1]],
            "expected": False
        },

        # No prerequisites
        {
            "numCourses": 5,
            "prerequisites": [],
            "expected": True
        },

        # Single course
        {
            "numCourses": 1,
            "prerequisites": [],
            "expected": True
        },

        # Linear chain
        # 0 -> 1 -> 2 -> 3
        {
            "numCourses": 4,
            "prerequisites": [[1, 0], [2, 1], [3, 2]],
            "expected": True
        },

        # Longer cycle
        # 0 -> 1 -> 2 -> 3 -> 0
        {
            "numCourses": 4,
            "prerequisites": [[1, 0], [2, 1], [3, 2], [0, 3]],
            "expected": False
        },

        # Multiple disconnected components, no cycles
        {
            "numCourses": 6,
            "prerequisites": [[1, 0], [3, 2], [5, 4]],
            "expected": True
        },

        # Multiple disconnected components, one contains a cycle
        {
            "numCourses": 6,
            "prerequisites": [[1, 0], [0, 1], [3, 2], [5, 4]],
            "expected": False
        },

        # Diamond dependency
        #     0
        #    / \
        #   1   2
        #    \ /
        #     3
        {
            "numCourses": 4,
            "prerequisites": [[1, 0], [2, 0], [3, 1], [3, 2]],
            "expected": True
        },

        # Cycle not involving all nodes
        {
            "numCourses": 5,
            "prerequisites": [[1, 0], [2, 1], [1, 2]],
            "expected": False
        },

        # Isolated nodes present
        {
            "numCourses": 7,
            "prerequisites": [[1, 0], [2, 1]],
            "expected": True
        },

        # Complex DAG
        {
            "numCourses": 8,
            "prerequisites": [
                [1, 0],
                [2, 0],
                [3, 1],
                [3, 2],
                [4, 3],
                [5, 3],
                [6, 4],
                [7, 5]
            ],
            "expected": True
        },

        # Complex graph with cycle deep inside
        {
            "numCourses": 8,
            "prerequisites": [
                [1, 0],
                [2, 1],
                [3, 2],
                [4, 3],
                [2, 4]
            ],
            "expected": False
        },
    ]

    for i, test in enumerate(test_cases, start=1):
        result = solution.canFinish(
            test["numCourses"],
            test["prerequisites"]
        )

        print(f"Test Case {i}")
        print(f"numCourses    = {test['numCourses']}")
        print(f"prerequisites = {test['prerequisites']}")
        print(f"Expected      = {test['expected']}")
        print(f"Got           = {result}")
        print(f"PASS          = {result == test['expected']}")
        print("-" * 50)