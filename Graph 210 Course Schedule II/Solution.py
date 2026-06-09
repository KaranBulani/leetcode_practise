'''
You are given:
* numCourses courses: 0 to numCourses - 1
* prerequisites[i] = [a, b]
  * To take course a, you must first take course b
  * Edge: b → a
This is a topological sorting problem.

####################################################################################################
# Solution 1: BFS (Kahn's Algorithm)

## Idea
A course can be taken if its indegree = 0.
1. Build graph
2. Compute indegree of every node
3. Put all indegree-0 nodes into queue
4. Pop from queue:
   * Add to answer
   * Reduce indegree of neighbors
   * If neighbor becomes 0, push into queue
5. If answer contains all courses → valid ordering
6. Otherwise cycle exists → return []

## Example
numCourses = 4
prerequisites = [ [1,0], [2,0], [3,1], [3,2] ]

Graph:
	0 → 1
	0 → 2
	1 → 3
	2 → 3
Indegree:
	0 : 0
	1 : 1
	2 : 1
	3 : 2
Queue:		[0]

Process:
	0
	↓
	1,2
	↓
	3

Result:		[0,1,2,3]
####################################################################################################
## BFS Code

from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        order = []
        while queue:
            course = queue.popleft()
            order.append(course)

            for neighbor in graph[course]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return order if len(order) == numCourses else []
####################################################################################################
# Solution 2: DFS (Topological Sort)

## Idea
In DFS topological sort:
* Visit all descendants first
* Then add current node
This naturally creates reverse topological order.

To detect cycles:
### State array
	0 = unvisited
	1 = visiting (currently in recursion stack)
	2 = visited

If we encounter a node with state 1:		back edge	⇒ cycle

## Example
Graph:
	0 → 1
	0 → 2
	1 → 3
	2 → 3

DFS:
     0
	 ├─1
	 │  └─3
	 └─2

Append after finishing:
	3
	1
	2
	0

Reverse:		0 2 1 3
Valid topological order.
####################################################################################################
## DFS Code

####################################################################################################
# Complexity Analysis

### Time and space complexity — why both are O(V + E)
Let V = numCourses (vertices) and E = len(prerequisites) (directed edges).

### BFS (Kahn's Algorithm)

Time complexity: O(V + E)

Breakdown:
1. Build adjacency list and indegree array: process each prerequisite once → O(E).
2. Initialize queue: scan all vertices to find indegree 0 → O(V).
3. Main BFS loop: each course is dequeued at most once → O(V) total queue pops.
4. For every dequeued course, iterate its outgoing edges. Across the entire run, every edge is examined exactly once, causing one indegree decrement per edge → O(E).
O(E) + O(V) + O(V) + O(E) = O(V+E)

Space complexity: O(V + E)

Components:
| Structure      | Size            |
| -------------- | --------------- |
| Adjacency list | O(V + E)        |
| Indegree array | O(V)            |
| Queue          | O(V) worst case |
| Output order   | O(V)            |
The adjacency list dominates because it stores all vertices and all edges.
O(V+E) + O(V) + O(V) + O(V) = O(V+E)

### DFS Topological Sort

Time complexity: O(V + E)
Breakdown:
1. Build adjacency list: O(E).
2. Outer loop over all courses: O(V) checks.
3. DFS traversal: because of the 3-state array (0=unvisited, 1=visiting, 2=visited), each vertex transitions through the states once, so each vertex is fully processed at most once → O(V).
4. When processing a vertex, you iterate its outgoing edges. Across the whole execution, every edge is traversed at most once → O(E).
O(E) + O(V) + O(V) + O(E) = O(V+E)

Space complexity: O(V + E)

Components:
| Structure       | Size            |
| --------------- | --------------- |
| Adjacency list  | O(V + E)        |
| State array     | O(V)            |
| Recursion stack | O(V) worst case |
| Output order    | O(V)            |

Why can the recursion stack be O(V)? In the worst case the graph is a chain:
DFS goes all the way down before returning, so the call stack depth becomes V.
O(V+E) + O(V) + O(V) + O(V) = O(V+E)

### The key intuition

* Vertices: each course is processed once → contributes O(V).
* Edges: each prerequisite relation is examined once → contributes O(E).
* Total:  O(V+E)O(V+E)O(V+E)
* Memory: storing the graph itself already costs O(V+E), which dominates the extra arrays/queues/stacks → O(V+E) space.

Bottom line
| Approach             | Time     | Space    |
| -------------------- | -------- | -------- |
| BFS (Kahn)           | O(V + E) | O(V + E) |
| DFS Topological Sort | O(V + E) | O(V + E) |
They have the same asymptotic complexity; the practical differences are queue + indegree array vs recursion stack + state array and implementation style.
'''
from typing import List
from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        state = [0] * numCourses
        order = []
        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True

            state[course] = 1
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            state[course] = 2
            order.append(course)
            return True

        for course in range(numCourses):
            if state[course] == 0:
                if not dfs(course):
                    return []

        return order[::-1]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1
        {
            "numCourses": 2,
            "prerequisites": [[1, 0]],
            "expected": "[0,1]"
        },

        # Example 2 (multiple valid answers exist)
        {
            "numCourses": 4,
            "prerequisites": [[1, 0], [2, 0], [3, 1], [3, 2]],
            "expected": "Any valid topological ordering, e.g. [0,1,2,3] or [0,2,1,3]"
        },

        # Example 3
        {
            "numCourses": 1,
            "prerequisites": [],
            "expected": "[0]"
        },

        # No prerequisites at all
        {
            "numCourses": 5,
            "prerequisites": [],
            "expected": "Any permutation containing all courses 0..4"
        },

        # Simple cycle
        {
            "numCourses": 2,
            "prerequisites": [[1, 0], [0, 1]],
            "expected": "[]"
        },

        # Longer cycle
        {
            "numCourses": 4,
            "prerequisites": [[1, 0], [2, 1], [3, 2], [0, 3]],
            "expected": "[]"
        },

        # Chain dependency
        {
            "numCourses": 5,
            "prerequisites": [[1, 0], [2, 1], [3, 2], [4, 3]],
            "expected": "[0,1,2,3,4]"
        },

        # Diamond dependency
        {
            "numCourses": 4,
            "prerequisites": [[1, 0], [2, 0], [3, 1], [3, 2]],
            "expected": "0 before 1 and 2, and both before 3"
        },

        # Multiple disconnected components
        {
            "numCourses": 6,
            "prerequisites": [[1, 0], [3, 2], [5, 4]],
            "expected": "Any valid ordering satisfying each pair"
        },

        # One independent course
        {
            "numCourses": 4,
            "prerequisites": [[1, 0], [2, 1]],
            "expected": "0 before 1 before 2, course 3 anywhere"
        },

        # All courses depend on one root
        {
            "numCourses": 5,
            "prerequisites": [[1, 0], [2, 0], [3, 0], [4, 0]],
            "expected": "0 must appear before all others"
        },

        # Reverse chain input order
        {
            "numCourses": 5,
            "prerequisites": [[4, 3], [3, 2], [2, 1], [1, 0]],
            "expected": "[0,1,2,3,4]"
        },

        # Complex DAG
        {
            "numCourses": 8,
            "prerequisites": [
                [1, 0],
                [2, 0],
                [3, 1],
                [3, 2],
                [4, 1],
                [5, 3],
                [6, 4],
                [7, 5],
                [7, 6]
            ],
            "expected": "Any valid topological ordering"
        },

        # Cycle in only one component
        {
            "numCourses": 6,
            "prerequisites": [
                [1, 0],
                [0, 1],   # cycle
                [3, 2],
                [5, 4]
            ],
            "expected": "[]"
        },

        # Single course self-contained graph
        {
            "numCourses": 2,
            "prerequisites": [],
            "expected": "Any permutation of [0,1]"
        }
    ]

    for idx, test in enumerate(test_cases, start=1):
        result = solution.findOrder(
            test["numCourses"],
            test["prerequisites"]
        )

        print(f"\nTest Case {idx}")
        print(f"numCourses   = {test['numCourses']}")
        print(f"prerequisites= {test['prerequisites']}")
        print(f"Expected     = {test['expected']}")
        print(f"Your Output  = {result}")