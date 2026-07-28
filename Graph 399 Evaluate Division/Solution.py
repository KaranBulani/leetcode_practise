'''
1. Intuition

We are given equations like:
	a / b = 2
	b / c = 3

From these, we should be able to answer queries such as:
	a / c = ?

Since,
	a / c
	= (a / b) × (b / c)
	= 2 × 3
	= 6

This naturally looks like a graph problem.
* Every variable is a node.
* Every equation creates two directed edges.

Example:
	a / b = 2
	a ----2----> b
	a <---1/2--- b

Similarly,
	b / c = 3
	b ----3----> c
	b <---1/3--- c

Entire graph:
	a --2--> b --3--> c

To answer
	a / c

we simply find a path from a to c and multiply all edge weights.
	2 × 3 = 6

So every query becomes:
> Can I reach destination? If yes, multiply edge weights along the path.
This is exactly a DFS/BFS traversal.
####################################################################################################


2. Graph Construction

For every equation
	A / B = value

store
	A → B : value
	B → A : 1/value

Example
	equations = [["a","b"],["b","c"]]
	values = [2,3]

Graph becomes
	a:
		b (2)
	b:
		a (1/2)
		c (3)
	c:
		b (1/3)

Python:
	graph = defaultdict(list)
	for i in range(len(values)):
		u, v = equations[i]
		graph[u].append((v, values[i]))
		graph[v].append((u, 1 / values[i]))

####################################################################################################

3. DFS

Suppose query is
	a / c

DFS starts at a.
	product = 1

Visit neighbor
	a -> b (2)
	product = 2

Then
	b -> c (3)
	product = 2 × 3 = 6

Reached destination.

Return
	6

####################################################################################################

Base Cases

Case 1
Variable doesn't exist.
	x / y

If either variable isn't in graph
	return -1

####################################################################################################

Case 2
Source equals destination.
	a / a

If variable exists,
	answer = 1

because
	a/a = 1

####################################################################################################

Case 3

No path exists.
	a     c

Disconnected graph.

Return
	-1

####################################################################################################

4. Example Walkthrough

Input


equations = [ ["a","b"], ["b","c"] ]
values = [2, 3]
queries = [
 ["a","c"],
 ["b","a"],
 ["a","e"],
 ["a","a"],
 ["x","x"]
]


Graph
	a --2--> b --3--> c

####################################################################################################

Query 1
	a/c

DFS
	a
	product = 1
	↓
	b
	product = 2
	↓
	c
	product = 6

Answer
	6

####################################################################################################

Query 2
	b/a

	b -> a
	weight = 1/2

Answer
	0.5

####################################################################################################

Query 3
	a/e
e doesn't exist.

Answer
	-1


####################################################################################################

Query 4
	a/a

Variable exists.
Answer
	1

####################################################################################################

Query 5
	x/x

Variable doesn't exist.

Answer
	-1


####################################################################################################

5. Algorithm

For every query:
* If source/destination absent
  * return -1
* If source == destination
  * return 1
* Run DFS
* Multiply weights while moving
* If destination reached
  * return accumulated product
* Else
  * return -1

####################################################################################################

6. Correctness Proof

We prove that the algorithm returns the correct answer for every query.
Let the query be (u, v).

Case 1: Variable missing
	If either u or v does not appear in any equation, there is no information to determine the ratio.
	The algorithm returns -1, which is correct.

####################################################################################################

Case 2: u == v

	For any known variable,
	u / u = 1
	The algorithm immediately returns 1, which is correct.

####################################################################################################

Case 3: A path exists
	Every graph edge represents a valid equation:
	x / y = w

	Suppose DFS finds the path
	u → x1 → x2 → ... → v

	The product computed is
	(u/x1) × (x1/x2) × ... × (last/v)

	Intermediate variables cancel:
	(u/x1)
	× (x1/x2)
	× (x2/x3)
	...
	× (last/v)
	= u/v

	Thus the accumulated product equals the desired ratio.

####################################################################################################

Case 4: No path exists

If DFS cannot reach v, no sequence of given equations connects u and v.
Hence their ratio cannot be determined.
Returning -1 is correct.

####################################################################################################

Since all possible cases are handled correctly, the algorithm is correct.

####################################################################################################

7. Complexity Analysis

Let
* N = number of variables
* E = number of equations
* Q = number of queries

Graph construction: 	O(E)
Each DFS: 	O(N + E)
Overall:	O(E + Q × (N + E))

Space:
	Graph:	O(N + E)
	Visited set:	O(N)
	Total:	O(N + E)


####################################################################################################
'''
from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(list)
        # Build graph
        for (u, v), value in zip(equations, values):
            graph[u].append((v, value))
            graph[v].append((u, 1 / value))

        def dfs(curr, target, product, visited):
            if curr == target:
                return product

            visited.add(curr)

            for nxt, weight in graph[curr]:
                if nxt not in visited:
                    ans = dfs(nxt, target, product * weight, visited)
                    if ans != -1:
                        return ans

            return -1

        answer = []
        for src, dst in queries:
            if src not in graph or dst not in graph:
                answer.append(-1.0)
            elif src == dst:
                answer.append(1.0)
            else:
                answer.append(dfs(src, dst, 1.0, set()))
        return answer

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        {
            "name": "Example 1",
            "equations": [["a", "b"], ["b", "c"]],
            "values": [2.0, 3.0],
            "queries": [
                ["a", "c"],
                ["b", "a"],
                ["a", "e"],
                ["a", "a"],
                ["x", "x"]
            ],
            "expected": [6.0, 0.5, -1.0, 1.0, -1.0]
        },
        {
            "name": "Example 2",
            "equations": [["a", "b"], ["b", "c"], ["bc", "cd"]],
            "values": [1.5, 2.5, 5.0],
            "queries": [
                ["a", "c"],
                ["c", "b"],
                ["bc", "cd"],
                ["cd", "bc"]
            ],
            "expected": [3.75, 0.4, 5.0, 0.2]
        },
        {
            "name": "Example 3",
            "equations": [["a", "b"]],
            "values": [0.5],
            "queries": [
                ["a", "b"],
                ["b", "a"],
                ["a", "c"],
                ["x", "y"]
            ],
            "expected": [0.5, 2.0, -1.0, -1.0]
        },

        # ---------------- Additional Edge Cases ----------------

        {
            "name": "Single Variable Queries",
            "equations": [["a", "b"]],
            "values": [2.0],
            "queries": [
                ["a", "a"],
                ["b", "b"],
                ["a", "b"],
                ["b", "a"]
            ],
            "expected": [1.0, 1.0, 2.0, 0.5]
        },

        {
            "name": "Disconnected Components",
            "equations": [["a", "b"], ["c", "d"]],
            "values": [2.0, 4.0],
            "queries": [
                ["a", "d"],
                ["c", "d"],
                ["d", "c"],
                ["b", "a"]
            ],
            "expected": [-1.0, 4.0, 0.25, 0.5]
        },

        {
            "name": "Long Chain",
            "equations": [["a", "b"], ["b", "c"], ["c", "d"], ["d", "e"]],
            "values": [2.0, 3.0, 4.0, 5.0],
            "queries": [
                ["a", "e"],
                ["e", "a"],
                ["b", "d"],
                ["d", "b"]
            ],
            "expected": [120.0, 1 / 120.0, 12.0, 1 / 12.0]
        },

        {
            "name": "Unknown Variables",
            "equations": [["a", "b"], ["b", "c"]],
            "values": [2.0, 3.0],
            "queries": [
                ["x", "a"],
                ["a", "x"],
                ["x", "x"],
                ["c", "x"]
            ],
            "expected": [-1.0, -1.0, -1.0, -1.0]
        },

        {
            "name": "Variables With Digits",
            "equations": [["x1", "x2"], ["x2", "x3"]],
            "values": [4.0, 2.5],
            "queries": [
                ["x1", "x3"],
                ["x3", "x1"],
                ["x2", "x1"]
            ],
            "expected": [10.0, 0.1, 0.25]
        },

        {
            "name": "Fractional Values",
            "equations": [["a", "b"], ["b", "c"]],
            "values": [0.5, 0.25],
            "queries": [
                ["a", "c"],
                ["c", "a"],
                ["b", "a"]
            ],
            "expected": [0.125, 8.0, 2.0]
        },

        {
            "name": "Bidirectional Check",
            "equations": [["usd", "eur"], ["eur", "inr"]],
            "values": [0.8, 100.0],
            "queries": [
                ["usd", "inr"],
                ["inr", "usd"],
                ["eur", "usd"],
                ["eur", "inr"]
            ],
            "expected": [80.0, 0.0125, 1.25, 100.0]
        },
    ]

    for i, test in enumerate(test_cases, 1):
        print("=" * 60)
        print(f"Test Case {i}: {test['name']}")

        result = solution.calcEquation(
            test["equations"],
            test["values"],
            test["queries"]
        )

        print("Result   :", result)
        print("Expected :", test["expected"])
        print("Pass     :", result == test["expected"])